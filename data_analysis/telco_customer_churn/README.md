# Telco Customer Churn Analysis

This project explores the IBM Telco Customer Churn dataset to uncover the factors that drive customers to leave a telecom service.  
It forms part of my **Data Career Portfolio**.

---

## 1 · Project Goals

- **Describe** overall churn and segment-level churn rates.
- **Identify** which customer attributes are statistically linked to churn.
- **Deliver** actionable insights that can inform retention strategy.

---

## 2 · Dataset

| Item    | Details                                           |
| ------- | ------------------------------------------------- |
| Source  | IBM Sample Data – _Telco Customer Churn_ (Kaggle) |
| Rows    | 7 043 customers                                   |
| Columns | 21 (demographics, services, charges, and `Churn`) |
| Target  | `Churn` (Yes / No)                                |

CSV file: `data/Telco-Customer-Churn.csv`

---

## 3 · Notebook Guide

| Notebook                                       | Purpose                                                                                              |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **`notebooks/eda_telco_customer_churn.ipynb`** | Data loading, cleaning, EDA, interactive Plotly visuals, chi-square statistical tests, and insights. |

---

## 4 · Key Insights

| #   | Finding                                                              | Business Implication                                            |
| --- | -------------------------------------------------------------------- | --------------------------------------------------------------- |
| 1   | **Overall churn rate ≈ 26 %**                                        | Baseline for evaluating high-risk segments.                     |
| 2   | **Month-to-month contracts churn ≈ 43 %** vs two-year ≈ 3 %          | Incentivize longer-term contracts (discounts, loyalty rewards). |
| 3   | **No Tech Support → highest churn** (χ² = 825, p < 10⁻¹⁷⁹)           | Bundle or upsell affordable support plans.                      |
| 4   | **Electronic-check payers churn most**; auto-pay methods churn least | Encourage automatic payments via credits or streamlined setup.  |
| 5   | **New customers (< 12 mo) on high-price plans churn heavily**        | Focus early-life retention and onboarding for premium tiers.    |

---

## 5 · Statistical Validation

Chi-square tests confirm strong associations with churn:

| Feature         | χ²     | p-value      |
| --------------- | ------ | ------------ |
| TechSupport     | 824.93 | 7.4 × 10⁻¹⁸⁰ |
| InternetService | 728.70 | 5.8 × 10⁻¹⁵⁹ |
| PaymentMethod   | 645.43 | 1.4 × 10⁻¹³⁹ |
| StreamingTV     | 372.46 | 1.3 × 10⁻⁸¹  |
| SeniorCitizen   | 158.44 | 2.5 × 10⁻³⁶  |

---

## 6 · How to Reproduce

1. Clone the repo and navigate to this folder.
2. Install requirements (conda or pip):
   ```bash
   conda install pandas numpy matplotlib plotly seaborn scipy jupyter
   ```
