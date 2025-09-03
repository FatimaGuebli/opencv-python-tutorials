import cv2
import numpy as np
#"create black image"

img = np.zeros((512,512))
#"size of img is matrix 512*512"



cv2.imshow("Blank",img)
#here we cannot store any colours

##################################""

#to store colours,  & 3 diff channels 
#we can store colours in 3 channels

imgBlank3 = np.zeros((512,512,3))

cv2.imshow("Blank3",imgBlank3)

########################"""
# 
# 0-255
'''
the values inside our 
matrix should be 8bit integers

uint means unsigned integer 

'''

imgColor = np.zeros((512,512,3), np.uint8)

print(imgColor)

cv2.imshow("Color",imgColor)


##################################
#we will colour with blue

imgBlue = np.zeros((512,512,3), np.uint8)
imgBlue[:]=255,0,0 #BGR

cv2.imshow("Blue",imgBlue)

'''
why we put [:] ?
in the cropping lesson
we needed to define the y 1st then the x
'''

imgBlueCrop = np.zeros((512,512,3), np.uint8)
imgBlueCrop[20:30, 60:100] = 255, 0, 0

cv2.imshow("imgblue crop", imgBlueCrop)
#we will see the all img black & only the crop in blue



###################################"
# #how to create lines on the img "

imgLine = np.zeros((512,512,3), np.uint8)
cv2.line(imgLine, (0,0), (500,500), (255,0,255), 5)

'''
we can create lines on the img using the cv2.line() function
(0,0) is the starting point of line
(500,500) is the ending point of line
(255,0,0) is colour of the line
Line thickness in pixels (use -1 to create a filled line)
'''

cv2.imshow("Line", imgLine)

########################################

imgWholeLine = np.zeros((512,512,3), np.uint8)
cv2.line(imgWholeLine, (0,0), (imgWholeLine.shape[1], imgWholeLine.shape[0]), (255,255,0), 1)


cv2.imshow("Whole Line", imgWholeLine)

##################################""

#how to  create a rectangle

imgRect = np.zeros((512,512,3), np.uint8)
cv2.rectangle(imgRect, (100,100), (400,400), (0,255,0), 5)
cv2.rectangle(imgRect, (200,200), (300,300), (255,0,0), cv2.FILLED)

# cv2.rectangle(img, (starting point), (ending point), (color), (thickness))

cv2.imshow("Rectangle", imgRect)

#################################

#draw a circle 

imgCircle = np.zeros((512,512,3), np.uint8)
cv2.circle(imgCircle, (256,256), 100, (0,0,255), 3)

#cv2.circle(img, (center), (radius), (color), (thickness))

cv2.imshow("Circle", imgCircle)


######################################

#add text to an image

cv2.putText(imgCircle, "Hello", (75,256), cv2.FONT_HERSHEY_COMPLEX, 2, (0,150,0), 2)

#cv2.putText(img, (text), (position), (font), (font scale), (color), (thickness))


cv2.imshow("Text", imgCircle)

cv2.waitKey(0)