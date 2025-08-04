# 📉 Financial Crisis Analysis
![status](https://img.shields.io/badge/status-passed-brightgreen)

### ✅ Project Status
This project is **functionally complete and tested**, but **open for future improvements and enhancements**.

📄 [View full analysis in Jupyter Notebook](https://github.com/CloudDataPalina/Technoprom-Financial-Analysis/blob/main/analysis.ipynb)

This project investigates the 5-year financial collapse of the fictional company **Technoprom Ltd.**  
Using Python, pandas, NumPy, and matplotlib, we analyze profitability, expenses, and debt to uncover the root causes of the crisis.

---
## 📁 Project Structure

```
Financial-Crisis-Analysis/
├── data/
│ └── financial_crisis_data.csv             ← Clean dataset (5 years of data)
├── images/
│ ├── revenue_vs_expenses.png
│ ├── expense_structure_pie.png
│ ├── margins_5y_bar.png
│ ├── top5_expenses_bar.png
│ └── profit_trend_line.png                ← All generated visualizations
├── output/
│ └── profitability_margins.csv            ← Calculated table with key financial ratios
├── src/
│ └── analysis.py                          ← Full Python script for ETL + visualizations + export
├── analysis.ipynb                         ← Jupyter version for step-by-step logic
├── requirements.txt                       ← Python dependencies
└── README.md                              ← Project documentation
```

---

## ⚙️ Skills & Tools

- `Python` : core programming language used for data analysis and scripting  
- `pandas` : data transformation, cleaning, and manipulation of tabular data  
- `NumPy` : efficient numerical operations and array-based calculations  
- `matplotlib` : visualizing data with line, bar, pie, and other chart types  
- `Jupyter Notebook` : interactive coding, data exploration, and documentation   

---

## 📊 Dataset Overview

The dataset includes:
- 📈 Revenue, Gross Profit, Net Profit  
- 💰 Cost of Goods Sold (COGS), Admin & Marketing Expenses  
- 📉 Year-End Debt, Loan Interest, Depreciation  
- 🧾 Cash Flow, Inventory, Payables  
- 👥 Employee Headcount  

Data source: [`financial_crisis_data.csv`](/data/financial_crisis_data.csv)  
*The dataset was manually created by the author for this project.*

---

## 📂 Data Preprocessing
Before starting the analysis, a technical audit of the data was performed to ensure its accuracy and suitability for use:
-  Data was loaded from a CSV file using pandas
-  Table structure, data types, missing values, and duplicates were checked
-  Numeric values were converted from int to float to improve calculation precision
-  Categorical values (indicators) were checked for uniqueness
-  Descriptive statistics revealed sharp fluctuations in profit, indicating financial instability

*All key preprocessing steps were successfully completed — the dataset is ready for full-scale analysis.*

---

## ✅ Project Goals

1. Load and explore the dataset  
2. Compute and visualize profitability over time  
3. Analyze cost structure and debt accumulation  
4. Identify turning points and causes of collapse  
5. Derive actionable business insights

---

## 📈 Visualizations

Key charts generated and saved to the [`images/`](./images) folder:

- 📊 **[5-Year Dynamics of Key Indicators](./images/technoprom_5y_change.png)** — change in revenue, profit, and costs  
- 🥧 **[Expense Structure in Year 5](./images/technoprom_expense_structure.png)** — breakdown of final-year spending  
- 🔻 **[Revenue vs. Expenses](./images/technoprom_revenue_expenses.png)** — comparison of income vs cost growth  
- 📉 **[Dynamics of Net Profit and Debt Load](./images/technoprom_netprofit_debtdynamics.png)** — illustrating deepening losses and rising liabilities  
- 📈 **[Financial Ratio Trends by Year](./images/technoprom_financial_ratio_trends.png)** — Gross, Operating, and Net margin trends

 *All plots are available in [`analysis.ipynb`](./analysis.ipynb).*

---

## 📄 Exported Results

-  Final margins table: [`profitability_margins.csv`](./output/profitability_margins.csv)  
-  All charts auto-saved to [`images/`](./images)  
-  Interactive code: [`analysis.ipynb`](./analysis.ipynb)  
-  Full automated script: [`src/analysis.py`](./src/analysis.py)

---
## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/CloudDataPalina/Financial-Crisis-Analysis.git
cd Financial-Crisis-Analysis
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run the Python script
```bash
python src/analysis.py
```
---

## 🔍 Key Findings

- Revenue declined by **38.5%** — indicating potential market share loss or shrinking demand  
- Net profit turned negative and fell nearly fourfold — confirming persistent losses  
- COGS rose despite declining revenue — signaling a drop in operational efficiency  
- Year-end debt increased **6.5×** — highlighting growing dependency on external financing  
- Admin and marketing expenses doubled — yet failed to produce revenue growth  
- All profitability margins (gross, operating, net) turned negative — confirming a deepening crisis

---

## 🧠 Key Hypotheses

- Loss of clients and contracts, decreasing demand, and growing competition  
- Poor cost control and inefficient marketing spending  
- Excessive borrowing to offset operational losses and liquidity issues

---

## 💡 Recommendations

- ✂️ **Cut overhead** — especially administrative and marketing expenses  
- 🔧 **Review COGS** — improve efficiency through supply chain audits  
- 💳 **Restructure debt** — freeze new borrowing, negotiate with creditors  
- 📌 **Focus on profitable segments** — shut down unprofitable operations  
- 📊 **Implement financial analytics** — enable data-driven decision-making

---

## 🧾 Conclusion

Technoprom Ltd. is undergoing a deep financial crisis and faces a high risk of bankruptcy if no corrective actions are taken. Only a strategic transformation — improving operational efficiency, reducing debt, and strengthening financial discipline — can stabilize the company and rebuild sustainable growth.

---

## 👩‍💻 Author

**Palina Krasiuk**  
Aspiring Cloud Data Engineer | ex-Senior Accountant  
[LinkedIn](https://www.linkedin.com/in/palina-krasiuk-954404372/) • [GitHub Portfolio](https://github.com/CloudDataPalina)
