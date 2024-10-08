# Face Recognition Attendance System

## Overview 

The Face Recognition Attendance System is an innovative project designed to automate the process of attendance tracking using advanced face recognition technology. This system leverages the power of OpenCV and the face_recognition library to detect and recognize faces in real-time from a live video feed, logging attendance with precise timestamps into an Excel file.

## Description
This project is a Face Recognition Attendance System that uses OpenCV and face_recognition libraries to detect and recognize faces from a live video feed and logs the attendance in an Excel file.

## Features
- Real-time face detection and recognition
- Logs attendance with timestamp in an Excel file
- Easy to configure with known faces

## Requirement.txt
- opencv-python
- face_recognition
- xlsxwriter
- cmake
- dlib


## Dependencies
- opencv-python
- face_recognition
- xlsxwriter

## Installation
To run this project, you need to have Python installed on your system. Follow the steps below to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/Ramrkr/Scan_Sync_Attendance_System.git
    cd face-recognition-attendance-system
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Prepare the known faces:
    - Create folders for each known person inside the project directory.
    - Add images of each person in their respective folders.

## Usage
Run the following command to start the face recognition attendance system:
```bash
python main.py

Project Structure
face-recognition-attendance-system/
│
├── Person1_folder_name/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── Person2_folder_name/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── main.py
├── requirements.txt
└── output.xlsx

Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
face_recognition
OpenCV
xlsxwriter

### 4. Additional Files
- **LICENSE**: Choose a license for your project (e.g., MIT License).
- **.gitignore**: Include common Python ignores like `__pycache__/`, `.vscode/`, `*.pyc`, etc.

### 5. Setting Up the Repository
1. **Create a new repository** on GitHub.
2. **Add a README file** using the template above.
3. **Push your code** to the repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git remote add origin https://github.com/your-username/face-recognition-attendance-system.git
    git push -u origin master
    ```
