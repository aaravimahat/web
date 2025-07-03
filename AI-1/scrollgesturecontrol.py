import cv2
import mediapipe as mp
import time
import pyautogui

h=mp.solutions.hands
hands=h.Hands(max_num_hands=1, min_detection_confidence=0.7)
d=mp.solutions.drawing_utils

scroll_speed=50
scroll_delay=0.5

c=cv2.VideoCapture(0)

f=[8,12,16,20]

def a(landmarks):
    finger=[]
    for tips in f:
        if landmarks.landmark[tips].y<landmarks.landmark[tips-2].y:
            finger.append(1)

        else:
            finger.append(0)
    return finger
l=time.time()

while True:
    s,img=c.read()

    if not s:
        break
    img=cv2.flip(img,1)
    r=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    re=hands.process(r)

    if re.multi_hand_landmarks:
        for i in re.multi_hand_landmarks:
         d.draw_landmarks(img,i,h.HAND_CONNECTIONS)

         finger=a(i)
         total=sum(finger)
         cv2.putText(img,f"finger{total}",(50,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),6)
         if total==5 and (time.time()-l)>scroll_delay:
            pyautogui.scroll(-scroll_speed)
            l()

    cv2.imshow("the hand gesture control", img)
    if cv2.waitKey(1)==ord("q"):
        break
c.release()
cv2.destroyAllWindows()



