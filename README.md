## 📌 Overview
This project presents a computer vision-based solution for monitoring construction site safety. The system detects workers and evaluates whether they are wearing required Personal Protective Equipment (PPE), specifically helmets and safety vests.

The model processes images and determines whether a situation is **Safe ✅** or **Unsafe ❌** based on defined safety rules.

---

## 🎯 Objectives
- 👷 Detect workers in construction environments  
- 🪖 Identify helmet usage  
- 🦺 Detect safety vest usage  
- ⚠️ Flag safety violations  
- ✅ Classify scenes as safe or unsafe  

---

## 📂 Dataset
This project uses a **combined dataset** built from:

- 📦 Public PPE dataset from Kaggle  
- ✍️ 57 manually collected and annotated images (Google Images + Roboflow)  

### 📊 Dataset Summary
- Train images: 3047  
- Validation images: 113  
- Test images: 108  
- Total images: 3268  

### 🏷️ Classes
- helmet 🪖  
- no-helmet  
- no-vest  
- person 👷  
- vest 🦺  

📄 Full dataset details:  
➡️ [Dataset Documentation](docs/dataset_documentation.md)

---

## ⚙️ Model
- **Model Used:** YOLOv8  
- **Framework:** Ultralytics  
- **Training Environment:** Google Colab (GPU)  

---

## 🧪 Training Details
- Epochs: 50  
- Image Size: 640  
- Batch Size: 16  
- Pretrained Model: yolov8n.pt  

📄 Full training process:  
➡️ [Training Notebook](training/training_colab.ipynb)

---

## 📊 Evaluation & Results
The model was evaluated using standard object detection metrics.

### 📈 Metrics
- Precision: *(add your value if available)*  
- Recall: *(add your value if available)*  
- mAP: *(add your value if available)*  

### 📉 Training Curves
Training performance including loss curves and metrics:

![Training Results](results/results.png)

---

## 🚨 Safety Rules
The system enforces PPE compliance using the following rules:

- 🪖 Workers must wear helmets  
- 🦺 Workers must wear safety vests  
- ⚠️ Missing PPE is flagged as a violation  

📄 Full safety rules definition:  
➡️ [Safety Rules](docs/safety_rules.md)

---

## 🔍 Inference
Run detection using:

```bash
pip install ultralytics