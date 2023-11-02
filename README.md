# Tello Drone Object Following with Color Detection

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
