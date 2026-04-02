# 🏗️ Construction Safety Monitor (PPE Detection System)

---

# 📌 OVERVIEW
This project presents a computer vision-based system for monitoring construction site safety using PPE (Personal Protective Equipment) detection.

The system detects workers and evaluates whether they are wearing:
- 🪖 Helmets  
- 🦺 Safety vests  

It classifies situations as:
- **Safe ✅**
- **Unsafe ❌**

---

# 🎯 OBJECTIVES
- Detect workers in construction environments  
- Identify helmet usage  
- Detect safety vest usage  
- Flag safety violations  
- Classify scenes as safe or unsafe  

---

# 🧠 TECH STACK
- YOLOv8 (Ultralytics)  
- Python  
- Google Colab (GPU)  
- Roboflow (Annotation)  
- OpenCV / Matplotlib  

---

# 📂 DATASET

## Overview
This project uses a combined dataset created from:
- 📦 Kaggle PPE dataset  
- ✍️ 57 manually collected images (Google + Roboflow)

---

## Classes
- helmet 🪖  
- no-helmet  
- no-vest  
- person 👷  
- vest 🦺  

---

## Dataset Size

### Kaggle Dataset
- Train: 3006  
- Validation: 102  
- Test: 102  

### Custom Dataset
- Train: 41  
- Validation: 11  
- Test: 6  

### Final Combined Dataset
- Train: 3047  
- Validation: 113  
- Test: 108  
- Total: 3268  

---

## Data Collection Process
- Downloaded dataset from Kaggle  
- Collected additional images from Google  
- Manually annotated using Roboflow  
- Used same class labels for consistency  

---

## Annotation
- Tool: Roboflow  
- Type: Bounding box  
- Custom labeled images: 57  

---

## Dataset Merging
- Combined both datasets (train, valid, test)  
- Maintained YOLO format  
- No relabeling required  

---

## Limitations
- Small custom dataset  
- Image quality varies  
- Class imbalance  

---

# ⚙️ MODEL

- Model: YOLOv8  
- Pretrained: yolov8n.pt  
- Training: Google Colab GPU  

---

# 🧪 TRAINING DETAILS
- Epochs: 50  
- Image Size: 640  
- Batch Size: 16  

---

# 📊 RESULTS

## Metrics
- Precision: (add if available)  
- Recall: (add if available)  
- mAP: (add if available)  

## Training Curves
Add this image:

results/results.png


---

# 🚨 SAFETY RULES

## Rule 1: Helmet
Workers must wear helmets.

❌ Violation:
- no-helmet detected  

---

## Rule 2: Safety Vest
Workers must wear vests.

❌ Violation:
- no-vest detected  

---

## Rule 3: Full PPE Compliance
Workers must wear BOTH:
- helmet  
- vest  

❌ Violation:
- missing one or both  

---

## Decision Logic

IF:
- person detected  
- helmet detected  
- vest detected  

→ SAFE ✅  

ELSE  
→ UNSAFE ❌  

---

# 🔍 INFERENCE

Install:

```bash
pip install ultralytics

Run:

python inference/predict.py

📁 PROJECT STRUCTURE

construction-safety-monitor/
├── README.md
├── requirements.txt
├── data.yaml
├── training/
│   └── training_colab.ipynb
├── inference/
│   └── predict.py
├── results/
│   └── results.png
├── docs/
│   └── images/

⚙️ HOW IT WORKS

Input image/video
YOLO detects objects
PPE checked
Rules applied
Output: Safe / Unsafe

⚠️ LIMITATIONS
Small custom dataset
Lighting sensitivity
Occlusion issues

🚀 FUTURE IMPROVEMENTS
Real-time detection
Larger dataset
More safety rules
Web deployment
👩‍💻 AUTHOR

Yugadharshini

📌 SUMMARY

This project demonstrates:

Dataset creation & annotation
Model training (YOLOv8)
PPE detection
Safety rule implementation

A complete pipeline for construction safety monitoring.


---

# 🎯 HOW TO USE THIS

## Option 1 (BEST)
Split into:

- README.md → main part  
- dataset_documentation.md → dataset section  
- safety_rules.md → rules  
