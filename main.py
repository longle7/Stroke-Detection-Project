import math
import sys
import cv2
import numpy as np

def imageToArray(fileName):
    #bring in image
    img_rgb = cv2.imread(fileName)
    #convert image to greyscale to get one value at each point
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    return img_gray

#first cut into squares then find avg of each square
#assume both images are same size
def avgSquare(normal, stroke):
    diffList = []
    row = len(normal)
    col = len(normal[0])
    rowSect = int(row/5) #138
    colSect = int(col/5) #108
    for x in range(0, row, rowSect):
        for y in range(0, col, colSect):
            areaNormal = normal[x:rowSect+x, y:colSect+y]
            areaStroke = stroke[x:rowSect+x, y:colSect+y]
            averageNormal = np.average(areaNormal)
            averageStroke = np.average(areaStroke)
            #myList.append(str(round(averageNormal, 2)))
            if not(math.isnan(averageNormal) or math.isnan(averageStroke)):
                diffList.append(round(abs(averageNormal - averageStroke)))

    threshHold = int(input("What is the threshhold? (avg is around 40): "))
    print(diffList)
    for x in range(len(diffList)):
        if diffList[x] > threshHold:
            return "There is a abnormality"
    return "There is no brain abnormality"

if __name__ == '__main__':
    normalBrain = imageToArray("normalBrain.png")
    strokeBrain = imageToArray("strokeBrain.png")
    #if we want to see whole array without truncation
    #numpy.set_printoptions(threshold=sys.maxsize)
    print(avgSquare(normalBrain,strokeBrain))




