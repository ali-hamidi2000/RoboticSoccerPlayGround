#include <opencv4/opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int meter2Pixel = 80; //you can change this part according to the specifications of your computer screen
int windowLength, radius, windowWidth, robotSize, penaltyRadius, fieldLength, fieldWidth, goalDepth, goalWidth, goalHeight, goalAreaLength, goalAreaWidth, penaltyMarkDistance, centerCircleDiameter, borderStripWidth, penaltyAreaWidth, penaltyAreaLength;
void initialize();
int main() {
    initialize();
    // make a window
    Mat Ground(windowWidth, windowLength, CV_8UC3, Scalar(0,50,0));

    // Draw the rectangle from point to point (A to B to C to D)
    //-----------------playGround-----------------
    Point pointA(borderStripWidth, borderStripWidth); //playGround-LeftUP
    Point pointB(borderStripWidth + fieldLength, borderStripWidth); //playGround-RightUp
    Point pointC(borderStripWidth + fieldLength, borderStripWidth + fieldWidth); //playGround-RightDown
    Point pointD(borderStripWidth, borderStripWidth + fieldWidth); //playGround-LeftDown
    line(Ground, pointA, pointD, Scalar(255, 255, 255), 2, 8, 0);
    line(Ground, pointB, pointC, Scalar(255, 255, 255), 2, 8, 0);
    line(Ground, pointC, pointD, Scalar(255, 255, 255), 2, 8, 0);
    line(Ground, pointA, pointB, Scalar(255, 255, 255), 2, 8, 0);

    // Draw the Line (the middle line of the ground) from point A to B
    Point pointMiddlelineA(borderStripWidth + fieldLength/2, borderStripWidth);
    Point pointMiddlelineB(borderStripWidth + fieldLength/2, borderStripWidth + fieldWidth);
    line(Ground, pointMiddlelineA, pointMiddlelineB, Scalar(255, 255, 255), 2, 8, 0);
/
    //-----------------centerCircle-----------------
	Point centerCircle(borderStripWidth+fieldLength/2,borderStripWidth+fieldWidth/2);
	circle(Ground, centerCircle, radius, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------centerCircle-----------------
	Point centerCircleBold(borderStripWidth+fieldLength/2,borderStripWidth+fieldWidth/2);
	circle(Ground, centerCircleBold, penaltyRadius, Scalar(255, 255, 255), -1, 8, 0);
    
    //-----------------Penalty Mark Distance Left----------------
    Point PenaltyMarkDistanceLeft(borderStripWidth + penaltyMarkDistance, (borderStripWidth + fieldWidth/2));
	circle(Ground, PenaltyMarkDistanceLeft, penaltyRadius, Scalar(255, 255, 255), -1, 8, 0);

    //-----------------Penalty Mark Distance Right---------------
    Point PenaltyMarkDistanceRight(borderStripWidth + fieldLength - penaltyMarkDistance, (borderStripWidth + fieldWidth/2));
	circle(Ground, PenaltyMarkDistanceRight, penaltyRadius, Scalar(255, 255, 255), -1, 8, 0);

    //-----------------PenaltyAreaLengthUp---------------
    Point pointPenaltyAreaLengthUpA(borderStripWidth, borderStripWidth + (fieldWidth/2 - penaltyAreaWidth/2));
    Point pointPenaltyAreaLengthUpB(borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth/2 - penaltyAreaWidth/2));
    line(Ground, pointPenaltyAreaLengthUpA, pointPenaltyAreaLengthUpB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------GoalAreaLengthDown---------------
    Point pointGoalAreaLengthDownA(borderStripWidth, borderStripWidth + (fieldWidth/2 + penaltyAreaWidth/2));
    Point pointGoalAreaLengthDownB(borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth/2 + penaltyAreaWidth/2));
    line(Ground, pointGoalAreaLengthDownA, pointGoalAreaLengthDownB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------GoalAreaLengthRight---------------
    Point pointGoalAreaLengthRightA(borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth/2 - penaltyAreaWidth/2));
    Point pointGoalAreaLengthRightB(borderStripWidth + penaltyAreaLength, borderStripWidth + (fieldWidth/2 + penaltyAreaWidth/2));
    line(Ground, pointGoalAreaLengthRightA, pointGoalAreaLengthRightB, Scalar(255, 255, 255), 2, 8, 0);
    
    //-----------------GoalAreaLength (for Right & Down : RD)---------------
    Point pointRDFirst(borderStripWidth + fieldLength - penaltyAreaLength, borderStripWidth + (fieldWidth/2 - penaltyAreaWidth/2));
    Point pointRDSecond(borderStripWidth + fieldLength - penaltyAreaLength, borderStripWidth + (fieldWidth/2 + penaltyAreaWidth/2));
    line(Ground, pointRDFirst, pointRDSecond, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------GoalAreaLengthDown---------------
    Point pointGoalAreaLengthDownRA(borderStripWidth + fieldLength, borderStripWidth + (fieldWidth/2 + penaltyAreaWidth/2));
    Point pointGoalAreaLengthDownRB(borderStripWidth + fieldLength - penaltyAreaLength, borderStripWidth + (fieldWidth/2 + penaltyAreaWidth/2));
    line(Ground, pointGoalAreaLengthDownRA, pointGoalAreaLengthDownRB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------GoalAreaLengthUpRight---------------
    Point pointGoalAreaLengthUpRightA(borderStripWidth + fieldLength, borderStripWidth + (fieldWidth/2 - penaltyAreaWidth/2));
    Point pointGoalAreaLengthUpRightB(borderStripWidth + fieldLength -  penaltyAreaLength, borderStripWidth + (fieldWidth/2 - penaltyAreaWidth/2));
    line(Ground, pointGoalAreaLengthUpRightA, pointGoalAreaLengthUpRightB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------GoalDepthLeft-----------------
    Point pointGDA(borderStripWidth - goalDepth, borderStripWidth + fieldWidth/2 - goalWidth/2);
    Point pointGDB(borderStripWidth - goalDepth, borderStripWidth + fieldWidth/2 + goalWidth/2);
    line(Ground, pointGDA, pointGDB, Scalar(0, 255, 255), 2, 8, 0);

    //-----------------GoalDepthUP-----------------
    Point pointGDUA(borderStripWidth - goalDepth, borderStripWidth + fieldWidth/2 - goalWidth/2);
    Point pointGDUB(borderStripWidth, borderStripWidth + fieldWidth/2 - goalWidth/2);
    line(Ground, pointGDUA, pointGDUB, Scalar(0, 255, 255), 2, 8, 0);

    //-----------------GoalDepthDown-----------------
    Point pointGDDA(borderStripWidth - goalDepth, borderStripWidth + fieldWidth/2 + goalWidth/2);
    Point pointGDDB(borderStripWidth, borderStripWidth + fieldWidth/2 + goalWidth/2);
    line(Ground, pointGDDA, pointGDDB, Scalar(0, 255, 255), 2, 8, 0);
	
    //-----------------GoalDepthRight-----------------
    Point pointGDRA(borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth/2 - goalWidth/2);
    Point pointGDRB(borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth/2 + goalWidth/2);
    line(Ground, pointGDRA, pointGDRB, Scalar(255, 255, 0), 2, 8, 0);

    //-----------------GoalDepthUP-----------------
    Point pointGDRUA(borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth/2 - goalWidth/2);
    Point pointGDRUB(borderStripWidth + fieldLength, borderStripWidth + fieldWidth/2 - goalWidth/2);
    line(Ground, pointGDRUA, pointGDRUB, Scalar(255, 255, 0), 2, 8, 0);

    //-----------------GoalDepthDown-----------------
    Point pointGDRDA(borderStripWidth + fieldLength + goalDepth, borderStripWidth + fieldWidth/2 + goalWidth/2);
    Point pointGDRDB(borderStripWidth + fieldLength, borderStripWidth + fieldWidth/2 + goalWidth/2);
    line(Ground, pointGDRDA, pointGDRDB, Scalar(255, 255, 0), 2, 8, 0);

    //-----------------PenaltyAreaLengthUp---------------
    Point pointPenaltyAreaLengthUpAA(borderStripWidth, borderStripWidth + (fieldWidth/2 - goalAreaWidth/2));
    Point pointPenaltyAreaLengthUpBB(borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth/2 - goalAreaWidth/2));
    line(Ground, pointPenaltyAreaLengthUpAA, pointPenaltyAreaLengthUpBB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------PenaltyAreaLengthDown---------------
    Point pointPenaltyAreaLengthDownA(borderStripWidth, borderStripWidth + (fieldWidth/2 + goalAreaWidth/2));
    Point pointPenaltyAreaLengthDownB(borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth/2 + goalAreaWidth/2));
    line(Ground, pointPenaltyAreaLengthDownA, pointPenaltyAreaLengthDownB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------PenaltyAreaLengthRight---------------
    Point pointPenaltyAreaLengthRightA(borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth/2 - goalAreaWidth/2));
    Point pointPenaltyAreaLengthRightB(borderStripWidth + goalAreaLength, borderStripWidth + (fieldWidth/2 + goalAreaWidth/2));
    line(Ground, pointPenaltyAreaLengthRightA, pointPenaltyAreaLengthRightB, Scalar(255, 255, 255), 2, 8, 0);
    

    //-----------------PenaltyAreaLength (for Right & Down : RD)---------------
    Point pointPALRDFirst(borderStripWidth + fieldLength - goalAreaLength, borderStripWidth + (fieldWidth/2 - goalAreaWidth/2));
    Point pointPALRDSecond(borderStripWidth + fieldLength -goalAreaLength, borderStripWidth + (fieldWidth/2 + goalAreaWidth/2));
    line(Ground, pointPALRDFirst, pointPALRDSecond, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------PenaltyAreaLengthDown---------------
    Point pointPenaltyAreaLengthDownRA(borderStripWidth + fieldLength, borderStripWidth + (fieldWidth/2 + goalAreaWidth/2));
    Point pointPenaltyAreaLengthDownRB(borderStripWidth + fieldLength - goalAreaLength, borderStripWidth + (fieldWidth/2 + goalAreaWidth/2));
    line(Ground, pointPenaltyAreaLengthDownRA, pointPenaltyAreaLengthDownRB, Scalar(255, 255, 255), 2, 8, 0);

    //-----------------PenaltyAreaLengthUpRight---------------
    Point pointPenaltyAreaLengthUpRightA(borderStripWidth + fieldLength, borderStripWidth + (fieldWidth/2 - goalAreaWidth/2));
    Point pointPenaltyAreaLengthUpRightB(borderStripWidth + fieldLength - goalAreaLength, borderStripWidth + (fieldWidth/2 - goalAreaWidth/2));
    line(Ground, pointPenaltyAreaLengthUpRightA, pointPenaltyAreaLengthUpRightB, Scalar(255, 255, 255), 2, 8, 0);

    /*
    //----------------Robot--------------
	Point robot(borderStripWidth+fieldLength/2,borderStripWidth+fieldWidth/2);
	circle(Ground, robot, robotSize, Scalar(255, 0, 255), 2, 8, 0);

    Point pointDirectionA(borderStripWidth + fieldLength/2,borderStripWidth + fieldWidth/2);
    Point pointDirectionB(borderStripWidth + fieldLength/2 - (2*robotSize), borderStripWidth + fieldWidth/2 -(2*robotSize));
    line(Ground, pointDirectionA, pointDirectionB, Scalar(255, 0, 255), 2, 8, 0);
    */
	
    //------Check Empty & Show Finaly----
    if (Ground.empty()) 
    {
        cout << "\n Image not created. You"
                     " have done something wrong. \n";
        return -1;  
    }
    imshow("SoccerGround", Ground);
    waitKey(0);
    destroyWindow("SoccerGround");            
    return 0;
}
//---------------Humanoid robocup fild rules---------------
void initialize() {
    fieldWidth = 6 * meter2Pixel;
    fieldLength = 9 * meter2Pixel;
    goalDepth = 0.6 * meter2Pixel;
    goalWidth = 2.6 * meter2Pixel;
    goalHeight = 1.2 * meter2Pixel;
    goalAreaLength = 1 * meter2Pixel;
    goalAreaWidth = 3 * meter2Pixel;
    penaltyMarkDistance = 1.5 * meter2Pixel;
    centerCircleDiameter = 1.5 * meter2Pixel;
    borderStripWidth = 1 * meter2Pixel;
    penaltyAreaLength = 2 * meter2Pixel;
    penaltyAreaWidth = 5 * meter2Pixel;
    windowWidth = fieldWidth + 2 * borderStripWidth;
    windowLength = fieldLength + 2 * borderStripWidth;
    radius = 1.5/2 * meter2Pixel;
    penaltyRadius = 0.075 * meter2Pixel;
    robotSize = 0.27 * meter2Pixel;
    /*
    //-----------------Adult robot proportions---------------
	fieldWidth = 14 * meter2Pixel;
    fieldLength = 9 * meter2Pixel;
    goalDepth = 0.6 * meter2Pixel;
    goalWidth = 2.6 * meter2Pixel;
    goalHeight = 1.8 * meter2Pixel;
    goalAreaLength = 1 * meter2Pixel;
    goalAreaWidth = 4 * meter2Pixel;
    penaltyMarkDistance = 2.1 * meter2Pixel;
    centerCircleDiameter = 3 * meter2Pixel;
    borderStripWidth = 1 * meter2Pixel;
    penaltyAreaLength = 3 * meter2Pixel;
    penaltyAreaWidth = 6 * meter2Pixel;
    windowWidth = fieldWidth + 2 * borderStripWidth;
    windowLength = fieldLength + 2 * borderStripWidth;
    radius = 1.5/2 * meter2Pixel;
    penaltyRadius = 0.075 * meter2Pixel;
    robotSize = 0.27 * meter2Pixel;
    */
}
