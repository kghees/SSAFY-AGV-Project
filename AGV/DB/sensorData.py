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
# 자신이 만든 변수에 맞게 넣고 사용하면 됨
write_data_to_firebase(humid, temp, distance, led_state)
