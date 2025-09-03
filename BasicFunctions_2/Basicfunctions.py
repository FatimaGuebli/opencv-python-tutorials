import cv2

#learn gray scale

#basic image settings  :
'''
path = "Ressources/PlagueTale.jpg"
img = cv2.imread(path)

cv2.imshow("A plague tale", img)
cv2.waitKey(0)
'''

#gray scale 

'''
path = "Ressources/PlagueTale.jpg" 
img = cv2.imread(path,0)

cv2.imshow("A Plague Tale", img)
cv2.waitKey(0)
'''


# how to put the grayscale into funtion

path = "Ressources/PlagueTale.jpg"
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

cv2.imshow("A plague Tale", img)
cv2.imshow("a plague tale grayscale", imgGray)
cv2.imshow("plague tale blur & gray", imgBlur)

#cv2.waitKey(0)



########################################################"
# edge detector


imgCanny = cv2.Canny(imgBlur, 100, 100)

cv2.imshow("plague tale canny", imgCanny)
#cv2.waitKey(0)

"""
once we have these edges
is that 
we can increase their size 
and decrease their size
we call it as dilation

"""
"""
Kernel : 
isa matrix that 
we use to iterate through the image itself
to perform a function
"""

#kernel is used in dilation

#we need to import numpy 
import numpy

kernel = numpy.ones((5,5), numpy.uint8)
print(kernel)

imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

cv2.imshow("plague tale dilation", imgDilation)

#cv2.waitKey(0)


######################################################

#erosion : the reverse of dilation

imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

cv2.imshow("plaguetale eroded", imgEroded)

cv2.waitKey(0)
