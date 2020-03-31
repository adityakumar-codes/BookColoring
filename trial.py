import cv2
import imutils
import numpy as np

def linePoints(p1,p2):
    points = []
    [x1,y1] = p1[0]
    [x2,y2] = p2[0]
    for x in range(x1,x2):
        y = int((x - x1)*((y2-y1)/(x2-x1)) + y1)
        points.append([x,y])

    return points

def linePoints2(p1,p2):
    points = []
    [x1,y1] = p1
    [x2,y2] = p2
    for y in range(y1,y2):
        x = int((y - y1)*((x2-x1)/(y2-y1)) + x1)
        points.append([x,y])

    return points


image = cv2.imread("pls.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

# find contours (i.e. the 'outlines') in the image and initialize the
# total number of books found
(cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total=0
    
# loop over the contours
for c in cnts:
# approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    # if the approximated contour has four points, then assume that the
    # contour is a book -- a book is a rectangle and thus has four vertices
    if len(approx) == 4:
       cv2.drawContours(image, [approx], -1, (255, 0, 0), 4)
       total += 1
       print(peri)
       for p in approx:
           print(p[0])


line1 = linePoints(approx[0],approx[3])
line2 = linePoints(approx[1],approx[2])
lines = []

print(len(line1),len(line2))

for n in range(0,min(len(line1),len(line2))):
    line = linePoints2(line1[n],line2[n])
    lines.append(line)

for line in lines:
    for point in line:
        x = point[1]
        y = point[0]
        image[x][y] = [0,125,255]
        


cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600,600)
print("I found {0} books in that image".format(total))
cv2.imshow("image", image)
cv2.waitKey(0)
