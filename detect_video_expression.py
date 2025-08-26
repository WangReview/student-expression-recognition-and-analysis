# Video face detect and expression recognition

from ultralytics import YOLO
import cv2
import numpy as np

face_model_path = '/autodl-fs/data/YOLO_FER/yolov8-face-main/yolov8n-face.pt'  
# expression_model_path = r'/autodl-fs/data/YOLO_FER/yolov8-face-main/expression_class_yolov8.pt'  
expression_model_path = r'/autodl-fs/data/YOLO_FER/ultralytics-main/runs/train/train2/weights/best.pt'  # expression

# face detect
face_model = YOLO(face_model_path, task='detect')   
# expression recognition
expression_model = YOLO(expression_model_path)


# video_path
# video_path = '/autodl-fs/data/YOLO_FER/yolov8-face-main/data/3.mp4'
video_path = '/autodl-fs/data/YOLO_FER/yolov8-face-main/data/datatest/testvideo2.mp4'
output_path = 'output_testvideo2.mp4'

# VideoCapture
cap = cv2.VideoCapture(video_path)


fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 


    results = face_model(frame)    # detect face 
    res = results[0].boxes.xyxy.tolist()   # multi face
    roi_color = []
    # multi face
    for each in res:
            x1,y1,x2,y2 = each[:4]
            x1 = int(x1)    # left
            y1 = int(y1)    # top
            x2 = int(x2)    # right
            y2 = int(y2)    # down

            roi_color = frame[y1:y2,x1:x2]
            results = expression_model.predict(roi_color)

            pred = results[0]
            # Top-1
            top1_label = pred.names[pred.probs.top1]  #  ml-citation{ref="1,8" data="citationList"}
            top1_conf = pred.probs.top1conf.item()  # 
            conf1 = "{:.2g}".format(top1_conf)  
          
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0, 255, 0), 1)
            cv2.putText(frame, top1_label, ((x1, y1 +20)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 250),1, cv2.LINE_AA)


    out.write(frame)

print('OK')
