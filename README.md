# 🏗️ PPE Safety Monitor (Construction Safety System)

## 📌 Overview
This project presents a computer vision-based system for monitoring construction site safety using PPE detection.

The system uses a YOLOv8 model to detect workers and evaluate whether they are wearing required safety equipment such as helmets and safety vests. A rule-based logic is applied to classify scenes as **Safe ✅** or **Unsafe ❌**.

---

## 🎯 Problem Framing
Construction environments are high-risk areas where lack of PPE can lead to serious accidents. This project aims to automate safety monitoring.

### Safety Requirements:
- Workers must wear helmets  
- Workers must wear safety vests  

---

## 🧠 Tech Stack
- YOLOv8 (Ultralytics)
- Python
- Google Colab (GPU)
- Roboflow (Annotation)

---

## 📂 Dataset

### Sources
- Public PPE dataset from Kaggle  
- 57 custom images collected from Google  
- Annotated using Roboflow  

### Classes
- helmet  
- no-helmet  
- vest  
- no-vest  
- person  

### Dataset Size
| Split | Images |
|------|--------|
| Train | 3047 |
| Validation | 113 |
| Test | 108 |

📄 More details:  
➡️ `docs/dataset_documentation.md`

---

## ⚙️ Model

- Model: YOLOv8n  
- Pretrained weights used  
- Transfer learning applied  

---

## 🧪 Training Details
| Parameter | Value |
|----------|------|
| Epochs | 20 |
| Image Size | 640 |
| Batch Size | 16 |

---
![alt text](image.png)

## 📊 Evaluation Results

### 📈 Metrics
| Metric | Value |
|--------|------|
| Precision | **80.11%** |
| Recall | **75.56%** |
| mAP@50 | **78.85%** |
| mAP@50–95 | **44.09%** |

---

### 📉 Training Curve
![alt text](image-1.png)

---

### 📊 Confusion Matrix
![alt text](image-6.png)

---

## 🔍 Sample Predictions

### ❌ No Vest
![alt text](image-3.png)

### ❌ No Helmet
![alt text](image-4.png)

### ✅ Safe
![alt text](image-5.png)

---

## 🚨 Safety Rules

- Helmet must be worn  
- Vest must be worn  
- Missing PPE → violation  

📄 Full rules:  
➡️ `docs/safety_rules.md`

---

## 🧠 Safe / Unsafe Logic

### SAFE
- person + helmet + vest  

### UNSAFE
- missing helmet  
- missing vest  
- both missing  

### Note
The system uses **scene-level classification**:
> If any violation is detected, the entire image is marked unsafe.

---

## 🔍 Inference

Run:

```bash
pip install ultralytics

```

Project Structure
PPESAFETY/
├── README.md
├── data.yaml
├── requirements.txt
├── training/
│   └── PPE-Detection.ipynb
├── inference/
│   └── predict.py
├── results/
├── docs/


⚠️ Limitations
Small custom dataset
Class imbalance
Weak performance on no-helmet
Scene-level logic

🚀 Future Work
Improve dataset balance
Add more safety classes
Real-time monitoring
Web deployment