from ultralytics import YOLO

# 加载模型
modelchanged=YOLO("data/yolov8n.yaml")
#modelchanged= YOLO("runs/detect/train17/weights/best.pt")  # 从头开始构建新模型

# Train the model
modelchanged.train(data='datasets/PCB_DATASET_Shear_Rotate/PCB.yaml', epochs=300, imgsz=640)
modelchanged.val()
#modelchanged_Shear_Rotate_Seg_Guass.train(data='datasets/PCB_DATASET_Shear_Rotate_Seg_Guass/PCB.yaml', epochs=60, imgsz=640)
#modelchanged_Shear_Rotate_Seg_Guass.val()