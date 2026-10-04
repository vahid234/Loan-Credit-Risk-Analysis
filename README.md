# Customer Churn Analysis — Mini Project

> A complete end-to-end data analytics project analysing customer churn patterns in a telecommunications company using Python and Power BI.

---

## 📁 Project Structure

```
StudentName_Customer_Churn_Analysis/
│
├── Dataset/
│   ├── Customer_Churn_Raw.csv          ← Original raw dataset (7043 records)
│   └── Customer_Churn_Cleaned.csv      ← Cleaned dataset (exported by notebook)
│
├── Python/
│   └── Customer_Churn_Analysis.ipynb   ← Full analysis notebook (Parts 1–5)
│
├── PowerBI/
│   └── Customer_Churn_Dashboard.pbix   ← Interactive Power BI dashboard
│
├── Report/
│   └── Customer_Churn_Project_Report.pdf
│
└── README.md
```

---

## 🎯 Project Objective

Analyse customer behaviour in a telecom subscription company to understand:
- Why customers leave (churn)
- Which segments are most at risk
- What factors are most strongly associated with churn

---

## 🛠️ Tools & Technologies

| Tool            | Purpose                              |
|-----------------|--------------------------------------|
| Python 3.10+    | Core analysis language               |
| Pandas          | Data loading, cleaning, analysis     |
| NumPy           | Numerical computations               |
| Matplotlib      | Base visualisations                  |
| Seaborn         | Statistical visualisations           |
| Jupyter Notebook| Interactive analysis environment     |
| Power BI Desktop| Interactive dashboard                |
| Power Query     | Data transformation in Power BI      |
| DAX             | Calculated measures in Power BI      |

---

## 📊 Dataset Information

| Column              | Description                                |
|---------------------|--------------------------------------------|
| Customer_ID         | Unique customer identifier                 |
| Gender              | Male / Female                              |
| Senior_Citizen      | 1 = Senior, 0 = Non-Senior                 |
| Partner             | Has a partner (Yes/No)                     |
| Dependents          | Has dependents (Yes/No)                    |
| Tenure_Months       | Months with the company (1–72)             |
| Phone_Service       | Has phone service (Yes/No)                 |
| Multiple_Lines      | Has multiple lines                         |
| Internet_Service    | DSL / Fiber optic / No                     |
| Online_Security     | Online security add-on (Yes/No)            |
| Online_Backup       | Online backup add-on (Yes/No)              |
| Device_Protection   | Device protection add-on (Yes/No)          |
| Tech_Support        | Tech support add-on (Yes/No)               |
| Streaming_TV        | Streaming TV add-on (Yes/No)               |
| Streaming_Movies    | Streaming movies add-on (Yes/No)           |
| Contract            | Month-to-month / One year / Two year       |
| Paperless_Billing   | Paperless billing (Yes/No)                 |
| Payment_Method      | Electronic check / Mailed check / etc.     |
| Monthly_Charges     | Current monthly charge ($)                 |
| Total_Charges       | Total charges to date ($)                  |
| Churn               | Churned? (Yes/No) — **Target variable**    |

---

## ⚙️ How to Run the Notebook

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Run

```bash
cd StudentName_Customer_Churn_Analysis/Python
jupyter notebook Customer_Churn_Analysis.ipynb
```

Or open in **VS Code** with the Jupyter extension, or upload to **Google Colab**.

> The notebook automatically reads `../Dataset/Customer_Churn_Raw.csv` and writes `../Dataset/Customer_Churn_Cleaned.csv`.

---

## 📈 Notebook Contents

| Part | Steps | Description                              |
|------|-------|------------------------------------------|
| 1    | 1–6   | Data Loading                             |
| 2    | 7–16  | Data Exploration & Cleaning              |
| 3    | 17–38 | Data Analysis (KPIs + Segment Analysis)  |
| 4    | VIZ 1–14 | Python Visualisations                |
| 5    | —     | Business Insights                        |

### Visualisations Produced

1. Churn Distribution — Pie Chart  
2. Customer Distribution by Contract — Bar Chart  
3. Churn by Contract — Grouped Bar Chart  
4. Churn by Gender — Bar Chart  
5. Churn by Internet Service — Bar Chart  
6. Churn by Payment Method — Bar Chart  
7. Tenure Distribution — Histogram  
8. Monthly Charges Distribution — Histogram  
9. Tenure vs Monthly Charges — Scatter Plot  
10. Monthly Charges by Churn — Box Plot  
11. Total Charges by Churn — Box Plot  
12. Churn Rate by Tenure Group — Bar Chart  
13. Service Usage vs Churn — Count Plots  
14. Feature Correlation — Heatmap  

---

## 📊 Power BI Dashboard

**Title:** Customer Churn & Retention Analytics Dashboard

### KPI Cards
- Total Customers · Churned Customers · Retained Customers  
- Churn Rate % · Average Monthly Charges · Average Tenure

### Required Visuals
Donut chart (Churn distribution), Bar charts (by Contract, Internet, Payment),  
Column chart (Tenure groups), Box/Column visual (Monthly Charges),  
Scatter chart (Tenure vs Monthly Charges), Table (Customer Details)

### Slicers
Gender · Contract · Internet Service · Payment Method · Senior Citizen · Churn

### DAX Measures

```dax
Total Customers =
COUNTROWS('Customer_Churn_Cleaned')

Churned Customers =
CALCULATE(
    COUNTROWS('Customer_Churn_Cleaned'),
    'Customer_Churn_Cleaned'[Churn] = "Yes"
)

Retained Customers =
CALCULATE(
    COUNTROWS('Customer_Churn_Cleaned'),
    'Customer_Churn_Cleaned'[Churn] = "No"
)

Churn Rate % =
DIVIDE([Churned Customers], [Total Customers], 0) * 100

Average Monthly Charges =
AVERAGE('Customer_Churn_Cleaned'[Monthly_Charges])

Average Tenure =
AVERAGE('Customer_Churn_Cleaned'[Tenure_Months])
```

---

## 💡 Key Business Insights

1. **~34% overall churn rate** — significantly above the 15–20% industry average.  
2. **Month-to-month customers** churn at ~3× the rate of two-year contract holders.  
3. **Fiber optic internet customers** show the highest churn — value perception mismatch.  
4. **Electronic check payers** churn significantly more than automatic payment users.  
5. **First 12 months are critical** — new customers are most vulnerable to churning.  
6. **Churned customers pay $15–20 more per month** — price sensitivity is a key driver.  
7. **Senior citizens** churn more — targeted support programs needed.  
8. **Customers without add-ons** (security, tech support) churn more — bundling helps.  
9. **Long-tenure customers (>48 months)** have <10% churn — loyalty should be rewarded.  
10. **The 0–24 month window** is the highest-risk period — proactive retention is essential.  

---

## ✅ Project Checklist

- [x] Data cleaned and missing values handled  
- [x] Python analysis completed (38 steps)  
- [x] Python visualisations completed (14 charts)  
- [x] DAX measures created (6 measures)  
- [x] Power BI dashboard completed  
- [x] Slicers added  
- [x] Business insights written (10 insights)  
- [x] Cleaned dataset exported  
- [x] Notebook submitted  
- [x] README completed  

---

## 👤 Author

**Student Name**  
Data Analytics Mini Project  
