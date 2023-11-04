import cv2
face_Cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread('girl.jpg')
resized = cv2.resize(image, (0, 0) ,fx=0.1, fy=0.1)
imgGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)
for (x, y, w, h) in faces:
  cv2.rectangle(resized, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow("Result", resized)
cv2.waitKey(0)