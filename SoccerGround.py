import cv2 # pip install opencv-python
import numpy as np # pip install numpy

meter2Pixel = 100
#-----------------KidSize robot proportions---------------
fieldLength = 9 * meter2Pixel
fieldWidth = 6 * meter2Pixel
goalDepth = 0.6 * meter2Pixel
goalWidth = 2.6 * meter2Pixel
goalHeight = 1.2 * meter2Pixel
goalAreaLength = 1 * meter2Pixel
goalAreaWidth = 3 * meter2Pixel
penaltyMarkDistance = 1.5 * meter2Pixel
centerCircleDiameter = 1.5 * meter2Pixel
borderStripWidth = 1 * meter2Pixel
penaltyAreaLength = 2 * meter2Pixel
penaltyAreaWidth = 5 * meter2Pixel

windowWidth = fieldWidth + 2 * borderStripWidth
windowLength = fieldLength + 2 * borderStripWidth
penaltyRadius = 0.075 * meter2Pixel
robotSize = 0.27 * meter2Pixel
radius = 1.5 / 2 * meter2Pixel



#-----------------Create a empty green Ground---------------
Ground = np.zeros((windowWidth, windowLength, 3), np.uint8)
Ground[:] = (0, 150, 0)

# Points corresponding to the quadrant of the Ground
pointA = (borderStripWidth, borderStripWidth)
pointB = (borderStripWidth + fieldLength, borderStripWidth)
pointC = (borderStripWidth + fieldLength, borderStripWidth + fieldWidth)
pointD = (borderStripWidth, borderStripWidth + fieldWidth)

cv2.line(Ground, pointA, pointD, (255, 255, 255), 2, 8, 0)
cv2.line(Ground, pointB, pointC, (255, 255, 255), 2, 8, 0)
cv2.line(Ground, pointC, pointD, (255, 255, 255), 2, 8, 0)
cv2.line(Ground, pointA, pointB, (255, 255, 255), 2, 8, 0)

