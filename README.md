# Regression Under Stress
``` 
How Linear, Polynomial, Ridge, and Lasso Regression behave when conditions stop being ideal
```
# Project Overview
Regression models are often introduced under clean, ideal assumptions.
In practice, data is noisy, features are correlated, and sample sizes are limited.

This project explores how common regression algorithms behave under stress, using both controlled synthetic datasets and a real-world validation on the California Housing dataset.

Rather than asking “Which model performs best?”, the focus is on why certain models succeed or fail under specific conditions.


---

## 🔹 Objectives

- Compare regression models under different stress scenarios

- Understand the impact of:

   - Noise

   - Multicollinearity

   - Small sample sizes

- Examine the role of regularization (Ridge & Lasso)

- Validate synthetic insights on real-world data

---

## 🧪 Experiments Covered

1. **Synthetic Stress Tests**
Controlled datasets were generated to isolate specific challenges:
- **Base dataset:** 500 samples, 6 numerical features, 1 target.  
- **Variants created:**  
  1. **Noisy target** – Gaussian noise added.  
  2. **Multicollinear features** – some features linearly correlated.  
  3. **Small sample regime** – downsampled to 50 rows.

> This setup allows us to clearly observe model behavior without messy real-world data.

---

## 🔹 Models & Experiments

| Model | Key Notes |
|-------|-----------|
| Linear Regression | Baseline, simple, interpretable |
| Polynomial Regression (degree=2) | Adds complexity, can overfit |
| Ridge Regression (alpha=1.0) | Regularizes coefficients, helps multicollinearity |
| Lasso Regression (alpha=0.1) | Promotes sparsity, mild regularization |

**Metrics evaluated:** RMSE and R² on test sets for all dataset variants.

---

---

2. **Real-World Validation**
**California Housing Dataset**

To test whether insights from synthetic data generalize to real-world scenarios, a final validation was performed using the California Housing dataset.

- Feature: Median Income (MedInc)

- Target: Median House Value (MedHouseVal)

- Models compared:

    - Linear Regression

    - Polynomial Regression (degree = 2)

This single-feature setup prioritizes interpretability over complexity.

Visualization (Test Set)

---

## 🔹 Key Observations

- **Linear Regression:** Handles clean and small-sample data well, fails under multicollinearity.  
- **Polynomial Regression:** Slightly overfits noisy data and worsens multicollinearity issues.  
- **Ridge Regression:** Mitigates multicollinearity, keeps coefficients stable.  
- **Lasso Regression:** Shrinks coefficients, promotes sparsity, performance similar to Ridge in this setup.  

---

## 🔹 Visual Insights

### RMSE Comparison

![RMSE Comparison](screenshots/rmse_plot.png)

### R² Comparison

![R² Comparison](screenshots/r2_plot.png)

> These plots make it clear which models are robust to which stress conditions at a glance.

---

---

📊 **Key Takeaways**

- Linear Regression remains robust under clean and real-world conditions

- Polynomial Regression improves fit but introduces overfitting risk

- Ridge Regression stabilizes performance under multicollinearity

- Lasso Regression may underperform when relationships are smooth and continuous

- Synthetic stress tests are informative — but real-world validation is essential

---

**📁 Project Structure**
```
regression-under-stress/
│
├── README.md
├── LICENSE
├── requirements.txt
├── notebooks/
│   └── 01_regression_under_stress.ipynb
├── data/
│   └── README.md
├── screenshots/
│   └── linear_vs_polynomial_test.png
└── src/
```

## 🔹 How to Run

1. Clone the repo:  
```bash
git clone https://github.com/perceptroncipher/regression-under-stress.git

2. Install dependencies:
pip install -r requirements.txt

3. Open and run the notebook:
notebooks/01_regression_under_stress.ipynb

4. Observe outputs and plots.
```


**📬 Contact**

If you want to reach out for collaboration, questions, or feedback:

Name: Adeyemi Boluwatife

Email: adeyemiboluwatife.olayinka@gmail.com

GitHub: github.com/perceptroncipher

