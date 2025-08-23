# 📚 student expression recognition and analysis

This study is based on computer vision for real-time facial detection and expression recognition methods, calculating students' head up rate, expression score, and emotion category in class, in order to analyze students' classroom focus, participation, and classroom emotions. This method can serve as an important reference for classroom teaching evaluation, promote the high-quality development of classroom teaching, inject new vitality into the intelligent and precise development of education, and has broad application prospects.


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


### Install
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



