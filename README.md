# Thesis-DSS-

# 🎓 Where Did the Students Go?
**Leveraging Oversampling and Neural Networks to Predict University Dropouts**

This repository contains all the code, analysis, and results related to my Master's thesis in Data Science and Society at Tilburg University. The study explores how class imbalance handling techniques—specifically SMOTE and ADASYN—affect the performance of machine learning models (Random Forest, CATBOOST, and Artificial Neural Networks) in predicting whether a university student will drop out.

---

## 🔍 Objective

To determine whether class imbalance techniques (SMOTE and ADASYN) significantly improve the F1-score of university dropout prediction models. We benchmark the performance of:

- Traditional ML models (Random Forest, CATBOOST)
- Deep learning models (Artificial Neural Network)
- Variants with and without oversampling (SMOTE/ADASYN)

---

## 📦 Dataset

We use the UCI "Predict Students' Dropout and Academic Success" dataset (Realinho et al., 2022), containing 4,424 records across 36 features. The dataset includes demographic, socioeconomic, academic, and macroeconomic variables.

**Target classes**:
- Dropout
- Graduate
- Enrolled (excluded during modeling for clarity)

**Main features**:
- Demographics (age, gender, marital status, nationality)
- Socioeconomic indicators (parent education, employment, scholarships)
- Academic records (credits passed/enrolled, GPA)
- Macroeconomic data (GDP, unemployment, inflation)

---

## ⚙️ Repository Structure


---

## 🛠️ Pipeline Overview

The pipeline follows a standard ML workflow:

1. **Data Preparation**:
   - Cleaning and type casting
   - Label encoding target
   - Feature grouping (demographic, academic, socioeconomic)

2. **Exploratory Data Analysis**:
   - Visual inspection of imbalance
   - Correlation and distribution plots

3. **Model Training**:
   - Train/test split (80/20)
   - Cross-validation and grid search
   - Baseline vs. SMOTE vs. ADASYN setups

4. **Evaluation**:
   - F1-score (primary metric)
   - Confusion matrix, precision, recall
   - Statistical testing: paired t-tests, Wilcoxon signed-rank test
   - Visualizations: boxplots, ROC curves

---

## 🧠 Models Used

| Model                  | Purpose                                   |
|------------------------|-------------------------------------------|
| Random Forest          | Strong baseline, high interpretability    |
| CATBOOST               | Gradient boosting with categorical focus  |
| Artificial Neural Net  | Added model not tested in past studies    |

---

## 📊 Results Summary

Performance is assessed across baseline and oversampled configurations using stratified 5-fold cross-validation. The primary metric is F1-Score, with accuracy and ROC-AUC reported for completeness.

| Model        | Baseline F1       | SMOTE F1          | ADASYN F1         |
|--------------|-------------------|-------------------|-------------------|
| Random Forest| 0.9289 ± 0.0050   | 0.9246            | 0.9221            |
| CATBOOST     | 0.9000 (macro)    | 0.9288            | 0.9288            |
| ANN          | 0.9289 ± 0.0050   | 0.9285 ± 0.0043   | 0.8877 ± 0.0486   |

> 📌 Highlights:
> - **CATBOOST + SMOTE** had the highest dropout recall (0.993) and strong precision (0.954), making it the most balanced performer.
> - **ANN + SMOTE** maintained strong precision and stable F1, but suffered from recall drop under ADASYN.
> - **Random Forest** remained consistently strong across all configurations with minimal performance variation.

> Full metrics, plots, and confusion matrices are available in the `/results` directory.


---

## 📈 Evaluation Metrics

- F1-Score (macro & class-specific)
- Precision & Recall
- Confusion Matrix
- ROC-AUC
- Paired t-tests & non-parametric tests for significance

---

## 📋 How to Reproduce

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/thesis-dropout-prediction.git
cd thesis-dropout-prediction

2. Create virtual enviroment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Run model pipeline

python src/main.py

🧪 Statistical Testing
t-test: Compare F1-score across different sampling methods

Wilcoxon: Non-parametric confirmation

Visuals: Boxplots, violin plots

Interpretation: Included in the thesis and summary notebooks

🧾 Citation
If you use this work, please cite:

Benavides, T. (2025). Where Did the Students Go? Leveraging Oversampling and Neural Networks to Predict University Dropouts. Master’s Thesis, Tilburg University.

🧑‍🏫 Academic Info
Author: Tobias Benavides
Program: MSc Data Science & Society
University: Tilburg University
Supervisors: Dr. Samaneh Khoshrou & Prof. Dr. Gonzalo Napoles
Date: June 2025

📬 Contact
Feel free to reach out with any questions or collaboration requests:

📧 t.i.benavides@tilburguniversity.edu

📄 License
MIT License. See LICENSE for details.

yaml


