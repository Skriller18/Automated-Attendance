import face_recognition
import cv2
import numpy as np
from datetime import datetime
import csv
import os

video_capture = cv2.VideoCapture(0)

# Directory containing the photos
photos_directory = "G:\Projects/face/faces"  # Update this path as necessary

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []

photo_filenames = [f for f in os.listdir(photos_directory) if f.endswith(('.JPG', '.jpeg', '.png','.jpg'))]

# Loop to load each photo, get its encoding, and append to the lists
print(photo_filenames)
for filename in photo_filenames:  # Assuming filenames are 1.jpg, 2.jpg, ..., 60.jpg
    photo_path = os.path.join(photos_directory, filename)
    if os.path.exists(photo_path):
        image = face_recognition.load_image_file(photo_path)
        encoding = face_recognition.face_encodings(image)
        if encoding:
            name, _ = os.path.splitext(filename)
            known_face_encodings.append(encoding[0])
            known_face_names.append(name)  # Assign a unique name or modify as needed

students = known_face_names.copy()

np.save('encodings.npy',known_face_encodings)