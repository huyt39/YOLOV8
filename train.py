from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")

# Train the model
train_results = model.train(
    data="config.yaml",  # path to dataset YAML
    epochs=100,  # number of training epochs
    device="cpu",  # device to run on, i.e. device=0 or device=0,1,2,3 or device=cpu
)

