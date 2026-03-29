# 🎓 Student Placement Intelligence System (SPIS)
**An Ensemble Machine Learning Approach to Career Readiness Prediction**

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange.svg)
![Status](https://img.shields.io/badge/Project-VITyarthi--BYOP-green.svg)

## 👤 Project Author
* **Lead Developer:** Mohit Pillai
* **Registration Number:** BAI11111
* **Course:** CSA2001 - Winter Semester 2025-26
* **Platform:** VITyarthi BYOP (Bring Your Own Project)

---

## 🚀 Project Overview
This project solves the problem of "Placement Uncertainty" by providing students with a data-driven prediction of their recruitment probability. Instead of relying on a single algorithm, this system implements a **Voting Classifier Ensemble** to analyze 7 critical student metrics and provide a **Confidence Score** (e.g., 94.23% Placement Probability).

### 📋 Student Profile Metrics (Input Features)
The AI evaluates the following parameters to determine placement readiness:

| Feature | Description | Range |
| :--- | :--- | :--- |
| **CGPA** | Overall academic performance | 0.0 - 10.0 |
| **Aptitude Score** | Logical and Quantitative ability | 0–100 |
| **Communication** | Soft skills and interview readiness | 1–10 |
| **Internships** | Number of industry exposures | 0–5 |
| **Projects** | Count of technical/academic projects | 1–10 |
| **Backlogs** | History of active/completed backlogs | 0–10 |
| **Technical Skills**| Proficiency in coding/domain knowledge | 1–10 |

---

## 🧠 Technical Architecture
To achieve high predictive stability, I utilized a **Soft-Voting Ensemble** combining three distinct "brains":
1. **Logistic Regression:** Analyzes linear relationships between scores and outcomes.
2. **Random Forest:** Handles complex decision-making and non-linear patterns.
3. **SVM (Support Vector Machine):** Finds the optimal boundary between "Placed" and "Not Placed" candidates.

**Key Preprocessing:** I used `StandardScaler` to normalize the data, ensuring that features with large ranges (like Aptitude) do not mathematically overpower smaller ranges (like CGPA).

---

## 📁 Repository Structure
```text
Placement-Predictor-ML/
├── data/
│   └── placement_data.csv        # Synthetic dataset (500 records)
├── notebooks/
│   └── Placement_Predictor.ipynb # Main Google Colab Notebook
├── src/
│   └── model_trainer.py          # Core ML logic script
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
