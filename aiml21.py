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

with open('string_array.txt', 'w') as file:
    for item in known_face_names:
        file.write(f"{item}\n")

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

classname = input("Enter the course code: ")

with open(f"{classname}_{current_date}_Attendance.csv", 'w+', newline="") as f:
    lnwriter = csv.writer(f)
    lnwriter.writerow(["USN", "Time entered"])

    while True:
        ret, frame = video_capture.read()

        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)
                if name in known_face_names:
                    if name in students:
                        students.remove(name)
                        print(students)
                        current_time = now.strftime("%H-%M-%S")
                        lnwriter.writerow([name, current_time])

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
