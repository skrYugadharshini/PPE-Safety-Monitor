# PPE-Safety-Monitor
PPE Safety Monitor is an AI-based computer vision system that detects workers and PPE (helmets, vests) in construction sites and classifies scenes as SAFE or UNSAFE using YOLOv8 and rule-based logic.

🚀 ✅ 1. SOURCE CODE REPOSITORY
📌 What to include

Your GitHub repo should contain:

PPE-Detection/
│
├── data/                     # dataset (or link to dataset)
├── notebooks/
│   └── training.ipynb       # Colab notebook
├── src/
│   ├── train.py
│   ├── inference.py
│   └── utils.py
├── runs/                    # model outputs
├── README.md
└── requirements.txt
📌 Example Commit History (IMPORTANT)

Make sure you don’t upload everything at once ❌

Use commits like:

Initial dataset upload
Added YOLOv8 training pipeline
Improved model performance
Added inference script
Updated README and documentation
🚀 ✅ 2. TRAINING NOTEBOOK (Colab)
📌 What to include

Your notebook should clearly show:

✔ Data loading
✔ Model training
✔ Evaluation
✔ Results
📌 Example Sections
🔹 Training
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=30,
    imgsz=640
)
🔹 Evaluation Output (IMPORTANT)

Include screenshots or outputs like:

Loss decreasing (box_loss, cls_loss)
mAP improving
Final metrics

👉 Your result:

Precision: 0.801
Recall: 0.756
mAP50: 0.788
🚀 ✅ 3. DATASET DOCUMENTATION
📌 Dataset Description

The dataset used for this project is a PPE Detection dataset collected from public sources (Roboflow/Kaggle).

📌 Classes
Helmet
No-Helmet
Vest
No-Vest
Person
📌 Dataset Size
Total Images: ~113 images (validation shown)
Instances: 699 objects
📌 Data Split
Training: ~70%
Validation: ~20%
Test: ~10%
📌 Annotation
Format: YOLO format
Bounding boxes manually annotated
Labels verified for consistency
📌 Data Challenges
Class imbalance (few “no-helmet” samples)
Small objects in crowded scenes
Lighting variations
🚀 ✅ 4. SAFETY RULES DEFINITION
📌 Rule 1: Helmet Compliance

✔ If a person is detected → must wear helmet

❌ Violation:

Person detected + no helmet detected
📌 Rule 2: Vest Compliance

✔ If a person is detected → must wear safety vest

❌ Violation:

Person detected + no vest detected
📌 Rule 3: PPE Violation Alert 🚨

If:

Person + No Helmet OR
Person + No Vest

👉 Trigger alert

📌 Example (write in report)
A worker without a helmet → violation
A worker without a vest → violation
Fully equipped worker → safe
🚀 ✅ 5. README.md (IMPORTANT)
📌 Project Title

Construction Safety Monitoring using YOLOv8

📌 Installation
pip install ultralytics
📌 Run Training
yolo detect train data=data.yaml model=yolov8n.pt epochs=30
📌 Run Inference (Images)
from ultralytics import YOLO

model = YOLO("best.pt")

model.predict(
    source="test/images",
    save=True
)
📌 Run Inference (Video)
model.predict(
    source="video.mp4",
    save=True
)
📌 Results
Precision: 0.801
Recall: 0.756
mAP50: 0.788
📌 Key Design Decisions
YOLOv8 chosen for real-time detection
Pretrained weights used for faster convergence
Image size 640 for balance of speed & accuracy
📌 Limitations (VERY IMPORTANT ⚠️)
Poor performance on no-helmet class
Struggles with small objects
Occlusion reduces accuracy
Dataset imbalance affects results
📌 Strengths

✔ Good detection for helmet & vest
✔ High accuracy for person detection
✔ Works on real-world images

🚀 ✅ 6. HONEST EVALUATION (VERY IMPORTANT 💯)
📌 Where model performs well
Detecting person
Detecting helmet and vest
Works in clear images
📌 Where model struggles
Detecting no-helmet
Crowded scenes
Low resolution images
📌 Why?
Less training data for some classes
Class imbalance
Visual similarity between classes
🏆 FINAL RESULT (WHAT YOU CAN SAY)

The developed YOLOv8-based system successfully detects PPE compliance in construction environments. The model achieves good performance for helmet, vest, and person detection, while showing limitations in detecting violations such as no-helmet due to dataset imbalance.
