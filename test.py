from ultralytics import YOLO

# Load model
model = YOLO("model/original+noCBAM+CIoU.pt") 

# Inference
model.val(data="datasets/PCB_DATASET_Contrast_000_0/test.yaml")  
# model.val(data="datasets/PCB_DATASET_Contrast_003_5/test.yaml")  
# model.val(data="datasets/PCB_DATASET_Contrast_003_10/test.yaml") 
# model.val(data="datasets/PCB_DATASET_Contrast_006_5/test.yaml")  
# model.val(data="datasets/PCB_DATASET_Contrast_006_10/test.yaml")

