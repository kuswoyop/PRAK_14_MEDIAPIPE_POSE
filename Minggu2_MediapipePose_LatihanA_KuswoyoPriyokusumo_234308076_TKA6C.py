import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils
cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgRGB)

    if hasil.pose_landmarks:
        mp_draw.draw_landmarks(img,hasil.pose_landmarks,mp_pose.POSE_CONNECTIONS)

        landmarks = hasil.pose_landmarks.landmark

        shoulder_right = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        wrist_right = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

        shoulder_left = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        wrist_left = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]

        #Cek tangan kanan terangkat
        if wrist_right.y<shoulder_right.y:
            cv2.putText(img,"Tangan kanan",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

        # Cek tangan kiri terangkat
        if wrist_left.y < shoulder_left.y:
            cv2.putText(img, "Tangan kiri", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

    cv2.imshow("Deteksi Angkat Tangan",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
