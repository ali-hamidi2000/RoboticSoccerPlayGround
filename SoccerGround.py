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
penaltyRadius = int(0.075 * meter2Pixel)
robotSize = int(0.27 * meter2Pixel)
radius = int(1.5 / 2 * meter2Pixel)
'''
#-----------------Adult robot proportions---------------
fieldLength = 14 * meter2Pixel
fieldWidth = 9 * meter2Pixel
goalDepth = 0.6 * meter2Pixel
goalWidth = 2.6 * meter2Pixel
goalHeight = 1.8 * meter2Pixel
goalAreaLength = 1 * meter2Pixel
goalAreaWidth = 4 * meter2Pixel
penaltyMarkDistance = 2.1 * meter2Pixel
centerCircleDiameter = 3 * meter2Pixel
borderStripWidth = 1 * meter2Pixel
penaltyAreaLength = 3 * meter2Pixel
penaltyAreaWidth = 6 * meter2Pixel

windowWidth = fieldWidth + 2 * borderStripWidth
windowLength = fieldLength + 2 * borderStripWidth
penaltyRadius = int(0.075 * meter2Pixel)
robotSize = int(0.27 * meter2Pixel)
radius = int(1.5 / 2 * meter2Pixel)
'''


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


#-----------------Center Circle Diameter------------
CenterCircleDiameter = (borderStripWidth+fieldLength//2, borderStripWidth+fieldWidth//2)
cv2.circle(Ground, CenterCircleDiameter, radius, (255, 255, 255), 2, 8, 0)

#-----------------Start Match Circle-----------------
StartMatchCircle = (borderStripWidth+fieldLength//2, borderStripWidth+fieldWidth//2)
cv2.circle(Ground, StartMatchCircle, penaltyRadius, (255, 255, 255), -1, 8, 0)

#-----------------Penalty Mark Distance Left---------
PenaltyMarkDistanceLeft = (int(borderStripWidth + penaltyMarkDistance), (borderStripWidth + fieldWidth//2))
cv2.circle(Ground, PenaltyMarkDistanceLeft, penaltyRadius, (255, 255, 255), -1, 8, 0)

#-----------------Penalty Mark Distance Right--------
PenaltyMarkDistanceRight = (int(borderStripWidth + fieldLength - penaltyMarkDistance), (borderStripWidth + fieldWidth//2))
cv2.circle(Ground, PenaltyMarkDistanceRight, penaltyRadius, (255, 255, 255), -1, 8, 0)

#-----------------Goal Width Left--------------------
pointGoalWidthLeftA = (int(borderStripWidth - goalDepth), int(borderStripWidth + fieldWidth//2 - goalWidth//2))
pointGoalWidthLeftB = (int(borderStripWidth - goalDepth), int(borderStripWidth + fieldWidth//2 + goalWidth//2))
cv2.line(Ground, pointGoalWidthLeftA, pointGoalWidthLeftB, (0, 255, 255), 2, 8, 0)

#-----------------Goal Depth Left UP-----------------
pointGoalDepthLeftUPA = (int(borderStripWidth - goalDepth),int(borderStripWidth + fieldWidth//2 - goalWidth//2))
pointGoalDepthLeftUPB = (int(borderStripWidth), int(borderStripWidth + fieldWidth//2 - goalWidth//2))
cv2.line(Ground, pointGoalDepthLeftUPA, pointGoalDepthLeftUPB, (0, 255, 255), 2, 8, 0)

#-----------------Goal Depth Left Down---------------
pointGoalDepthLeftDownA = (int(borderStripWidth - goalDepth), int(borderStripWidth + fieldWidth//2 + goalWidth//2))
pointGoalDepthLeftDownB = (int(borderStripWidth), int(borderStripWidth + fieldWidth//2 + goalWidth//2))
cv2.line(Ground, pointGoalDepthLeftDownA, pointGoalDepthLeftDownB, (0, 255, 255), 2, 8, 0)

#-----------------Goal Width Right-------------------
pointGoalWidthRightA = (int(borderStripWidth + fieldLength + goalDepth), int(borderStripWidth + fieldWidth//2 - goalWidth//2))
pointGoalWidthRightB = (int(borderStripWidth + fieldLength + goalDepth), int(borderStripWidth + fieldWidth//2 + goalWidth//2))
cv2.line(Ground, pointGoalWidthRightA, pointGoalWidthRightB, (255, 255, 0), 2, 8, 0)

#-----------------Goal Depth Right UP----------------
GoalDepthRightUPA = (int(borderStripWidth + fieldLength + goalDepth), int(borderStripWidth + fieldWidth//2 - goalWidth//2))
GoalDepthRightUPB = (int(borderStripWidth + fieldLength), int(borderStripWidth + fieldWidth//2 - goalWidth//2))
cv2.line(Ground, GoalDepthRightUPA, GoalDepthRightUPB, (255, 255, 0), 2, 8, 0)
#-----------------Goal Depth Right Down--------------
GoalDepthRightDownA = (int(borderStripWidth + fieldLength + goalDepth), int(borderStripWidth + fieldWidth//2 + goalWidth//2))
GoalDepthRightDownB = (int(borderStripWidth + fieldLength), int(borderStripWidth + fieldWidth//2 + goalWidth//2))
cv2.line(Ground, GoalDepthRightDownA, GoalDepthRightDownB, (255, 255, 0), 2, 8, 0)

'''
#----------------Robot--------------
robot = (borderStripWidth+fieldLength//2,borderStripWidth+fieldWidth//2)
cv2.circle(Ground, robot, robotSize, (255, 0, 255), 2, 8, 0)
#----------------Direction----------
pointDirectionA = (borderStripWidth + fieldLength//2,borderStripWidth + fieldWidth//2)
pointDirectionB = (borderStripWidth + fieldLength//2 - (2*robotSize), borderStripWidth + fieldWidth//2 -(2*robotSize))
cv2.line(Ground, pointDirectionA, pointDirectionB, (255, 0, 255), 2, 8, 0)
'''

cv2.imshow("SoccerGround", Ground)
cv2.waitKey(0)
cv2.destroyAllWindows()
