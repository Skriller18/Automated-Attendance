import threading
import tkinter as tk
from tkinter import messagebox
import cv2
from deepface import DeepFace
import os

i=0
while i in range(0,68):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    usn = input("Enter your USN : ")
    usn = usn+".JPG"
    filepath = os.path.join("C:\Projects\Face_Recognition/faces",usn)
    print(filepath)

    counter = 0

    reference_img = cv2.imread(filepath)  # use your own image here

    face_match = False


    def check_face(frame):
        global face_match
        try:
            if DeepFace.verify(frame, reference_img.copy())['verified']:
                face_match = True
            else:
                face_match = False
        except ValueError:
            face_match = False


    while True:
        ret, frame = cap.read()

        if ret:
            if counter % 30 == 0:
                try:
                    threading.Thread(target=check_face, args=(frame.copy(),)).start()
                except ValueError:
                    pass
            counter += 1
            if face_match:
                cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

            cv2.imshow('video', frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()