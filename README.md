# 📉 Technoprom Ltd.: Financial Crisis Analysis (EDA Project)

📄 [View full analysis in Jupyter Notebook](https://github.com/CloudDataPalina/Technoprom-Financial-Analysis/blob/main/analysis.ipynb)

This project investigates the 5-year financial collapse of the fictional company **Technoprom Ltd.**  
Using Python, pandas, NumPy, and matplotlib, we analyze profitability, expenses, and debt to uncover the root causes of the crisis.


---

## 📁 Project Structure

```
Technoprom-Financial-Analysis/
├── techno_prom_financials.csv    ← Source dataset (5 years of annual data)
├── analysis.ipynb                ← Jupyter notebook with full EDA
└── README.md                     ← This file


```

## ⚙️ Tools & Technologies

- Python  
- pandas  
- NumPy  
- matplotlib  
- Jupyter Notebook  

---

## 📊 Dataset Overview

The dataset includes:
- 📈 Revenue, Gross Profit, Net Profit
- 💰 Cost of Goods Sold (COGS), Admin & Marketing Expenses
- 📉 Year-End Debt, Loan Interest, Depreciation
- 🧾 Cash Flow, Inventory, Payables
- 👥 Employee Headcount

Data source: [`techno_prom_financials.csv`](techno_prom_financials.csv)  
*The dataset was manually created by the author for this project.*

---

## 📂 Data Preprocessing

Before analysis, the dataset underwent a basic preprocessing stage:
- Checked for consistency and missing values
- Converted to appropriate data types
- Cleaned from duplicates and anomalies
- Formatted for further visualization and metric calculations

---

## ✅ Project Goals

1. Load and explore the dataset  
2. Compute and visualize profitability over time  
3. Analyze cost structure and debt accumulation  
4. Identify turning points and causes of collapse  
5. Derive actionable business insights

---

## 📈 Visualizations

- 📉 **Net Profit vs Year-End Debt** — declining profitability vs rising debt  
- 📊 **5-Year Change in Financial Indicators** — percent changes in key metrics  
- 📈 **Trendlines of Gross, Operating, and Net Profit Margins** — margin deterioration over time  
- 🥧 **Expense Structure in Year 5** — cost distribution in the final year  
- 🔻 **Revenue vs Operating Expenses** — visualizing when costs exceeded income  

📌 *All visualizations are included in [`analysis.ipynb`](analysis.ipynb).*

---

## 🔍 Key Findings

- 📉 Revenue declined by **38.5%** (from 520K to 320K)  
- 📈 COGS increased by **13.8%** — efficiency worsened despite falling sales  
- 🔻 Net Profit dropped from +$100K to –$290K — deep losses by Year 5  
- 💣 Year-End Debt rose from $80K to $520K — **6.5** increase  
- ❌ All profit margins turned negative in final years  
- 💸 Admin & Marketing doubled while revenue fell — inefficient cost control

---

## 💡 Recommendations

- ✂️ **Cut overhead** — reduce unnecessary admin and marketing expenses  
- 🔧 **Audit COGS** — improve supply chain and cost efficiency  
- 💳 **Restructure debt** — freeze new borrowing, focus on repayment  
- 📌 **Focus on profitable segments** — eliminate loss-making operations  
- 📈 **Adopt data-driven analytics** — implement financial dashboards and forecasting

---

## 👩‍💻 Author

**Palina Krasiuk**  
Aspiring Cloud Data Engineer | ex-Senior Accountant  
[LinkedIn](https://www.linkedin.com/in/palina-krasiuk-954404372/) • [GitHub Portfolio](https://github.com/CloudDataPalina)
