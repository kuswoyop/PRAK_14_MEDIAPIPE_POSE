import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mdraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgRGB)
    if hasil.pose_landmarks:
        mdraw.draw_landmarks(img,hasil.pose_landmarks,mp_pose.POSE_CONNECTIONS)
        for id,lm in enumerate(hasil.pose_landmarks.landmark):
            print(lm.x,lm.y)

            cv2.imshow("webcam",img)
            cv2.waitKey(10)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
