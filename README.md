<h1 align="center">
  <br>
  <a href="https://github.com/Awrsha/RoboticSoccerPlayGround"><img src="https://s6.uupload.ir/files/hsl_0dhk.png" alt="HSL" width="200"></a>
  <br>
  Humanoid Soccer Robot 
  <br>
</h1>

<b><h4 align="center">.:: Soccer Robot Playground ::.</h4></b>

<p align="center">
<a href="https://github.com/Awrsha/RoboticSoccerPlayGround"><img src="https://img.shields.io/badge/Version-1.2.1-brightgreen" alt="HSL" width="100"></a>
<a href="https://github.com/Awrsha/RoboticSoccerPlayGround"><img src="https://img.shields.io/badge/Platform-linux--64 -blue" alt="HSL" width="130"></a>
<a href="https://github.com/Awrsha/RoboticSoccerPlayGround"><img src="https://img.shields.io/badge/Platform-windows-cyan" alt="HSL" width="130"></a>
<a href="https://github.com/Awrsha/RoboticSoccerPlayGround/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/LICENSE-MIT-red" alt="HSL" width="110"></a>
<a href="https://github.com/Awrsha/RoboticSoccerPlayGround/network/members"><img src="https://img.shields.io/badge/Developers-2-lightgrey" alt="HSL" width="100"></a>
</p>
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

## Languages  
<code>
<img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/python/python-original-wordmark.svg" width="50" height="50" /> <img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/vscode/vscode-original-wordmark.svg" width="50" height="50"/><img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/c/c-line.svg" width="50" height="50" /> <img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/numpy/numpy-original.svg" width="50" height="50"/><img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/opencv/opencv-original-wordmark.svg" width="50" height="50" /> <img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/pycharm/pycharm-original.svg" width="50" height="50"/>
</code>

## Robocup Rules
According to the [PDF](https://humanoid.robocup.org/wp-content/uploads/RCHL-2019-Roadmap-Draft1.pdf) file taken from the official RoboCup website, we have to design the competition field dynamically, that is, we should not have any problem displaying it on any screen with any resolution.
<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/8ed7bd7c-7657-4fa4-b6d9-0e581d1f2837" alt="HSL" height="350" width="700">
</h1>

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

### Installation
install necessary libraries for python with these command :

* for install **opencv** library

   ```sh
   pip install opencv-python
   ```
 * for install **numpy** library

   ```sh
   pip install numpy
   ```

### Land proportions according to RoboCup rules
Land ratios for **KidSize Robot** with **Python** programming language :
```python:
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
```
Land ratios for **AdultSize Robot** with **Python** programming language :
```python:
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
```

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

### Create a Empty Ground

Source Code : 

```python:
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
```
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

### Create a Empty Ground & Penalty Mark Distance
The coordinates of each point for this section are as follows:

<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/601b91db-b74a-4ea4-b4d1-7a0c3d07d207" alt="HSL" height="350" width="700">
</h1>

### Penalty Area Length & Width
The coordinates of each point for this section are as follows:
<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/0b1c95d6-9eff-415a-8d16-edd7fd799d13" alt="HSL" height="350" width="700">
</h1>

### Goal Area Length & Width
The coordinates of each point for this section are as follows:

<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/3a696a11-fb89-4763-aedf-a6127f83f890" alt="HSL" height="350" width="700">
</h1>

### Goal Depth & Width
The coordinates of each point for this section are as follows:

<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/d8ea31eb-a179-480e-99a5-a7b0eb769b84" alt="HSL" height="350" width="700">
</h1>

### Center Circle Diameter 
The coordinates of each point for this section are as follows:

<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/fd8b1640-253e-485b-98fa-bd4d8ac6f7ce" alt="HSL" height="350" width="700">
</h1>

### Final Shape
After all of that you should see something like this:
<h1 align="center">
  <br>
	<img src="https://github.com/Awrsha/RoboticSoccerPlayGround/assets/89135083/fdf2903d-5484-4919-9856-a14cc84bc196" alt="HSL" height="350" width="700">
</h1>

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

## Developers 👨🏻‍💻
<p align="center">
<a href="https://github.com/Awrsha"><img src="https://avatars.githubusercontent.com/u/89135083?v=4" width="100;" alt="Awrsha Parvizi"/><br /><sub><b>.:: Amir M. Parvizi ::.</b></sub></a>
</p>
<p align="center">
<a href="https://github.com/mahan1379"><img src="https://avatars.githubusercontent.com/u/91094721?v=4" width="100;" alt="Sheikh Ahmadi"/><br /><sub><b>.:: Mohammad Reza Sheikh Ahmadi ::.</b></sub></a>
</p>

## System & Hardware 🛠  
<br> <summary><b>⚙️ Things I use to get stuff done</b></summary> <ul> <li><b>OS:</b> Windows 11</li> <li><b>Laptop: </b>TUF Gaming</li> <li><b>Code Editor:</b> Visual Studio Code - The best editor out there.</li> <li><b>To Stay Updated:</b> Medium, Linkedin and Instagram.</li> <br /> ⚛️ Checkout Our VSCode Configrations <a href="">Here</a>. </ul> <p align="center">💙 If you like my projects, Give them ⭐ and Share it with friends!</p></p><p align="center"><img height="27" src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" alt="Github Stats" /></p>
