import subprocess
import cv2
import time
from tkinter import Tk, Label
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

# Threshold for the number of browser tabs
TAB_THRESHOLD = 2
CHECK_INTERVAL = 5  # Check every 5 seconds

# List of browser process names
BROWSER_PROCESSES = ["chrome", "firefox", "safari", "edge"]

class WebcamCapture:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam Capture")

        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            raise Exception("Could not access the webcam")

        self.label = Label(root)
        self.label.pack()

        self.current_frame = None  # Initialize current_frame
        self.prev_tab_count = self.count_browser_tabs()  # Initialize previous tab count

        self.update_frame()
        self.check_tabs()

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            self.current_frame = frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
        self.root.after(10, self.update_frame)

    def capture_image(self):
        if self.current_frame is not None:  # Check if current_frame is not None
            filename = f"screenshot_{self.get_timestamp()}.png"
            cv2.imwrite(filename, self.current_frame)
            print(f"Screenshot saved as {filename}")
            self.display_image(self.current_frame)

    def get_timestamp(self):
        return time.strftime("%Y%m%d-%H%M%S")

    def display_image(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()

    def check_tabs(self):
        tab_count = self.count_browser_tabs()
        print(f"Open browser tabs: {tab_count}")
        if tab_count > self.prev_tab_count:
            self.capture_image()
            self.prev_tab_count = tab_count  # Update previous tab count
        self.root.after(CHECK_INTERVAL * 1000, self.check_tabs)

    def count_browser_tabs(self):
        count = 0
        try:
            output = subprocess.check_output(['tasklist'])
            for line in output.decode('utf-8').splitlines():
                if any(proc in line for proc in BROWSER_PROCESSES):
                    count += 1
        except Exception as e:
            print(f"Error: {e}")
        return count

    def __del__(self):
        if self.video_capture is not None:  # Check if video_capture is not None
            self.video_capture.release()

if __name__ == "__main__":
    root = Tk()
    webcam_app = WebcamCapture(root)
    root.mainloop()