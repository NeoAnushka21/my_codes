
# Human Pose Estimation

Human Pose Estimation is a  computer vision technique to track the movements of a person.



## Description
The Pose estimation is usually performed by finding the location of key points (knee, elbows, joints , etc.) 
Based on key points we can get postures and movements to draw insights as per requirements.
 Pose estimation is actively used in the field of augmented reality, animation, gaming, and robotics.

Different Available models :
1.Open pose 2.Pose net 3.Blaze pose 4. Deep Pose 5. Dense pose 6.Deep cut

Used model for project :  
Blaze pose ( Media Pipe library )


The inclusion of more key points is necessary for succeeding applications of domain-specific pose estimation models, like for hands, face, and feet. 
The model is available in two versions Blaze pose lite and Blaze pose fully to provide a balance between speed and accuracy.


Applications / Use cases :

1. Activity Recognition
Tracking the variations in the pose of a person over a period of time can also be used for activity, gesture and gait recognition .Few are listed below :
to detect if a person has fallen down or is sick.
To  autonomously teach proper workout  regimes, sport techniques and dance activities.
For understanding  full-body sign language. (Ex: Airport runway signals, traffic policemen signals, etc.).
To enhance security and surveillance.

2. Motion Capture and Augmented Reality
It is used in the field of CGI(Computer generated imagery)/Animations  for   Graphics, styles, fancy enhancements, equipment and artwork. It can be superimposed on the person if their human pose can be estimated. By tracking the variations of this human pose, the rendered graphics can “naturally fit” the person as they move.

3. Motion Tracking for Consoles
An interesting application of pose estimation is for tracking the motion of human subjects for interactive gaming. Popularly, Kinect used 3D pose estimation (using IR sensor data) to track the motion of the human players and to use it to render the actions of the virtual characters.


## How to get started 

To install the packages used inside the project , run the command below

```bash
  pip install -r requirements.txt
```

To run the basic pose estimation code
```bash
  python3 Pose_Estimation_basics.py
```

To run the code for single key point detection
```bash
  pyton3 Pose_Estimation_module.py
```
## Documentation

[Pose Estimation Docs](https://docs.google.com/document/d/1xe4Wn6NipPPexuJnKtIZ4aLhp8GBEhB0OmYVivuGW5k/edit?usp=sharing)

