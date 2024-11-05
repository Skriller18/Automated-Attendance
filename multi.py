import cv2
from deepface import DeepFace
import os
import pandas as pd

# Function to perform face recognition
def recognize_faces(test_img, reference_folder):
    # Load reference images
    reference_images = {}
    for person in os.listdir(reference_folder):
        person_folder = os.path.join(reference_folder, person)
        if os.path.isdir(person_folder):
            reference_images[person] = [os.path.join(person_folder, img) for img in os.listdir(person_folder)]

    # Initialize an empty DataFrame to store results
    df = pd.DataFrame(columns=["Person", "Distance"])

    # Perform face recognition
    for person, reference_imgs in reference_images.items():
        for ref_img_path in reference_imgs:
            result = DeepFace.verify(test_img, ref_img_path, detector_backend='opencv')
            distance = result["distance"]
            df = df.append({"Person": person, "Distance": distance}, ignore_index=True)

    # Check if there are any rows in the DataFrame
    if df.empty:
        return "Unknown", df

    # Find the person with the minimum distance
    min_distance_row = df.loc[df["Distance"].idxmin()]

    # Return the recognized person and the DataFrame with distances
    recognized_person = min_distance_row["Person"]
    return recognized_person, df

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera, change if needed

# Load OpenCV's pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using OpenCV's Cascade Classifier
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Perform face recognition on the grayscale frame
    recognized_person, distances_df = recognize_faces(gray_frame, "faces")

    # Draw the recognized person's name on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"Recognized Person: {recognized_person}", (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Webcam Feed', frame)

    # Display recognized person and distances
    print(f"Recognized Person: {recognized_person}")
    print("Distances:")
    print(distances_df)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
