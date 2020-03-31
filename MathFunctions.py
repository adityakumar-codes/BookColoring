import math


def distanceFormula(p1, p2):
    [x1, y1] = p1
    [x2, y2] = p2

    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))


def triangleArea(p1, p2, p3):
    a = distanceFormula(p1, p2)
    b = distanceFormula(p2, p3)
    c = distanceFormula(p3, p1)

    s = (a+b+c)/2
    return math.sqrt(s*abs(s-a)*abs(s-b)*abs(s-c))


def quadArea(p1, p2, p3, p4):
    return triangleArea(p1, p2, p3) + triangleArea(p1, p4, p3)


def approxEqual(a, b, factor=1):
    return abs(a-b) < 10


def pointTest(point, rectangle):
    p1 = rectangle[0]
    p2 = rectangle[1]
    p3 = rectangle[2]
    p4 = rectangle[3]

    a1 = triangleArea(point, p1, p2)
    a2 = triangleArea(point, p2, p3)
    a3 = triangleArea(point, p3, p4)
    a4 = triangleArea(point, p4, p1)

    area = a1 + a2 + a3 + a4
    area2 = quadArea(p1, p2, p3, p4)

    # print(area, area2)
    return approxEqual(area, area2)
