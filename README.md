# Project1---HandDetection
Hand Detection for Safety in Machine Operation

bjective: Develop a vision system to detect and prevent accidents by identifying human hands in proximity to critical machine parts.

1. System Architecture:
- Describe the overall architecture of the vision system, including hardware and software components.
- Specify how the Nvidia Jetson Nano will be utilized in the system.
  
2. Image Processing and Hand Detection:
- Outline the steps for image preprocessing and feature extraction.
- Explain how Region of Interest (ROI) can be utilized to identify critical areas in the image.
- Propose an algorithm or method to accurately detect and track human hands in real-time
  
3. AI Training and Development:
- Explain the data collection process and annotation methodology for training the hand detection model.
- Discuss the AI training pipeline, including the selection of appropriate deep learning frameworks and models.
- Outline the steps for training and fine-tuning the hand detection model using the collected dataset.
  
4. Deployment Planning:
- Describe the deployment strategy for the vision system on the Nvidia Jetson Nano.
- Discuss any considerations or optimizations required for real-time performance.
- Address any challenges or limitations that may arise during the deployment process

**Solution:-**

1. System Architecture:
   
Hardware -
a) Camera - The vision system relies on capturing image frames from a camera source. In my case, I am utilizing the built-in camera on my laptop to capture the video stream.
b) Operating System - MediaPipe and open-cv supports Windows, so I am using Windows 10
c) CPU - A modern multi-core processor with a clock speed of at least 2.0 GHz or higher.
d) RAM: At least 4 GB of RAM is typically sufficient for basic MediaPipe applications and open-cv.
e) Graphics: Since MediaPipe primarily runs on the CPU, you don't need a dedicated graphics card.

Software 
i. Python - I am using python 3.8 version
ii. open-cv - To capture and process video stream
iii. mediapipe - MediaPipe is an open-source framework developed by google for building pipelines to perform computer vision inference over arbitrary sensory data such as video or audio.

2. Image Processing and Hand Detection:
   
To develop a vision system aimed at detecting and preventing accidents, the system will identify human hands in close proximity to critical machine parts. In this setup, two rectangles will
represent the critical machine parts. If the tip of a person's index finger crosses either of these rectangles, an alert will be triggered and displayed on the screen.
The purpose of the alert is to warn the individual of the potential danger posed by their hand's position relative to the critical machine parts.
   
Steps to Capture Hand Movement in an Image and Show an Alert on Screen When the Tip of the Index Finger Crosses a Specific Region:
i. Begin by importing the necessary libraries: OpenCV for image processing and MediaPipe for hand detection.
ii. Capture the video stream using OpenCV and convert each frame to RGB format as MediaPipe requires RGB images for processing.
iii. Define the critical region on the image by creating two rectangles, marked as the red zone, using OpenCV.
![image](https://github.com/Somnath1998-hub/Project1---HandDetection/assets/83363287/f128562a-6027-4823-b20d-56bcc4bdc9d8)
iv. Initialize the hand detection object from MediaPipe and pass the video stream as input to detect and track the hand in each frame.
v. Locate the tip of the index finger in the image and save its coordinates into a list for further processing.
vi. Implement an alert mechanism to check if the tip of the index finger crosses the red zone. If detected, display an alert on the screen to indicate the event.

![image](https://github.com/Somnath1998-hub/Project1---HandDetection/assets/83363287/ff52ed09-fb18-4b83-a8a7-ffeeb073769e)

![image](https://github.com/Somnath1998-hub/Project1---HandDetection/assets/83363287/19d355a7-bb4e-4f2e-94db-1b2d3d3d3e6f)

3. AI Training and Development:
   
To detect hands in image I am using transfer leraning optimising mediapipe open-source framework. By using MediaPipe to detect hands in an image involves
leveraging a pre-trained hand detection model as a starting point.

The pre-trained model has already learned to detect hands in various scenarios, making it a strong feature extractor for hand-related patterns.
The MediaPipe Hand Landmarker task lets you detect the landmarks of the hands in an image. You can use this Task to localize key points of the hands and render visual effects over the hands.
This task operates on image data with a machine learning (ML) model as static data or a continuous stream and outputs hand landmarks in image coordinates, hand landmarks in world coordinates 
and handedness(left/right hand) of multiple detected hands.

The hand landmark model bundle detects the keypoint localization of 21 hand-knuckle coordinates within the detected hand regions. The model was trained on approximately 30K real-world images,
as well as several rendered synthetic hand models imposed over various backgrounds.
 
![image](https://github.com/Somnath1998-hub/Project1---HandDetection/assets/83363287/6f554fa6-2be0-4d68-a975-0fe361fb9ac4)

4. Deployment Planning:

To maintain the real-time performance of the application, the quality of the video stream will be a key factor. and detecting the critical region will be a challenge that may  arise during the deployment process.

