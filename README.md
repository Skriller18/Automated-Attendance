# Automated-Attendance

Use the Automated Attendance System

## Steps to be followed:

Clone this Git Repository
```bash
git clone https://github.com/Skriller18/Automated-Attendance.git
```

Install the needed requirements
```bash
pip install -r requirements.txt
```

Load the images if you have into the faces folder by keeping the name of the image as the name of the label
```bash
cd faces
```

Edit the Labels file for the name of the label you want to ID for each photo
```bash
gedit labels.txt
```

Run the encoding script to get the encoding for each person
```bash
python encodings.py
```

After the encodings are generated, run the Face Recognition Script
```bash
python face_recognition.py
```

Once the program has been run and terminated, a CSV file will be generated of the attendance record with the entry timestamp.