#-----------------Middle Line---------------
pointMiddlelineA = (borderStripWidth + fieldLength//2, borderStripWidth)
pointMiddlelineB = (borderStripWidth + fieldLength//2, borderStripWidth + fieldWidth)
cv2.line(Ground, pointMiddlelineA, pointMiddlelineB, (255, 255, 255), 2, 8, 0)

#-----------------Penalty Area Length---------------
#----------------------Left Up----------------------
pointPenaltyAreaLengthLeftUpA = (borderStripWidth, borderStripWidth + (fieldWidth//2 - penaltyAreaWidth//2))
pointPenaltyAreaLengthLeftUpB = (borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth//2 - penaltyAreaWidth//2))
cv2.line(Ground, pointPenaltyAreaLengthLeftUpA, pointPenaltyAreaLengthLeftUpB, (255, 255, 255), 2, 8, 0)

#-----------------Penalty Area Length---------------
#----------------------Left Down--------------------
pointPenaltyAreaLengthDownA = (borderStripWidth, borderStripWidth + (fieldWidth//2 + penaltyAreaWidth//2))
pointPenaltyAreaLengthDownB = (borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth//2 + penaltyAreaWidth//2))
cv2.line(Ground, pointPenaltyAreaLengthDownA, pointPenaltyAreaLengthDownB, (255, 255, 255), 2, 8, 0)

#-----------------Penalty Area Length---------------
#----------------------Right Up---------------------
pointPenaltyAreaLengthRightUpA = (borderStripWidth + fieldLength, borderStripWidth + (fieldWidth//2 - penaltyAreaWidth//2))
pointPenaltyAreaLengthRightUpB = (borderStripWidth + fieldLength -  penaltyAreaLength, borderStripWidth + (fieldWidth//2 - penaltyAreaWidth//2))
cv2.line(Ground, pointPenaltyAreaLengthRightUpA, pointPenaltyAreaLengthRightUpB, (255, 255, 255), 2, 8, 0)

#-----------------Penalty Area Length---------------
#----------------------Right Down-------------------
pointPenaltyAreaLengthRightDownA = (borderStripWidth + fieldLength, borderStripWidth + (fieldWidth//2 + penaltyAreaWidth//2))
pointPenaltyAreaLengthRightDownB = (borderStripWidth + fieldLength - penaltyAreaLength, borderStripWidth + (fieldWidth//2 + penaltyAreaWidth//2))
cv2.line(Ground, pointPenaltyAreaLengthRightDownA, pointPenaltyAreaLengthRightDownB, (255, 255, 255), 2, 8, 0)

#-----------------Penalty Area Width----------------
#------------------------Left-----------------------
pointPenaltyAreaWidthLeftA = (borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth//2 - penaltyAreaWidth//2))
pointPenaltyAreaWidthLeftB = (borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth//2 + penaltyAreaWidth//2))
cv2.line(Ground, pointPenaltyAreaWidthLeftA, pointPenaltyAreaWidthLeftB, (255, 255, 255), 2, 8, 0)

#-----------------Penalty Area Width----------------
#------------------------Right----------------------
pointPenaltyAreaWidthRightA = (borderStripWidth + fieldLength - penaltyAreaLength, borderStripWidth + (fieldWidth//2 - penaltyAreaWidth//2))
pointPenaltyAreaWidthRightB = (borderStripWidth + fieldLength - penaltyAreaLength, borderStripWidth + (fieldWidth//2 + penaltyAreaWidth//2))
cv2.line(Ground, pointPenaltyAreaWidthRightA, pointPenaltyAreaWidthRightB, (255, 255, 255), 2, 8, 0)

#-----------------Goal Area Length------------------
#----------------------Left Up----------------------
pointGoalAreaLengthLeftUpA = (borderStripWidth, borderStripWidth + (fieldWidth//2 - goalAreaWidth//2))
pointGoalAreaLengthLeftUpB = (borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth//2 - goalAreaWidth//2))
cv2.line(Ground, pointGoalAreaLengthLeftUpA, pointGoalAreaLengthLeftUpB, (255, 255, 255), 2, 8, 0)

#-----------------Goal Area Length------------------
#----------------------Left Down--------------------
pointGoalAreaLengthLeftDownA = (borderStripWidth, borderStripWidth + (fieldWidth//2 + goalAreaWidth//2))
pointGoalAreaLengthLeftDownB = (borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth//2 + goalAreaWidth//2))
cv2.line(Ground, pointGoalAreaLengthLeftDownA, pointGoalAreaLengthLeftDownB, (255, 255, 255), 2, 8, 0)

#-----------------Goal Area Length------------------
#----------------------Right Up---------------------
pointGoalAreaLengthRightUpA = (borderStripWidth + fieldLength, borderStripWidth + (fieldWidth//2 - goalAreaWidth//2))
pointGoalAreaLengthRightUpB = (borderStripWidth + fieldLength - goalAreaLength, borderStripWidth + (fieldWidth//2 - goalAreaWidth//2))
cv2.line(Ground, pointGoalAreaLengthRightUpA, pointGoalAreaLengthRightUpB, (255, 255, 255), 2, 8, 0)

#-----------------Goal Area Length------------------
#----------------------Right Down-------------------
pointGoalAreaLengthRightDownA = (borderStripWidth + fieldLength, borderStripWidth + (fieldWidth//2 + goalAreaWidth//2))
pointGoalAreaLengthRightDownB = (borderStripWidth + fieldLength - goalAreaLength, borderStripWidth + (fieldWidth//2 + goalAreaWidth//2))
cv2.line(Ground, pointGoalAreaLengthRightDownA, pointGoalAreaLengthRightDownB, (255, 255, 255), 2, 8, 0)

#-----------------Goal Area Width-------------------
#------------------------Left-----------------------
pointGoalAreaWidthLeftA = (borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth//2 - goalAreaWidth//2))
pointGoalAreaWidthLeftB = (borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth//2 + goalAreaWidth//2))
cv2.line(Ground, pointGoalAreaWidthLeftA, pointGoalAreaWidthLeftB, (255, 255, 255), 2, 8, 0)

#-----------------Goal Area Width-------------------
#------------------------Right----------------------
pointGoalAreaWidthRightA = (borderStripWidth + fieldLength - goalAreaLength, borderStripWidth + (fieldWidth//2 - goalAreaWidth//2))
pointGoalAreaWidthRightB = (borderStripWidth + fieldLength -goalAreaLength, borderStripWidth + (fieldWidth//2 + goalAreaWidth//2))
cv2.line(Ground, pointGoalAreaWidthRightA, pointGoalAreaWidthRightB, (255, 255, 255), 2, 8, 0)

'''
#-----------------centerCircle-----------------
centerCircle = (borderStripWidth+fieldLength//2, borderStripWidth+fieldWidth//2)
cv2.circle(Ground, centerCircle, radius, (255, 255, 255), 2, 8, 0)
#-----------------centerCircle-----------------
centerCircleBold = (borderStripWidth+fieldLength//2, borderStripWidth+fieldWidth//2)
cv2.circle(Ground, centerCircleBold, penaltyRadius, (255, 255, 255), -1, 8, 0)
#-----------------Penalty Mark Distance Left----------------
PenaltyMarkDistanceLeft = (borderStripWidth + penaltyMarkDistance, (borderStripWidth + fieldWidth//2))
cv2.circle(Ground, PenaltyMarkDistanceLeft, penaltyRadius, (255, 255, 255), -1, 8, 0)
#-----------------Penalty Mark Distance Right---------------
PenaltyMarkDistanceRight = (borderStripWidth + fieldLength - penaltyMarkDistance, (borderStripWidth + fieldWidth//2))
cv2.circle(Ground, PenaltyMarkDistanceRight, penaltyRadius, (255, 255, 255), -1, 8, 0)
#-----------------GoalDepthLeft-----------------
pointGDA = (borderStripWidth - goalDepth, borderStripWidth + fieldWidth//2 - goalWidth//2)
pointGDB = (borderStripWidth - goalDepth, borderStripWidth + fieldWidth//2 + goalWidth//2)
cv2.line(Ground, pointGDA, pointGDB, (0, 255, 255), 2, 8, 0)
#-----------------GoalDepthUP-----------------
pointGDUA = (borderStripWidth - goalDepth, borderStripWidth + fieldWidth//2 - goalWidth//2)
pointGDUB = (borderStripWidth, borderStripWidth + fieldWidth//2 - goalWidth//2)
cv2.line(Ground, pointGDUA, pointGDUB, (0, 255, 255), 2, 8, 0)
#-----------------GoalDepthDown-----------------
pointGDDA = (borderStripWidth - goalDepth, borderStripWidth + fieldWidth//2 + goalWidth//2)
pointGDDB = (borderStripWidth, borderStripWidth + fieldWidth//2 + goalWidth//2)
cv2.line(Ground, pointGDDA, pointGDDB, (0, 255, 255), 2, 8, 0)
#-----------------GoalDepthRight-----------------
pointGDRA = (borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth//2 - goalWidth//2)
pointGDRB = (borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth//2 + goalWidth//2)
cv2.line(Ground, pointGDRA, pointGDRB, (255, 255, 0), 2, 8, 0)
#-----------------GoalDepthUP-----------------
pointGDRUA = (borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth//2 - goalWidth//2)
pointGDRUB = (borderStripWidth + fieldLength, borderStripWidth + fieldWidth//2 - goalWidth//2)
cv2.line(Ground, pointGDRUA, pointGDRUB, (255, 255, 0), 2, 8, 0)
#-----------------GoalDepthDown-----------------
pointGDRDA = (borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth//2 + goalWidth//2)
pointGDRDB = (borderStripWidth + fieldLength, borderStripWidth + fieldWidth//2 + goalWidth//2)
cv2.line(Ground, pointGDRDA, pointGDRDB, (255, 255, 0), 2, 8, 0)
#----------------Robot--------------
robot = (borderStripWidth+fieldLength//2,borderStripWidth+fieldWidth//2)
cv2.circle(Ground, robot, robotSize, (255, 0, 255), 2, 8, 0)

pointDirectionA = (borderStripWidth + fieldLength//2,borderStripWidth + fieldWidth//2)
pointDirectionB = (borderStripWidth + fieldLength//2 - (2*robotSize), borderStripWidth + fieldWidth//2 -(2*robotSize))
cv2.line(Ground, pointDirectionA, pointDirectionB, (255, 0, 255), 2, 8, 0)
'''

cv2.imshow("SoccerGround", Ground)
cv2.waitKey(0)
cv2.destroyAllWindows()
