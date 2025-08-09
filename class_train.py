from ultralytics import YOLO

# Load a model
# model = YOLO("yolov8s-cls.yaml")  # build a new model from YAML
# model = YOLO("yolo8s-cls.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolov8s-cls.yaml").load("yolov8s-cls.pt")  # build from YAML and transfer weights


# Dataset
data_path = r"/autodl-fs/data/YOLO_FER/DataSets/RAF-DB_classified"


# Train model
# results = model.train(data=data_path, epochs=100)
model.train(data=data_path,  
            imgsz=224,  
            epochs=300,  
            batch=32,  
            workers=8,  
            device='0',  
            optimizer='SGD',  
            project='runs/train',  
            )



