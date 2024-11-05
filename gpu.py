import face_recognition
import cv2

# Load the known faces
image = face_recognition.load_image_file("faces/1RV21AI054.jpg")
face_encoding = face_recognition.face_encodings(image)[0]

# Use the GPU for face recognition
face_recognition.face_recognition_model = face_recognition.face_recognition_model.cuda()

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Detect faces in the frame
    face_locations = face_recognition.face_locations(frame)

    # Recognize faces and calculate face distance
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    face_distances = face_recognition.face_distance(face_encodings, face_encoding)

    # Loop over each face in the frame
    for (top, right, bottom, left), face_distance in zip(face_locations, face_distances):
        # If the distance to the known face is less than a certain threshold, consider it a match
        if face_distance < 1:
            # Draw a rectangle around the matched face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        else:
            # Draw a rectangle around the unmatched face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the display window
cap.release()
cv2.destroyAllWindows()