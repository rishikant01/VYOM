import cv2

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) 
cam.set(3,1280) #framewith
cam.set(4,720) #frameheight

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#haar classifier : object detection approch

face_id = input("Enter numeric user ID here: ")
#unique integer id for each face

print("Taking samples, look at camera >>>>> ")
count=0

while True:
    #print("Running..........")
    ret, img=cam.read() #reads the frames using the above created object
    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image,1.3,5)

    for(x,y,w,h) in faces:
        #print("For loop running..........")

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #used to draw ractangle on image
        count+=1

        cv2.imwrite("samples/face."+ str(face_id) + '.'+ str(count)+".jpg",converted_image[y:y+h,x:x+w])
        
        cv2.imshow("image",img) #displays image on the screen

    k=cv2.waitKey(100) & 0xff #waiting for pressed key
    if k == 27:  # Any key press
        break
    elif count >=50: #take 50 samples (more samples will give more accuracy)
        break

print("Samples taken now closing the window >>>>>>> ")
cam.release()
cv2.destroyAllWindows()