"""
Generates a synthetic Loan Credit Risk dataset and saves it as CSV.
Run this script once to produce the raw dataset used in the analysis notebook.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
N = 2000

# ── Demographics ─────────────────────────────────────────────────────────────
customer_ids = [f"CUST{str(i).zfill(5)}" for i in range(1, N + 1)]
genders       = np.random.choice(["Male", "Female"], N, p=[0.54, 0.46])
ages          = np.random.randint(21, 66, N)
educations    = np.random.choice(
    ["High School", "Bachelor's", "Master's", "PhD", "Other"],
    N, p=[0.25, 0.40, 0.20, 0.07, 0.08]
)
employment_statuses = np.random.choice(
    ["Employed", "Self-Employed", "Unemployed", "Retired"],
    N, p=[0.55, 0.20, 0.15, 0.10]
)
marital_statuses = np.random.choice(
    ["Single", "Married", "Divorced", "Widowed"],
    N, p=[0.35, 0.45, 0.15, 0.05]
)
dependents = np.random.choice([0, 1, 2, 3, 4, 5], N, p=[0.30, 0.20, 0.25, 0.15, 0.07, 0.03])

# ── Financial Profile ────────────────────────────────────────────────────────
annual_income = np.where(
    np.isin(employment_statuses, ["Unemployed", "Retired"]),
    np.random.randint(10000, 35000, N),
    np.random.randint(30000, 150000, N)
).astype(float)

credit_scores = np.clip(
    np.random.normal(650, 80, N).astype(int), 300, 850
)

existing_loans = np.random.choice([0, 1, 2, 3, 4], N, p=[0.30, 0.35, 0.20, 0.10, 0.05])
employment_years = np.where(
    np.isin(employment_statuses, ["Unemployed"]),
    0,
    np.random.randint(0, 31, N)
).astype(int)

previous_defaults = np.random.choice([0, 1, 2, 3], N, p=[0.65, 0.20, 0.10, 0.05])
credit_history    = np.random.randint(1, 25, N)   # years
property_ownership = np.random.choice(["Owned", "Rented", "Mortgaged", "None"], N, p=[0.30, 0.35, 0.25, 0.10])
regions = np.random.choice(["North", "South", "East", "West", "Central"], N, p=[0.20, 0.22, 0.20, 0.18, 0.20])

# ── Loan Details ─────────────────────────────────────────────────────────────
loan_ids   = [f"LOAN{str(i).zfill(5)}" for i in range(1, N + 1)]
loan_types = np.random.choice(
    ["Personal", "Home", "Auto", "Education", "Business"],
    N, p=[0.30, 0.25, 0.20, 0.15, 0.10]
)

loan_amount = np.where(
    loan_types == "Home",
    np.random.randint(80000, 500000, N),
    np.where(
        loan_types == "Business",
        np.random.randint(20000, 200000, N),
        np.where(
            loan_types == "Auto",
            np.random.randint(10000, 60000, N),
            np.where(
                loan_types == "Education",
                np.random.randint(5000, 80000, N),
                np.random.randint(2000, 50000, N),  # Personal
            )
        )
    )
).astype(float)

loan_term_months  = np.random.choice([12, 24, 36, 48, 60, 84, 120, 180, 240], N)
interest_rate     = np.clip(np.random.normal(10.5, 3.5, N).round(2), 4.0, 22.0)
monthly_installment = (loan_amount * (interest_rate / 100 / 12) /
                       (1 - (1 + interest_rate / 100 / 12) ** (-loan_term_months))).round(2)
debt_to_income_ratio = np.clip((monthly_installment * 12 / annual_income).round(4), 0.01, 0.99)

# ── Default Status ────────────────────────────────────────────────────────────
# Logistic-like probability based on risk factors
risk_score = (
    - 0.005 * credit_scores
    - 0.000003 * annual_income
    + 0.5 * previous_defaults
    + 0.8 * debt_to_income_ratio
    + 0.15 * (employment_statuses == "Unemployed").astype(int)
    + 0.10 * existing_loans
    + np.random.normal(0, 0.3, N)
)
default_prob = 1 / (1 + np.exp(-risk_score + 1.5))
default_status = (np.random.rand(N) < default_prob).astype(int)
loan_status    = np.where(default_status == 1, "Defaulted", "Active")

# ── Introduce a small fraction of missing values ──────────────────────────────
def inject_nulls(arr, frac=0.02):
    arr = arr.astype(object)
    idx = np.random.choice(len(arr), int(len(arr) * frac), replace=False)
    arr[idx] = np.nan
    return arr

annual_income_with_nulls = inject_nulls(annual_income.copy())
credit_scores_with_nulls = inject_nulls(credit_scores.astype(float).copy())
employment_years_with_nulls = inject_nulls(employment_years.astype(float).copy())

# ── Assemble DataFrame ────────────────────────────────────────────────────────
df = pd.DataFrame({
    "Customer_ID":          customer_ids,
    "Gender":               genders,
    "Age":                  ages,
    "Education":            educations,
    "Employment_Status":    employment_statuses,
    "Marital_Status":       marital_statuses,
    "Dependents":           dependents,
    "Annual_Income":        annual_income_with_nulls,
    "Credit_Score":         credit_scores_with_nulls,
    "Existing_Loans":       existing_loans,
    "Loan_ID":              loan_ids,
    "Loan_Type":            loan_types,
    "Loan_Amount":          loan_amount.round(2),
    "Loan_Term_Months":     loan_term_months,
    "Interest_Rate":        interest_rate,
    "Monthly_Installment":  monthly_installment,
    "Debt_to_Income_Ratio": debt_to_income_ratio,
    "Employment_Years":     employment_years_with_nulls,
    "Previous_Defaults":    previous_defaults,
    "Credit_History":       credit_history,
    "Property_Ownership":   property_ownership,
    "Region":               regions,
    "Loan_Status":          loan_status,
    "Default_Status":       default_status,
})

# Add ~5 duplicate rows
dup_rows = df.sample(5, random_state=99)
df = pd.concat([df, dup_rows], ignore_index=True)
df = df.sample(frac=1, random_state=7).reset_index(drop=True)

out_path = "StudentName_Loan_Credit_Risk_Analysis/Dataset/Loan_Credit_Risk_Raw.csv"
df.to_csv(out_path, index=False)
print(f"Dataset saved: {out_path}  |  Shape: {df.shape}")
