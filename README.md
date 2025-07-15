# 📉 Technoprom Financial Crisis Analysis (EDA Project)

📄 [View full analysis in Jupyter Notebook](https://github.com/CloudDataPalina/CloudDataPalina/blob/main/BankruptcyAnalysis/analysis.ipynb)


This project investigates the 5-year financial collapse of the fictional company **Technoprom Ltd.**  
Using Python, pandas, NumPy, and matplotlib, we analyze profitability, expenses, and debt to uncover the root causes of the crisis.

---

## 📁 Project Structure

```
BankruptcyAnalysis/
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

---

## ✅ Project Goals

1. Load and explore the dataset  
2. Compute and visualize profitability over time  
3. Analyze cost structure and debt accumulation  
4. Derive insights and root causes of collapse  
5. Provide actionable recommendations

---

## 📈 Visualizations

- 📉 **Net Profit vs Year-End Debt** — analysis of declining profit and rising debt  
- 📊 **5-Year Change in Financial Indicators** — percentage changes in key metrics  
- 📈 **Trendlines of Gross, Operating, and Net Profit Margins** — visualization of margin deterioration over time  
- 🥧 **Expense Structure in Year 5** — pie chart of cost distribution in the final year  
- 📉 **Revenue vs Operating Expenses** — identifying the tipping point when expenses exceeded revenue  

**Note:** The dataset was manually created by the author for the purposes of this project. 

*(All visualizations are available in `analysis.ipynb`)*


---

## 🔍 Key Findings
-  Revenue declined by 38.5% (from 520K to 320K) — indicating loss of clients or demand
-  COGS increased by 13.8% (from 290K to 330K) — despite falling sales, efficiency worsened
-  Net Profit dropped from +100K to –290K — a full reversal into deep losses
-  Year-End Debt grew from 80K to 520K — a 6.5× increase, signaling rising insolvency risk
-  Profit Margins (Gross, Operating, Net) fell sharply and all turned negative
-  Admin & Marketing Costs doubled (from 80K to 155K), while revenue dropped — showing inefficient spending

---

## 💡 Recommendations

- 🧾 **Cut unnecessary overhead** — especially administrative and marketing costs  
- ⚙️ **Audit and optimize COGS** — improve supply chain and operational efficiency  
- 💳 **Restructure debt** — avoid new borrowing until financial stabilization  
- 🎯 **Focus on profitable segments** — shut down unprofitable business lines  
- 📊 **Implement strong financial analytics** — enable data-driven decisions and forecasting

---

## 👩‍💻 Author

**Palina Krasiuk**  
Aspiring Cloud Data Engineer | ex-Senior Accountant  
[LinkedIn](https://www.linkedin.com/in/palina-krasiuk-954404372/) • [GitHub Portfolio](https://github.com/CloudDataPalina)
