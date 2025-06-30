from ultralytics import YOLO

# Load model
modelchanged=YOLO("data/yolov8.yaml")
#modelchanged= YOLO("runs/detect/train17/weights/best.pt")  # Train a new model from scratch

# Train the model
modelchanged.train(data='datasets/PCB_DATASET_Shear_Rotate/PCB.yaml', epochs=300, imgsz=640)
modelchanged.val()
#modelchanged_Shear_Rotate_Seg_Guass.train(data='datasets/PCB_DATASET_Shear_Rotate_Seg_Guass/PCB.yaml', epochs=60, imgsz=640)
#modelchanged_Shear_Rotate_Seg_Guass.val()
