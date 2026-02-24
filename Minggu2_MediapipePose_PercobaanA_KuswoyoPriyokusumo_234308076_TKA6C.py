import cv2
import mediapipe as mp
mpose = mp.solutions.pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0)

while True:
    success, img=cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil =pose.process(imgRGB)
    if hasil.pose_landmarks:
        print("terdetaksi")
    else:
        print("tidak terdetaksi")

    cv2.imshow("webcam",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
