import cv2
import numpy as np

c=cv2.VideoCapture(0)
if not c.isOpened():
    print("unable to open cam")
    exit()

while True:
    ret,frame=c.read()
    if not ret:
        print("failed to capture image")
        break

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_skin=np.array([0,30,60], dtype=np.uint8)
    u_skin=np.array([30,255,255],dtype=np.uint8)

    mask=cv2.inRange(hsv,l_skin,u_skin)
    r=cv2.bitwise_and(frame,frame,mask=mask)
    contour,d=cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contour:
        maxc=max(contour,key=cv2.contourArea)
        x,y,w,h=cv2.boundingRect(maxc)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),6)
        centerx=int(x+w/2)
        centery=int(y+h/2)
        cv2.circle(frame,(centerx,centery),8,(0,0,0),-1)
    cv2.imshow("orignal image", frame)
    cv2.imshow("filtered", r)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
c.release()
cv2.destroyAllWindows()




