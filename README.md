# Emotion Detector with Face Verification
This program captures the user's face through the webcam, detects the primary emotion of the face, and responds with a relevant message using speech synthesis. Additionally, the program offers face verification functionality to check if the current face matches a reference face.
## Core Competencies:
* Understand how neural networks are made
* Using packages to help simplify the problem
* use a database
## Requirements:
* OpenCV (cv2)
* threading
* deepface for emotion analysis and face verification
* tkinter for the GUI
* PIL (from Pillow) for image processing
* pyttsx3 for text-to-speech conversion
* A webcam

## Features:
Emotion Detection: Captures the emotion of the face and categorizes it into emotions such as 'happy', 'sad', 'fear', 'disgust', 'surprise', 'angry', and 'neutral'.
Face Verification: Verifies whether the current face matches a previously captured reference face.
GUI: Uses tkinter to display a live feed and provide an option to start emotion detection and face verification.
Text-to-Speech: Responds to detected emotion with a relevant message using speech synthesis.

## How to Run:
Ensure you have all the required libraries installed.
Run the script. A GUI window will appear.
Click on the "START" button. The program will then capture a reference image of your face.
The program will continuously detect emotion on the captured face and check if the face matches the reference image.
### Future Improvements:
 Improve face verification accuracy.
 Integrate with other applications for better user experience.
