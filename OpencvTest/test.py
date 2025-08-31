import cv2

# how to illustrate an image for 5 seconds
'''
import cv2

img = cv2.imread("Ressources/PlagueTale.jpg")

cv2.imshow("PlagueTale", img)
cv2.waitKey(5000)

'''

################################################
# display a video
'''
frameWidth = 640
frameHeight = 360

cap = cv2.VideoCapture("Ressources/Forest.mp4")

while True : 
    # the video will be stored in mg, & if it suceed, success will be tru
    sucess, img = cap.read() 
    cv2.imshow("Video", img)

    #cv2.waitKey(0): Waits forever for me to press any key.
    #& 0xFF == ord('q'): Checks if the key you pressed was the 'q' key.
    if cv2.waitKey(1) & 0xFF == ord('q'):  #stop for 1ms & keep going / normal speed
        break

        '''

##############################################"
# use webcam
 
'''
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)

cap.set(3, frameWidth) #3 for height
cap.set(4, frameHeight) #4 for height

while True: 
 sucess, img = cap.read()
 cv2.imshow("Video", img)

 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
 '''

########################################################

#resize screen for video

framewidth = 640
frameHeight = 100

cap = cv2.VideoCapture("Ressources/Forest.mp4")

while True: 
    success, img = cap.read()
    img = cv2.resize(img,(framewidth, frameHeight))
    cv2.imshow("VideoForest", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break