# Drone_Object-Detection
This repository provides data conversion codes, label map and scripts to train models for real-time object detection on the Nvidia Jetson Nano. The dataset used for Aerial Object Detection is Dota v1.0 (Horizontal Bounding Boxes). We shall also soon be providing the optimised TensorRT graph for the trained SSD Inception v2 model which can be directly used for inference.
## Requirements:
-	Nvidia Jetson Nano (4 GB) Developer Kit
-	SanDisk Extreme microSD (64 GB recommended)
-	Jetpack SDK >= 4.4.1 
-	Ubuntu >= 18.04.5 LTS
-	TensorRT >= 7.1.3 
-	CUDA and cuDNN (pre-installed with JetPack SDK)
-	Tensorflow 1.15
-	Python >= 3.6
## Steps for Training:
- For maximum performance mount the 4GB swap and set the Nano to maximum power capacity using [performance.sh](performance.sh).
-	Download the dataset from [Dota v1.0](https://captain-whu.github.io/DOTA/dataset.html).
- Using the Jetson Inference API:
  - Setup the Jetson Inference API using the [Docker Container](https://github.com/dusty-nv/jetson-inference/blob/master/docs/aux-docker.md) or from [Source](https://github.com/dusty-nv/jetson-inference/blob/master/docs/building-repo-2.md). 
  - Convert the images from png to jpg.
  - Use [DOTA_to_VOC.py](DOTA_to_VOC.py) to convert the annotations in the standard VOC format (XML files).
  - Follow along [this video](https://www.youtube.com/watch?v=2XMkPW_sIGg&list=PL5B692fm6--uQRRDTPsJDp4o0xbzkoyf8&index=13) to train your models on the dataset. You may skip the collection of dataset part as we already have the dataset in the required format.
  - Here, the model is automatically exported to ONYX format.
- Using TensorFlow Object Detection API (recommended):
  - Install the [Tensorflow Object Detection API 1](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1.md).
  -	Use DOTA_to_tfrecords.py to convert the dataset to the tfrecords format.
  -	Follow the steps given [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/using_your_own_dataset.md) to train your model on the dataset.
  -	Obtain the optimised TensorRT graph using the [trt_convert.py](trt_convert.py) script. 
## Steps for inference:
- Using the Jetson Inference API: Refer to [this video](https://www.youtube.com/watch?v=obt60r8ZeB0&list=PL5B692fm6--uQRRDTPsJDp4o0xbzkoyf8&index=12).
- Using TensorFlow Object Detection API: Use [inference_script.py](inference_script.py) to get the output dict.
  


