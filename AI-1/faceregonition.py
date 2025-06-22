import cv2
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

c=cv2.VideoCapture(0)

if not c.isOpened():
    print("error, camera couldnt be opened")
    exit()

while True:
    ret,frame=c.read()

    if not ret:
        print("failed to capture image")
        break
    g=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(g,scaleFactor=1.1,minNeighbors=5,minSize=(20,20))

    for (x,w,h,y) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),2)

    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'people count:{len(faces)}',(15,100),font,2,(255,0,0),2)

    cv2.imshow("face detecting and counting",frame)

    if cv2.waitKey(1) & 0xFF== ord("q"):
        break
c.release()
cv2.destroyAllWindows()


