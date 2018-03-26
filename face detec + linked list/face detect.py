import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier("C:\\Users\\risha\\Desktop\\haarcascade_frontalface_default.xml")  #loading classifier/detector
img=cv2.imread('C:\\Users\\risha\\OneDrive\\Pictures\\Camera Roll\\WP_20140518_002.jpg')    #loading image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                   #creating grayscale version of the image
faces=face_cascade.detectMultiScale(gray, 1.1, 5)           #executing the detector
kernel = np.ones((30, 30), np.float32) / 900                #averaging kernel
blur = cv2.filter2D(img, -1, kernel)                        #blurring image copy
for(x,y,w,h) in faces:
    face=img[y:y+h,x:x+w]
    blur[y:y+h,x:x+w]=face                                  #copying the face onto the blurred copy of the image
    cv2.rectangle(blur, (x, y), (x + w, y + h), (255, 0, 0), 2)         #drawing rectangle around the face
plt.subplot(121),plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)),plt.title('Original')     #displaying
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)),plt.title('Processed')
plt.xticks([]), plt.yticks([])
plt.show()
