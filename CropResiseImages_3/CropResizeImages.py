import cv2

#how to resize an image

path = "Ressources/PlagueTale.jpg"
img = cv2.imread(path)

width, height = 350, 250
imgResize = cv2.resize(img, (width, height))
imgResize = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
print("img resize : " + str(imgResize.shape))

#this return () is the height, width and number of channels
print("img : " + str(img.shape))

cv2.imshow("Plague Tale", img)
cv2.imshow("Plague Tale Resize", imgResize)

#cv2.waitKey(0)



#--------------------------------------------

#how to crop an image  // extract Amicia & Hugo 🐀

imgCropped  =img[60:168, 120:180]
cv2.imshow("Plague Tale Cropped", imgCropped)

#cv2.waitKey(0)


##########################################"""""""

# resize this image  into the original size

# cv.resize(imgCropped, (height, width))
imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0])) 

cv2.imshow("plague tale cropped resized" , imgCropResize)

#cv2.waitKey(0)

#######################"""""""
# test on my own
import numpy

kernel = numpy.ones((5,5), numpy.uint8)
imgRoded = cv2.erode(imgCropResize, kernel, iterations=1)

cv2.imshow("eroded plague", imgRoded)

#cv2.waitKey(0)


##############################

imgDilated = cv2.dilate(imgRoded, kernel, iterations=1)

cv2.imshow("dilated plague", imgDilated)

cv2.waitKey(0)
