# Loan Default & Credit Risk Analysis

> **Mini-Project | Data Analytics**  
> Tools: Python · Pandas · NumPy · Matplotlib · Seaborn · Power BI

---

## Project Objective

Analyse customer loan information to identify patterns associated with loan default, transforming raw financial data into actionable credit-risk insights that support business decision-making.

---

## Folder Structure

```
StudentName_Loan_Credit_Risk_Analysis/
│
├── Dataset/
│   ├── Loan_Credit_Risk_Raw.csv          ← Raw synthetic dataset (2 005 rows)
│   └── Loan_Credit_Risk_Cleaned.csv      ← Cleaned dataset used for analysis
│
├── Python/
│   └── Loan_Credit_Risk_Analysis.ipynb   ← Full analysis notebook (Parts 1–4 + Insights)
│
├── PowerBI/
│   └── Loan_Credit_Risk_Dashboard.pbix   ← Interactive Power BI dashboard
│
├── Report/
│   └── Loan_Credit_Risk_Project_Report.pdf  ← Full project report
│
├── generate_dataset.py                   ← Script that produced the raw dataset
└── README.md                             ← This file
```

---

## Dataset Description

| Column | Description |
|---|---|
| Customer_ID | Unique customer identifier |
| Gender | Male / Female |
| Age | Customer age (21–65) |
| Education | High School / Bachelor's / Master's / PhD / Other |
| Employment_Status | Employed / Self-Employed / Unemployed / Retired |
| Marital_Status | Single / Married / Divorced / Widowed |
| Dependents | Number of dependents (0–5) |
| Annual_Income | Annual income in USD |
| Credit_Score | Credit score (300–850) |
| Existing_Loans | Number of existing active loans |
| Loan_ID | Unique loan identifier |
| Loan_Type | Personal / Home / Auto / Education / Business |
| Loan_Amount | Loan principal in USD |
| Loan_Term_Months | Loan duration in months |
| Interest_Rate | Annual interest rate (%) |
| Monthly_Installment | Computed monthly repayment amount |
| Debt_to_Income_Ratio | Monthly debt obligations / annual income |
| Employment_Years | Years in current employment |
| Previous_Defaults | Number of prior defaults |
| Credit_History | Years of credit history |
| Property_Ownership | Owned / Rented / Mortgaged / None |
| Region | North / South / East / West / Central |
| Loan_Status | Active / Defaulted |
| Default_Status | 0 = Non-Default, 1 = Default |
| Credit_Score_Group | Binned credit score category |
| Income_Group | Binned annual income category |

---

## How to Run

### Python Notebook

**Requirements**
```
pip install pandas numpy matplotlib seaborn jupyterlab
```

**Steps**
1. Open a terminal in the project root.
2. Generate the raw dataset (if not already present):
   ```bash
   python generate_dataset.py
   ```
3. Launch Jupyter:
   ```bash
   jupyter lab Python/Loan_Credit_Risk_Analysis.ipynb
   ```
4. Run all cells (`Kernel → Restart & Run All`).

The notebook will:
- Load and clean the dataset
- Perform all 44 analysis tasks
- Produce 15 visualisations
- Save `Loan_Credit_Risk_Cleaned.csv` to `Dataset/`

### Power BI Dashboard

1. Open **Power BI Desktop**.
2. Open `PowerBI/Loan_Credit_Risk_Dashboard.pbix`.
3. On first load, update the data source path to point to `Dataset/Loan_Credit_Risk_Cleaned.csv`.
4. Click **Refresh** to load data.

---

## Analysis Summary (Parts 1–4)

| Part | Content |
|---|---|
| Part 1 | Data Loading — import libraries, load CSV, inspect shape & columns |
| Part 2 | Data Cleaning — handle missing values, remove duplicates, check outliers |
| Part 3 | Data Analysis — 44 analysis tasks covering KPIs, default rates, segment analysis |
| Part 4 | Visualizations — 15 charts (pie, bar, histogram, scatter, box, heatmap) |

---

## Power BI Dashboard Components

- **KPI Cards:** Total Customers · Total Loans · Defaulted Loans · Default Rate % · Avg Loan Amount · Avg Credit Score · Avg Annual Income  
- **Charts:** Donut chart · Bar/Column charts · Histogram · Scatter chart · Table matrix  
- **Slicers:** Gender · Education · Employment Status · Loan Type · Region · Default Status · Credit Score Group  
- **DAX Measures:** COUNTROWS · DISTINCTCOUNT · CALCULATE · DIVIDE · AVERAGE

---

## Key Business Insights

1. Credit Score < 580 is the strongest predictor of default.
2. Unemployed borrowers default at nearly 2× the rate of employed borrowers.
3. Debt-to-Income Ratio > 0.40 is a reliable early warning threshold.
4. Customers with prior defaults are substantially more likely to default again.
5. Personal and Business loans carry the highest default rates (no collateral).
6. Low-income segment (<$30K) shows the highest default risk.
7. Property ownership acts as a financial stability buffer — lower default rates.
8. Higher education correlates with lower default probability.
9. Regional variation in default rates suggests portfolio mix and economic differences.
10. A multi-factor scorecard (credit score + DTI + employment + prior defaults) is recommended.

---

## Technologies Used

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Pandas | Data manipulation & analysis |
| NumPy | Numerical computing |
| Matplotlib | Static visualisations |
| Seaborn | Statistical visualisations |
| Jupyter Notebook | Interactive analysis environment |
| Power BI Desktop | Interactive dashboard |
| Power Query | ETL inside Power BI |
| DAX | Calculated measures in Power BI |

---

## Project Checklist

- [x] Dataset loaded  
- [x] Data cleaned  
- [x] Missing values handled  
- [x] Duplicate values checked and removed  
- [x] Python analysis completed (44 tasks)  
- [x] Python visualizations completed (15 charts)  
- [x] Power BI data model completed  
- [x] DAX measures created  
- [x] KPI cards created  
- [x] Charts created  
- [x] Slicers added  
- [x] Dashboard formatted  
- [x] Business insights written  
- [x] Project report completed  
- [x] Python file submitted  
- [x] Cleaned dataset submitted  
- [x] PBIX file submitted  
- [x] PDF report submitted  
- [x] README completed  
