# object detection and Tracking Using Yolo


img/objectdetection.gif

## What is Object Tracking in Computer Vision?

Object tracking involves an algorithm tracking the movement of a target object, and predicting the position and other relevant information about the objects in the image or video.
Object tracking is different from object detection (which many will be familiar with from the YOLO algorithm): whereas object detection is limited to a single frame or image and only works if the object of interest is present in the input image, object tracking is a technique used to predict the position of the target object, by tracking the trajectory of the object whether it is present in the image or video frame or not.

Object tracking algorithms can be categorized into different types based on both the task and the kind of inputs they are trained on. Let’s have a look at the four most common types of object tracking algorithms:

- Image tracking 
- Video tracking 
- Single object tracking 
- Multiple object tracking

## Use Cases for Object Tracking in Computer Vision:

- Surveillance
- Retail
- Autonomous Vehicles
- Healthcare

## What is YOLO?

You Only Look Once (YOLO) proposes using an end-to-end neural network that makes predictions of bounding boxes and class probabilities all at once. It differs from the approach taken by previous object detection algorithms, which repurposed classifiers to perform detection.
Following a fundamentally different approach to object detection, YOLO achieved state-of-the-art results, beating other real-time object detection algorithms by a large margin.
While algorithms like Faster RCNN work by detecting possible regions of interest using the Region Proposal Network and then performing recognition on those regions separately, YOLO performs all of its predictions with the help of a single fully connected layer.
Methods that use Region Proposal Networks perform multiple iterations for the same image, while YOLO gets away with a single iteration.
Several new versions of the same model have been proposed since the initial release of YOLO in 2015, each building on and improving its predecessor. Here's a timeline showcasing YOLO's development in recent years.


<img width="760" alt="image" src="https://github.com/Ramahalharbi/object_detection_and_Tracking/assets/139393175/1a4336e1-d0b3-429e-8e78-25ee0d6f3228">


## How does YOLO work? YOLO Architecture
The YOLO algorithm takes an image as input and then uses a simple deep convolutional neural network to detect objects in the image. The architecture of the CNN model that forms the backbone of YOLO is shown below.

<img width="760" alt="image" src="https://github.com/Ramahalharbi/object_detection_and_Tracking/assets/139393175/1d9a505d-10a4-4684-9ea5-4b50a6cc9db6">


## YOLO v4: 
for my project i use YOLO v4 algorithem.which is, YOLOv4-tiny Implemented in Tensorflow 2.0. Convert YOLO v4, YOLOv3, YOLO tiny .weights to .pb, .tflite and trt format for tensorflow, tensorflow lite, tensorRT.

<img width="665" alt="image" src="https://github.com/Ramahalharbi/object_detection_and_Tracking/assets/139393175/613460fc-3fbd-40ae-93b4-9b6927a35834">




