<h1 align="center">
  <br>
  <a href="https://github.com/"><img src="https://github.com/Awrsha/Robotics-3D-Quadcopter-Controller/assets/89135083/b6d22394-f8a4-453a-bf0d-8fb4049514e9" alt="QUAD" width="600"></a>
  <b><h4 align="center">.:: Tello Drone Object Following with Color Detection ::.</h4></b>
</h1>

This project demonstrates how to use a Tello drone for object following using color detection. It leverages the Tello drone's camera to detect and follow objects of a specified color. The project is implemented in Python and uses the OpenCV library for image processing.

## Prerequisites

Before running the code, you need to install the following libraries:

1. [djitellopy](https://github.com/damiafuentes/DJITelloPy): A Python library for controlling DJI Tello drones.
2. [OpenCV](https://opencv.org/): Open Source Computer Vision Library for image processing.

You should also have a DJI Tello drone with a working camera and a compatible computer to run the code.

## Usage

1. Connect the Tello drone to your computer.
2. Run the provided Python code using a Python interpreter (e.g., Anaconda, Jupyter Notebook).
3. Follow the instructions to control the Tello drone for object following.

## Code Overview

The code consists of three main parts:

1. **Tello Drone Initialization**: This section connects to the Tello drone, initializes its velocity and speed settings, and starts the video stream. It also includes logic for taking off and landing the drone.

2. **Color Detection**: In this part, color detection is performed using the drone's camera feed. You can adjust the color detection parameters (HUE, SAT, VALUE) using trackbars. The code will track and highlight objects of the specified color.

3. **Object Following**: The code tracks the detected object's position and provides control commands to the drone to follow the object. It can move left, right, up, down, or hover in place based on the object's position.

## How to Control

- Adjust the color detection parameters (HUE, SAT, VALUE) using the trackbars in the HSV window.
- The detected object is highlighted in the camera feed.
- The program detects the object's position relative to the center of the frame.
- Based on the object's position, the drone is controlled to follow the object.

## Keyboard Controls

- Press 'Q' to stop and land the drone, ending the program.

## Notes

- The code provides a basic example of object following using color detection. Further improvements and features can be added, such as obstacle avoidance and more advanced tracking algorithms.

Feel free to modify and extend the code to suit your needs or to experiment with different object tracking techniques.

## Contributing

This is an open-source project and contributions are welcome. To contribute, please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developers 👨🏻‍💻

<p align="center">
<a href="https://github.com/Awrsha"><img src="https://avatars.githubusercontent.com/u/89135083?v=4" width="100;" alt="Awrsha Parvizi"/><br /><sub><b>.:: Amir M. Parvizi ::.</b></sub></a>
</p>

## System & Hardware 🛠  
<br> <summary><b>⚙️ Things I use to get stuff done</b></summary> <ul> <li><b>OS:</b> Windows 11</li> <li><b>Laptop: </b>TUF Gaming</li> <li><b>Code Editor:</b> Visual Studio Code - The best editor out there.</li> <li><b>To Stay Updated:</b> Medium, Linkedin and Instagram.</li> <br /> ⚛️ Checkout Our VSCode Configrations <a href="">Here</a>. </ul> <p align="center">💙 If you like my projects, Give them ⭐ and Share it with friends!</p></p><p align="center"><img height="27" src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" alt="Github Stats" /></p>

<p align="center">
<img src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" alt="Github Stats" />
</p>
