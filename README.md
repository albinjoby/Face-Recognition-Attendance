# Face Recognition Attendance System

This project is a simple Face Recognition Attendance System using Python, OpenCV, and the `face_recognition` library. The system uses webcam input to detect faces and records attendance either in an Excel sheet or a CSV file.

## Features
- Detects faces from webcam input
- Matches faces with preloaded images stored in the `Training_images` folder
- Automatically logs attendance:
  - In a CSV file (`Attendance.csv`) for basic tracking
- Displays a live video feed with bounding boxes around recognized faces
- Prevents repeated attendance logging within a 1-minute interval for each recognized person

## Files
- `main.py`: The main script to run the face recognition system and log attendance into either an Excel file or a CSV.

- `capture.py`: The script used to capture images of new people and save them in the `Training_images` directory.

- `Attendance.csv`: File where attendance is logged (generated after running the system).

- `Training_images/`: Folder where captured images are saved.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- face_recognition library
- xlrd, xlwt, and xlutils for Excel operations
- Numpy
