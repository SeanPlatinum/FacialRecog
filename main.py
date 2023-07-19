import cv2
import threading
from deepface import DeepFace

emotion = 'Processing...'
def checkface(frame):
    global face_match
    global emotion
    try:
        results = DeepFace.analyze(frame, actions = ['emotion'])
        if results:
            emotion = results[0]['dominant_emotion']
        else:
            emotion = 'No face detected'
        verification = DeepFace.verify(frame, ref_image.copy())
        face_match = verification['verified']
    except Exception as e:
        face_match = False
        emotion = str(e)

videocapture = cv2.VideoCapture(0)
counter = 0
face_match = False
ref_image = cv2.imread("WIN_20230719_10_25_38_Pro.jpg")
while True:
    ret, frame = videocapture.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=checkface, args =(frame.copy(),)).start()
            except ValueError:
                pass
        counter += 1
        if face_match:
            cv2.putText(frame, "MATCH! Emotion: " + emotion, (20, 450), cv2.FONT_ITALIC, .7, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "No face detected. Emotion: " + emotion, (20, 450), cv2.FONT_ITALIC, .7, (0, 255, 0), 2)

        cv2.imshow("Facial Detection", frame)

    if cv2.waitKey(1) == ord('q'):
        break

videocapture.release()
cv2.destroyAllWindows()
