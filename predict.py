from ultralytics import YOLO

Model = YOLO("yolov8n.pt") # load a pretrained model (recommended for training)
#Model.predict(source="ultralytics/assets/bus.jpg",save_txt=True, imgsz=416, save_conf=True)
results=Model.predict(source="0014/")

for r in results:
    print(r.boxes.cls)
    print(r.boxes.xyxy)  # print the Boxes object containing the detection bounding boxes
    print(r.boxes.conf)