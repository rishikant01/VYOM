import cv2
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(r'C:\Users\HP\Desktop\VYOM\Face_detect\Trainer.yml')
cascadePath="haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

id=2

names=['','Rishi'] #leaving first space empty because counter starts from 0

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #DSHOW to remove warning
cam.set(3,1280)
cam.set(4,720)

#Defining minimum window side to be recognizeed as a face
minW=0.1*cam.get(3)
minH=0.1*cam.get(4)
flag=0
while True:
    ret,img=cam.read() #read the frames using the above created object
    converted_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW),int(minH))
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        label, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

        #checking accuracy
        if accuracy < 100:
            recognized_name = names[label]
            if recognized_name=='Rishi':
                flag=1
            #accuracy_str = "  {0}% Match Found".format(round(100 - accuracy))
        else:
            recognized_name = "unknown"
            accuracy_str = "  {0}% Match Found".format(round(100 - accuracy))

        cv2.putText(img, str(recognized_name), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(accuracy_str), (x+5, y+h-5), font, 1, (255, 255, 0), 1)


    cv2.imshow('camera',img)

    k= cv2.waitKey(10) & 0xff
    if k==27:
        break
cam.release()
cv2.destroyAllWindows()  
    
