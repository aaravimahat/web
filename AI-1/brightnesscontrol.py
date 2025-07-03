import os

def set_brightness_mac(level):
    # level should be a float between 0.0 (dark) and 1.0 (full brightness)
    os.system(f"brightness {level}")

# Example: Set to 70% brightness
set_brightness_mac(0.7)


import cv2
import mediapipe as mp

import numpy
import math
import platform

import screen_brightness_control as sbc




h=mp.solutions.hands
g=h.Hands()
d=mp.solutions.drawing_utils
c=cv2.VideoCapture(0)

while True:
    s,image=c.read()
    rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    r=g.process(rgb)

    if r.multi_hand_landmarks:
        for i in r.multi_hand_landmarks:
            l=[]
            for id,lm in enumerate(i.landmark):
                h,w,c=image.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                l.append((cx,cy))
            if l:
                x1,y1=l[4]
                x2,y2=l[8]

                length=math.hypot(x2-x1,y2-y1)
                brightness=int(max(0,min(100,(length-30)*2)))
                sbc.set_brightness(brightness)
                cv2.circle(image, (x1,y1),7,(255,0,0),cv2.FILLED)
                cv2.circle(image, (x2,y2),7,(255,0,0),cv2.FILLED)
                cv2.line(image,(x1,y1),(x2,y2),(0,255,0),5)
                cv2.putText(image,f"brightness:{brightness}", (50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(245,255,255),3)
            d.draw_landmarks(image,i,h.HAND_CONNECTIONS)

    cv2.imshow("the gesture control", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


