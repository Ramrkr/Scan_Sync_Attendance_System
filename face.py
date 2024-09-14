import os
import cv2
import face_recognition
from datetime import datetime
import xlsxwriter

# Initialize known persons dictionary
known_persons = {}
known_persons_folder = {
    "Person_name1":"Person1_folder_name",
    "Person_name2":"Person2_folder_name",
    "Person_name3":"Person3_folder_name",
    "Person_name4":"Person4_folder_name",
    "Person_name5":"Person5_folder_name",
    "Person_name6":"Person6_folder_name",
    "Person_name7":"Person7_folder_name"
}
# Load known faces
for person, folder_path in known_persons_folder.items():
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        continue

    image_paths = [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.lower().endswith(".jpg")
    ]
    known_persons[person] = []
    for image_path in image_paths:
        face_encodings = face_recognition.face_encodings(
            face_recognition.load_image_file(image_path)
        )
        if face_encodings:
            known_persons[person].append(face_encodings[0])

# Initialize video capture
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not open video capture.")
    exit()

current_person = None

# Initialize Excel workbook
workbook = xlsxwriter.Workbook("output.xlsx")
worksheet = workbook.add_worksheet()
hist = []

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    for (top, right, bottom, left), face_encoding in zip(
        face_locations, face_encodings
    ):
        matched_person = None  # Initialize matched_person here to handle cases when no faces match
        for name, known_encodings in known_persons.items():
            for known_encoding in known_encodings:
                match = face_recognition.compare_faces([known_encoding], face_encoding)
                if match and match[0]:  # Check if match is not empty and the first element is True
                    matched_person = name
                    break
            if matched_person:
                break

        if matched_person:
            detection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            status = "Present"
            hist.append([matched_person, detection_time, status])
            print(f"{matched_person} present at {detection_time}")

            # Stop the camera and exit the loop after the first detection
            video_capture.release()
            cv2.destroyAllWindows()
            break

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(
            frame,
            matched_person or "Unknown",
            (left + 6, bottom - 6),
            font,
            0.5,
            (255, 255, 255),
            1,
        )

    if matched_person:
        break  # Exit the outer loop after the first detection

    cv2.imshow("Video", frame)
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()

# Write to Excel
worksheet.write(0, 0, "Matched Person")
worksheet.write(0, 1, "Detected Time")
worksheet.write(0, 2, "Status")
row = 1
col = 0
for mp, t, s in hist:
    worksheet.write(row, col, mp)
    worksheet.write(row, col + 1, t)
    worksheet.write(row, col + 2, s)
    row += 1

workbook.close()