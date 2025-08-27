# 📚 1、Title: student expression recognition and analysis

This study is based on computer vision for real-time facial detection and expression recognition methods, calculating students' head up rate, expression score, and emotion category in class, in order to analyze students' classroom focus, participation, and classroom emotions. This method can serve as an important reference for classroom teaching evaluation, promote the high-quality development of classroom teaching, inject new vitality into the intelligent and precise development of education, and has broad application prospects.

# 2、Description

This study is based on computer vision for real-time facial detection and expression recognition methods, calculating students' head up rate, expression score, and emotion category in class, in order to analyze students' classroom focus, participation, and classroom emotions. This method can serve as an important reference for classroom teaching evaluation, promote the high-quality development of classroom teaching, inject new vitality into the intelligent and precise development of education, and has broad application prospects.

# 3、Dataset Information

The publicly available dataset of facial expressions used in this study was RAF-DB. The RAF-DB dataset is a real-world affective faces database. This study used a single facial expression dataset aligned with the RAF-DB dataset, which includes seven basic facial expressions: surprise, fear, disgust, happiness, sadness, anger, and neutral expressions. This dataset consists of 15339 facial expression images, divided into 12271 training sets and 3068 testing sets.
The RAF-DB Dataset is available at: http://www.whdeng.cn/RAF/model1.html

# 4、Code Information

The ultralytics folder contains YOLO model code. The dcos and docker folders contain YOLO model instructions and configuration information. The data folder contains the dataset for model training and testing.

Yolov8n-cls.pt contains the pre-trained weights for the YOLO8 classification model. yolov8-cls.yaml contains the YOLO8 classification model configuration parameters. class.train.py contains the YOLO8 classification training code.

expression_clsss_yolov8.pt contains the optimal weights obtained after training the expression classification model. detect_video_expression.py contains the code for face detection and student expression classification in classroom videos. expressions_to_3.py processes and classifies the detected faces and expression categories. percentage_stacked_bar_char.py plots the processed data into graphs for visualization.

# 5、Usage Instructions
First, download the YOLO model and the pre-trained weights for yolov8n-cls.pt. Then, create two folders, tran and test, within the data folder. Next, download the RAFDB facial expression dataset and place the expression images into the tran and test folders, respectively, according to the dataset's label categories.

# 6、Requirements

The experimental environment uses Ubuntu 18.04 operating system, pytorch architecture, and NVIDIA RTX 3090 graphics card. The specific experimental configuration is shown in Table 1.
Table 1. Experimental environment configuration
|Parameter|Configuration|
|--|--|
|CPU|20 vCPU AMD EPYC 7642 48-Core|
|GPU|NVIDIA RTX 3090(24GB)|
|System|Ubuntu18. 04|
|Language|Python3.8|
|CUDA|CUDA 11.0|
|cuDNN|cuDNN 8.0|
|Pytorch|Pytorch 1.7.1|

## Install
$ git clone https://github.com/ultralytics/ultralytics.git
$ cd ultralytics
$ pip install -r requirements.txt  
$ pip install requests  
$ pip install pyyaml  
$ pip install tqdm  

### Train
$ python class_train.py

### Detecte and classify
$ python detect_video_expression.py

### Data processing and analysis
expressions_to_3.py

student_exmotion.py

attention_and_participation.py



