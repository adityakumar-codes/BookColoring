from MathFunctions import pointTest
import cv2
import imutils
import numpy as np
import sys

filename = sys.argv[1]

totalPage = input("how many pages in the book?")
pagesRead = input("how many pages have you read?")
percent = float(pagesRead)/float(totalPage)

image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)


(cnts, _) = cv2.findContours(closed.copy(),
                             cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total = 0
approx = 0


for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 4:
        #cv2.drawContours(image, [approx], -1, (255, 0, 0), 4)
        total += 1

[p1, p2, p3, p4] = approx


Y1 = min(p1[0][0], p2[0][0], p3[0][0], p4[0][0])
X1 = min(p1[0][1], p2[0][1], p3[0][1], p4[0][1])
Y2 = max(p1[0][0], p2[0][0], p3[0][0], p4[0][0])
X2 = max(p1[0][1], p2[0][1], p3[0][1], p4[0][1])

p1 = [p1[0][1], p1[0][0]]
p2 = [p2[0][1], p2[0][0]]
p3 = [p3[0][1], p3[0][0]]
p4 = [p4[0][1], p4[0][0]]

rectangle = [p1, p2, p3, p4]
points = []


for x in range(X1, X2):
    for y in range(Y1, Y2):
        if(pointTest([x, y], rectangle)):
            points.append([x, y])

length = (1-percent)*len(points)


for l in range(0, int(0.7*length)):
    p = points[l]
    x = p[0]
    y = p[1]
    image[x][y] = [255, 0, 0]


cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 600, 600)
cv2.imshow("image", image)
cv2.imwrite("output.jpeg", image)
cv2.waitKey(0)
