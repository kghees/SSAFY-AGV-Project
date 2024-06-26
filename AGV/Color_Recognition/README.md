# Color_Recognition

HSV 모델 <br>
프레임 내의 특정 픽셀의 HSV값을 획득하여 후속 색상 추적기능을 사용한다. <br>
HSV 색상 휠은 원뿔 혹은 원형으로 나타낼 수 있으면 3가지 구성요소를 가진다. <br>

HSV: Hue(색상), Saturation(채도), Value(명도)의 약자로, 인간이 색을 인식하는 방식에 더 가깝게 색을 표현한다. <br>

Hue(색상): 0도에서 360도까지의 값으로, 색상 환에서의 각도를 나타낸다. 예를 들어, 빨강은 0도, 초록은 120도, 파랑은 240도이다. <br>

Saturation(채도): 색의 강도를 나타내며, 0%에서 100%까지의 값을 가진다. 0%는 회색(무채색)을 의미하고, 100%는 가장 강한 색을 의미힌다. <br>
Value(명도): 색의 밝기를 나타내며, 0%에서 100%까지의 값을 가진다. 0%는 검정(가장 어두운 상태)을 의미하고, 100%는 가장 밝은 상태를 의미한다. 
<br>

![image](https://github.com/kghees/SSAFY-AGV-Project/assets/92205960/9d0669c2-1f92-458a-b1a9-21f8cb3f395e)  


## Working Area Inspection
우선, 인공지능 무인운반차량(AGV)을 수동 조작하여 map에 있는 색상 값의 HSV 값을 조사한다.
<br>

(이떄 조건은 항상 같은 조건을 가질 수 있는 위치에서 진행한다. <br>
 빛의 밝기, 빛의 방향의 조건들로인해 측정할 때 마다 달라질 수 있다.) <br>
 ![image](https://github.com/kghees/SSAFY-AGV-Project/assets/92205960/06781399-275f-4f94-9546-0cfc5e40b7e7)
 ![image](https://github.com/kghees/SSAFY-AGV-Project/assets/92205960/c9f20a59-1b53-4587-bb57-47c1b3af8eec)  
 
이미지에서 중심점을 이동한 이유는 경로를 따라가가 보니 중앙의 측정 위치는 검은색 경로위에 놓이게된다. <br>
"colorRecog() 클래스 생성하기" 하기에 있는 frame_width, frame_height의 수치를 조정해서 측정하고자하는 위치를 변경시킬 수 있다.
