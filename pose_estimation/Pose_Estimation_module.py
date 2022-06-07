# Importing necessary libraries

import cv2              # for image processing
import mediapipe as mp  # framework to allow us use pose estimation
import time             # Manipulation of time

# creating a class
# in which we should be able to create object
# also have methods that will allow to detect pose and find the points for us


class PoseDetector():

    # creating the initializing function
    def __init__(self, mode=False, model_complexity=1, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.model_complexity = model_complexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # for creating the model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.model_complexity, self.upBody, self.smooth,
                                     self.detectionCon, self.trackCon)

    # creating th method to find the Pose
    def find_pose(self, img, draw=True):
        """draw=TRue (is a flag) -- it will ask user if he wants to draw or not"""

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # to send converted image to the model
        self.results = self.pose.process(imgRGB)

        # for drawing the skeleton by joining the detected key points
        if self.results.pose_landmarks:
            if draw:
                # Check if the landmarks are present
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def find_position(self, img, draw=True):
        lm_list = []
        # Checking if results are available the go inside for
        if self.results.pose_landmarks:
            # Looping through each landmark
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # h- height , w- width , c- channel
                h, w, c = img.shape

                # this will print the id(keypoint (0-32)) and it's landmark for each frame
                print(id, lm)
                # storing in new variables and converting to integer as it is a pixel value
                cx, cy = int(lm.x*w), int(lm.y*h)
                lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (0, 0, 200), cv2.FILLED)
        return lm_list


def main():
    demo_vid = cv2.VideoCapture("/home/neosoft/PycharmProjects/my_codes/pose_estimation/DEmo_video/solo-dance02_ZcfTM7to.mp4")
    # Setting the initial time to zero for fps
    past_time = 0
    detector = PoseDetector()
    while True:
        success, img = demo_vid.read()
        #print("This is the printed image",img)
        img = detector.find_pose(img)

        lm_list = detector.find_position(img, draw=True)
        print(lm_list)

        # For extracting one key-point
        # if lm_list is not None:
        #     # 10 -- left mouth key point
        #     cv2.circle(img, (lm_list[10][1], lm_list[10][2]), 5, (255, 80, 120), cv2.FILLED)

        # to check the fps [Given video we have around 300fps]
        cur_time = time.time()
        fps = 1 / (cur_time - past_time)
        past_time = cur_time
        cv2.putText(img, str(int(fps)), (70, 70), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
