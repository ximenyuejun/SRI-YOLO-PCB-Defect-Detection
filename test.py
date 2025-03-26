from ultralytics import YOLO

# 加载模型
model = YOLO("runs/detect/train18/weights/best.pt")  # 加载预训练模型（建议用于训练）

# 使用模型
model.val(data="datasets/PCB_DATASET_Contrast_000_0/test.yaml") 
#model.val(data="datasets/PCB_DATASET_Original/PCB_test.yaml")  # 测试模型
model.val(data="datasets/PCB_DATASET_Contrast_003_5/test.yaml")  # 测试模型
model.val(data="datasets/PCB_DATASET_Contrast_003_10/test.yaml")  # 测试模型
model.val(data="datasets/PCB_DATASET_Contrast_006_5/test.yaml")  # 测试模型
model.val(data="datasets/PCB_DATASET_Contrast_006_10/test.yaml") 
#model.val(data="datasets/PCB_DATASET_Shear_Rotate_Seg_Guass/PCB_test.yaml")  # 测试模型

