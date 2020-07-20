# BDD100K-YOLOV3-tiny

Road Object detection on BDD100K using Yolov3-tiny trained on Jetson TX2. 

## Barkeley DeepDrive Dataset 

The largest open driving video dataset with 100K videos and 10 tasks to evaluate the exciting progress of image recognition algorithms on autonomous driving. Each video has 40 seconds and a high resolution. The dataset represents more than 1000 hours of driving experience with more than 100 million frames. The videos comes with GPU/IMU data for trajectory information. The dataset possesses geographic, environmental, and weather diversity, which is useful for training models that are less likely to be surprised by new conditions. The dynamic outdoor scenes and complicated ego-vehicle motion make the perception tasks even more challenging. The tasks on this dataset include image tagging, lane detection, drivable area segmentation, road object detection, semantic segmentation, instance segmentation, multi-object detection tracking, multi-object segmentation tracking, domain adaptation, and imitation learning. 

Reference from [BDD100k_Github](https://github.com/ucbdrive/bdd100k)


## Dependencies & Dataset 

This repository requires the following dependencies and dataset 
- Python3 
- [Berkeley DeepDrive Dataset](https://bdd-data.berkeley.edu/) - Download the Images and Labels (Total size bdd100k_images.zip - 6.8 GB)
- [Yolov3](https://github.com/pjreddie/darknet)


## Understanding the Dataset 

After being unzipped, all the files will reside in a folder named bdd100k. All the images will reside in bdd100k/images and labels in bdd100k/labels.  The images contains the frame at 10th second in the corresponding video.

- bdd100k/images contains three other folders called train, test and val. 
- bdd100k/labels contains two json files based on the label format for training and validation sets.  


## Steps to build 

- Download the dataset and unzip the image and labels. Make sure you have \train folder with ~70k images as well as labels with train json file. 
- Clone the Yolov3 darknet repository. 
  ```
  git clone https://github.com/pjreddie/darknet.git
  cd darknet 
  make 
  ```

