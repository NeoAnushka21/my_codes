# Importing necessary libraries

# framework to allow us use pose estimation
import cv2              # for image processing
import mediapipe as mp
import time

# for creating the model
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
# demo_vid = cv2.VideoCapture(0)   # This is for accessing local cam in machine
demo_vid = cv2.VideoCapture("DEmo_video/Solo_dance_solo_dance_short_vid_(getmp3.pro).mp4")

# Setting the initial time to zero for fps
past_time = 0
# for checking the video
"""while True:
    success, img = demo_vid.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)
"""

while True:
    success, img = demo_vid.read()
    # above img is in BGR

    # Convert to RGB for being compatible with mediapipe  lib
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # to send converted image to the model
    results = pose.process(imgRGB)
    # THis wil print the result == the landmarks(coordinates)
    print(results.pose_landmarks)

    # for drawing the skeleton by joining the detected key points
    if results.pose_landmarks:
        # results.pose_landmarks -- give the detected key points
        # mpPose.POSE_CONNECTIONS -- to connect the dots
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        # Looping through each landmark
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # h- height , w- width , c- channel
            h, w, c = img.shape

            # this will print the id(keypoint (0-32)) and it's landmark for each frame
            print(id, lm)
            # storing in new variables and converting to integer as it is a pixel value
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 5, (0, 0, 200), cv2.FILLED)

    # to check the fps [Given video we have around 300fps]
    cur_time = time.time()
    fps = 1 / (cur_time-past_time)
    past_time = cur_time
    cv2.putText(img, str(int(fps)), (70, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    # cv2.waitKey(35)
    # increasing the waitKey will reduce the fps
    # but we do not need to do it as our model will do that for us
