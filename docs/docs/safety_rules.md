# 🚨 Safety Rules Definition

## 1. Overview
This system is designed to monitor construction site safety by detecting workers and evaluating whether they comply with required Personal Protective Equipment (PPE) regulations.

The model analyzes images and determines whether a situation is **Safe ✅** or **Unsafe ❌** based on predefined safety rules.

---

## 2. Safety Rules

### 🔹 Rule 1: Helmet Compliance
**Definition:**  
Every worker present in the scene must wear a safety helmet.

**Safe Condition ✅:**
- Worker is detected wearing a helmet properly

**Violation ❌:**
- Worker is detected without a helmet  
- Worker labeled as `no-helmet`

**Example Violations:**
- Worker standing on site without a helmet  
- Worker carrying a helmet but not wearing it  

---

### 🔹 Rule 2: Safety Vest Compliance
**Definition:**  
Every worker must wear a high-visibility safety vest.

**Safe Condition ✅:**
- Worker is detected wearing a safety vest

**Violation ❌:**
- Worker is detected without a vest  
- Worker labeled as `no-vest`

**Example Violations:**
- Worker in active construction zone without a vest  
- Vest worn incorrectly or not visible  

---

### 🔹 Rule 3: Combined PPE Compliance
**Definition:**  
Each worker must wear both required PPE:
- Helmet  
- Safety vest  

**Safe Condition ✅:**
- Worker is wearing both helmet and vest  

**Violation ❌:**
- Missing helmet  
- Missing vest  
- Missing both  

---

## 3. Safety Decision Logic

The system determines safety using the following logic:

- If a **person is detected** AND
  - helmet is present AND
  - vest is present  
  → **SAFE ✅**

- If any required PPE is missing  
  → **UNSAFE ❌**

---

## 4. Violation Flagging

When a violation is detected, the system:

- Identifies the worker  
- Highlights bounding boxes  
- Flags the image as unsafe  
- Indicates missing PPE (helmet or vest)

---

## 5. Example Scenarios

### ✅ Safe Scenario
- Worker wearing helmet 🪖 and vest 🦺  
- Proper PPE usage  
- No violations detected  

### ❌ Unsafe Scenario 1
- Worker without helmet  
→ Violation: Helmet missing  

### ❌ Unsafe Scenario 2
- Worker without vest  
→ Violation: Vest missing  

### ❌ Unsafe Scenario 3
- Worker without both helmet and vest  
→ Violation: Multiple PPE missing  

---

## 6. Visual Examples (Proof)

Below are example outputs from the model:

### 🔹 Safe Example
![Safe Example](images/safe_example.png)

### 🔹 Helmet Violation
![No Helmet](images/no_helmet_example.png)

### 🔹 Vest Violation
![No Vest](images/no_vest_example.png)

### 🔹 Multiple Violations
![Multiple Violations](images/multiple_violation.png)

*(Images are located in the `docs/images/` folder)*

---

## 7. Limitations of Safety Rules

- The system relies on visible detection; occluded workers may not be correctly evaluated  
- PPE detection accuracy depends on image quality and lighting  
- Incorrect labeling or partial visibility may lead to false positives or false negatives  

---

## 8. Summary
The system enforces basic PPE compliance rules focused on helmet and vest usage.

These rules enable the model to:
- Detect unsafe conditions 🚨  
- Identify missing protective equipment  
- Provide clear and interpretable safety decisions  

This rule-based approach ensures that the system is simple, explainable, and effective for real-world construction safety monitoring.