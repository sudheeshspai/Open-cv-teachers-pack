import cv2
import time
import numpy as np
import tkinter as tk
from tkinter import messagebox

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)

    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords.append([x, y, w, h])

    return coords, img

def detect(img, faceCascade, eyeCascade):
    color = {"blue": (255, 0, 0), "red": (0, 0, 255)}

    face_coords, img = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")

    face_detected = False
    if len(face_coords) > 0:
        face_detected = True
        for (x, y, w, h) in face_coords:
            roi_img = img[y:y+h, x:x+w]
            eye_coords, roi_img = draw_boundary(roi_img, eyeCascade, 1.1, 14, color['red'], "Eyes")

    return img, face_detected, face_coords

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

video_capture = cv2.VideoCapture(0)

last_face_detected_time = time.time()
face_not_detected_time = 0

while True:
    ret, img = video_capture.read()

    if not ret:
        print("Error: Unable to capture frame from video source.")
        break

    img = cv2.flip(img, 1)
    img, face_detected, coords = detect(img, faceCascade, eyeCascade)

    if face_detected:
        last_face_detected_time = time.time()
        face_not_detected_time = 0
    else:
        face_not_detected_time = time.time() - last_face_detected_time

    if face_not_detected_time > 10:
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning("Alert", "person is not there in class!")
        face_not_detected_time = 0
        last_face_detected_time = time.time()

    try:
        cv2.imshow('Video', img)
    except cv2.error as e:
        print(f"Error displaying video: {e}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
