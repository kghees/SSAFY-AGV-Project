from gpiozero import DistanceSensor
from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt
from firebase import firebase
from datetime import datetime
import pytz
import sys

# Firebase Realtime Database에 연결하는 Firebase 객체 생성
# project host url
firebase_url = ""
firebase = firebase.FirebaseApplication(firebase_url, None)

korea_timezone = pytz.timezone("Asia/Seoul")

# Sense HAT 및 거리 센서 초기화
sense = SenseHat()
sensor = DistanceSensor(echo=15, trigger=14)

# Sensor Hat에 띄울 색상 정의
red = (255, 0, 0)
green = (0, 255, 0)

# MQTT 클라이언트 설정
mqtt_broker = "192.168.110.134" # 실제 MQTT 브로커 주소로 변경
mqtt_port = 1883 # MQTT 브로커 포트
mqtt_client = mqtt.Client("SenseHATPublisher")

try:
    mqtt_client.connect(mqtt_broker, mqtt_port)
except Exception as e:
    print(f"MQTT Error: {e}")
    sys.exit(1)
    
# 클라이언트 루프 시작
mqtt_client.loop_start()

def write_data_to_firebase(humidity, temperature, distance, led_state):
    current_time = datetime.now(korea_timezone)
    time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "humidity": round(humidity, 2),
        "temperature": round(temperature, 2),
        "distance": round(distance, 2),
        "led_state": led_state
    }
    result = firebase.put("/sensorData", time, data)



while True:
    try:
        distance = sensor.distance * 100

        try:
            humid = sense.get_humidity()
        except OSError as e:
            print(f"humidity Error: {e}")
            humid = None

        try:
            temp = sense.get_temperature()
        except OSError as e:
            print(f"temperature Error: {e}")
            temp = None
            
        # 거리 값에 따른 LED 색상 설정
        if distance <= 8:
            for i in range(8):
                for j in range(8):
                    sense.set_pixel(i, j, red)
            led_state = "Object Detection"
        else:
            for i in range(8):
                for j in range(8):
                    sense.set_pixel(i, j, green)
            led_state = "Keep Going"
            
			  # 센서 데이터 출력 및 MQTT 퍼블리시
        if humid is not None:
            print(f"Humidity(%) : {humid:.2f}%")
            mqtt_client.publish("sensors/humidity", f"{humid:.2f}")

        if temp is not None:
            print(f"Temperature(C) : {temp:.2f}C")
            mqtt_client.publish("sensors/temperature", f"{temp:.2f}")

        print(f"Distance(cm) : {distance:.2f}cm")
        mqtt_client.publish("sensors/distance", f"{distance:.2f}")
        
        # LED 상태 퍼블리시
        mqtt_client.publish("sensors/led", led_state)


        write_data_to_firebase(humid, temp, distance, led_state)


    except Exception as e:
        print(f"Error: {e}")

    sleep(1)
    
# 클라이언트 루프 정지
mqtt_client.loop_stop()
