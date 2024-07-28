# 1st project To look whether student is there or not in class 

## Description
This project uses OpenCV to detect faces and eyes in real-time through a webcam. It also integrates with Tkinter to show a warning message if a face is not detected for more than 10 seconds. This can be useful for monitoring purposes, such as checking if someone is present in front of the camera.

## Features
- Real-time face and eye detection using Haar cascades.
- Alerts if no face is detected for more than 10 seconds.
- Easy to use and customizable.

## Requirements
- Python 3.x
- OpenCV
- Tkinter

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/face-eye-detection.git
    cd face-eye-detection
    ```

2. **Install Dependencies**
    ```bash
    pip install opencv-python-headless numpy
    ```

## Usage
1. **Run the Script**
    ```bash
    python face_eye_detection.py
    ```

2. **Quit the Application**
    - Press `q` to quit the application.

## Code Explanation
[ how it works video is here](https://drive.google.com/file/d/1IYgScPuvyAuTTDNehUAkIaRwiuaS4d_2/view?usp=drive_link )                                                         
  
  
  

### Import Libraries
The required libraries are imported at the beginning of the script.
```python
 import cv2
import time
import numpy as np
import tkinter as tk
from tkinter import messagebox  
```




# 2nd To know if student is opening other website

## Description
This project uses OpenCV and Tkinter to capture video from a webcam, display it in a GUI, and monitor the number of open browser tabs. If the number of open tabs increases, the application captures a screenshot from the webcam.

## Features
- Real-time webcam feed display.
- Automatic screenshot capture if the number of open browser tabs increases.
- Display of captured screenshots using Matplotlib.

## Requirements
- Python 3.x
- OpenCV
- Tkinter
- PIL (Pillow)
- Matplotlib

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/webcam-tab-monitor.git
    cd webcam-tab-monitor
    ```

2. **Install Dependencies**
    ```bash
    pip install opencv-python-headless pillow matplotlib numpy
    ```

## Usage
1. **Run the Script**
    ```bash
    python webcam_tab_monitor.py
    ```

2. **Quit the Application**
    - Close the GUI window.

## Code Explanation
[How it works video is here](https://drive.google.com/file/d/1orWtcHvrB5HLUeBdT7B8Zq8xMoHLEunz/view?usp=drive_link)

### Import Libraries
The required libraries are imported at the beginning of the script.
```python
import subprocess
import cv2
import time
from tkinter import Tk, Label
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
