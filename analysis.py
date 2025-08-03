# pip install pandas

# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the data from the CSV file into a DataFrame
df = pd.read_csv('data/financial_crisis_data.csv')


# Display the shape of the DataFrame (number of rows and columns)
print("Dataset shape:", df.shape)

# Show the first 5 rows to get a quick look at the structure and content
print("\nFirst 5 rows:")
print(df.head())

# Check the data types of each column
print("\nData types:")
print(df.dtypes)

# Check for missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())

print("Number of duplicate rows:", df.duplicated().sum())

# Display unique values in the 'Indicator' column
print(df['Indicator'].unique())

# Identify all columns except 'Indicator' (since it contains text)
numeric_columns = df.columns.drop('Indicator')

# Convert numeric columns to float type
df[numeric_columns] = df[numeric_columns].astype(float)

# Display the first 5 rows after type conversion
df.head()

# Print section title
print("\nDescriptive Statistics:")

# Use the describe() method to generate a statistical summary of numeric columns
print(df.describe())

# Add a column with 5-year percentage change, rounded to 1 decimal place
df['Change_5Y (%)'] = np.round(((df['Year 5'] - df['Year 1']) / df['Year 1']) * 100, 1)

# Display a table with selected columns: indicator name, values for Year 1 and Year 5, and the calculated change
df[['Indicator', 'Year 1', 'Year 5', 'Change_5Y (%)']]

# Set the size of the figure (width x height)
plt.figure(figsize=(9, 6))  

# Create a bar chart
plt.bar(df['Indicator'], df['Change_5Y (%)'], color='skyblue')  

# Add a horizontal line at 0% to separate growth and decline
plt.axhline(0, color='gray', linestyle='--') 

# Add chart title with increased font size
plt.title('Technoprom Ltd. — 5-Year Change in Key Indicators (%)', fontsize=14)

# Label for the Y-axis
plt.ylabel('Change (%)') 

# Rotate X-axis labels for better readability
plt.xticks(rotation=75)  

# Add grid for easier visual analysis
plt.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()  

# Save the chart to a file (PNG format)
plt.savefig('images/technoprom_5y_change.png')

# Display the chart
plt.show()


# Selecting key expense categories for analysis
expense_rows = [
    'COGS',                    # Cost of Goods Sold    
    'Administrative_Expenses', # Administrative Expenses
    'Marketing_PR',            # Marketing & PR
    'Depreciation',            # Depreciation
    'Loan_Interest',           # Loan Interest
    'Other_Expenses'           # Other Expenses
]

# Filter the dataset for selected expense rows and keep values for Year 1 and Year 5
expense_data = df[df['Indicator'].isin(expense_rows)][['Indicator', 'Year 1', 'Year 5']].copy()

# Extract Year 5 expense values as a NumPy array
values = expense_data['Year 5'].values                                                    # array([330, 100,  55,  40,  50,  35], dtype=int64)

# Calculate total expenses in Year 5
total = np.sum(values)                                                                    # 610

# Calculate the share of each expense category as a percentage of the total (rounded to 1 decimal)
proportions = np.round((values / total) * 100, 1)                                         # array([54.1, 16.4,  9.0,  6.6,  8.2,  5.7])

# Add a new column with the calculated shares
expense_data['Share (%)'] = proportions

# Reset the index for a cleaner table display
expense_data.reset_index(drop=True, inplace=True)

# Display the final table with expense distribution
expense_data


# Create the figure
plt.figure(figsize=(7, 7))

# Plot the pie chart
plt.pie(expense_data['Share (%)'], labels=expense_data['Indicator'], autopct='%1.1f%%', startangle=60)

# Add chart title with increased font size
plt.title('Technoprom Ltd. Expense Structure in Year 5 (%)', fontsize=14)

# Ensure the pie chart is perfectly circular
plt.axis('equal')

# Save the pie chart to a file (PNG format)
plt.savefig('images/technoprom_expense_structure.png')

# Show the chart
plt.show()

# Define an array with the names of the years
years = np.array(['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'])                  # array(['Year 1', ..., 'Year 5'], dtype='<U6')

# Extract revenue values by year
revenue = df[df['Indicator'] == 'Revenue'].iloc[0, 1:6].values                        # array([520, 470, 410, 360, 320], dtype=object)

# Extract values for expense categories: COGS, administrative, and marketing
cogs = df[df['Indicator'] == 'COGS'].iloc[0, 1:6].values                              # array([290, 300, 310, 320, 330], dtype=object)
admin = df[df['Indicator'] == 'Administrative_Expenses'].iloc[0, 1:6].values          # array([60, 70, 85, 95, 100], dtype=object)
marketing = df[df['Indicator'] == 'Marketing_PR'].iloc[0, 1:6].values                 # array([20, 30, 45, 50, 55], dtype=object)

# Sum the three categories to get total operating expenses
total_expenses = cogs + admin + marketing                                             # array([370, 400, 440, 465, 485], dtype=object)

# Create the final summary table with results by year
data = {
    'Year': ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
    'Revenue': revenue,
    'Total_Operating_Expenses': total_expenses
}
df_summary = pd.DataFrame(data)
df_summary

# Plotting the graph
plt.figure(figsize=(8, 5))  # Create a figure with specified width and height

# Revenue line
plt.plot(years, revenue, marker='o', label='Revenue', color='blue')

# Operating expenses line (COGS + Admin + Marketing)
plt.plot(years, total_expenses, marker='o', label='Operating Expenses (COGS + Admin + Marketing)', color='orange')

# Add a red marker at the year when expenses exceeded revenue (Year 3)
plt.plot('Year 3', total_expenses[2], 'ro')

# Add an annotation (label with an arrow) to this point
plt.annotate(
    'Expenses > Revenue',                          # Annotation text
    xy=('Year 3', total_expenses[2]),              # Arrow points to this coordinate
    xytext=('Year 3', total_expenses[2] + 30),     # Text position (30 units above)
    arrowprops=dict(arrowstyle='->', color='red')  # Arrow style and color
)

# Title of the chart
plt.title('Technoprom Ltd.: Revenue vs. Expenses (in $K)', fontsize=14)

# Axis labels
plt.xlabel('Fiscal Year')
plt.ylabel('Amount ($K)')

# Display the legend (line descriptions)
plt.legend()

# Add gridlines for better readability
plt.grid(True)

# Optimize layout and spacing of chart elements
plt.tight_layout()

# Save the pie chart to a file (PNG format)
plt.savefig('images/technoprom_revenue_expenses.png')

# Display the final chart
plt.show()


# Extract Net Profit values for each year
net_profit = df[df['Indicator'] == 'Net_Profit'].iloc[0, 1:6].values          # array([100.0, 5.0, -115.0, -215.0, -290.0])

# Extract Year-End Debt values
debt = df[df['Indicator'] == 'Year_End_Debt'].iloc[0, 1:6].values             # array([80.0, 150.0, 250.0, 380.0, 520.0])

# Create a summary table with results by year
data1 = {
    'Year': ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
    'Net_Profit': net_profit,
    'Year_End_Debt': debt
}
df_summary1 = pd.DataFrame(data1)
df_summary1

# Define the list of years for the X-axis
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']

# Create a figure with specified size
plt.figure(figsize=(8, 5))

# Plot Net Profit: points with 'o' marker, green color, label in the legend
plt.plot(years, net_profit, marker='o', label='Net Profit', color='green')

# Plot Year-End Debt: points with 'o' marker, red color, label in the legend
plt.plot(years, debt, marker='o', label='Year-End Debt', color='red')

# Add chart title with increased font size
plt.title('Technoprom Ltd.: Net Profit and Debt Dynamics (in $K)', fontsize=14)

# X-axis label
plt.xlabel('Fiscal Year')

# Y-axis label
plt.ylabel('Amount (in $K)')

# Add horizontal dashed line at 0 to show when values cross into negative
plt.axhline(0, color='black', linestyle='--', linewidth=1.5)

# Display the legend for the plots
plt.legend()

# Enable grid for better readability
plt.grid(True)

# Automatically adjust layout for clean display
plt.tight_layout()

# Save the pie chart to a file (PNG format)
plt.savefig('images/technoprom_netprofit_debtdynamics.png')

# Show the plot
plt.show()


# Create a dictionary-like DataFrame for easy access to rows by indicator (index by 'Indicator' column)
ind = df.set_index('Indicator')

# Extract 5-year values for key indicators

# Revenue over 5 years
revenue = ind.loc['Revenue'].iloc[:5].values                         # array([520.0, 470.0, 410.0, 360.0, 320.0])

# Gross Profit over 5 years
gross_profit = ind.loc['Gross_Profit'].iloc[:5].values               # array([230.0, 170.0, 100.0, 40.0, -10.0])

# Operating Profit = Gross Profit - Administrative Expenses - Marketing & PR
op_profit = (                                                        #array([150.0, 70.0, -30.0, -105.0, -165.0])   
    gross_profit                                                     #array([230.0, 170.0, 100.0,  40.0, -10.0])
    - ind.loc['Administrative_Expenses'].iloc[:5].values             #array([ 60.0,  70.0,  85.0,  95.0, 100.0])
    - ind.loc['Marketing_PR'].iloc[:5].values                        #array([20.0, 30.0, 45.0, 50.0, 55.0])
)

# Net Profit over 5 years 
net_profit = ind.loc['Net_Profit'].iloc[:5].values                   # array([100.0, 5.0, -115.0, -215.0, -290.0])


# Calculate profitability ratios in percentages (rounded to 1 decimal)

# Gross Profit Margin = Gross Profit / Revenue
gpm = np.round((gross_profit / revenue) * 100, 1)                   # array([44.2, 36.2, 24.4, 11.1, -3.1])

# Operating Margin = Operating Profit / Revenue
opm = np.round((op_profit / revenue) * 100, 1)                      # array([28.8, 14.9, -7.3, -29.2, -51.6])

# Net Profit Margin = Net Profit / Revenue
npm = np.round((net_profit / revenue) * 100, 1)                     # array([19.2, 1.1, -28.0, -59.7, -90.6])

# Create a summary table with results by year
margins_df = pd.DataFrame({
    'Year': [1, 2, 3, 4, 5],
    'Gross Profit Margin (%)': gpm,
    'Operating Margin (%)': opm,
    'Net Profit Margin (%)': npm
})

# Save the summary table to a CSV file
margins_df.to_csv('profitability_margins.csv', index=False)     # File: profitability_margins.csv

# Print the result to console
print(margins_df)


# Define the list of years for the X-axis
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']

# Create the figure and set the plot size
plt.figure(figsize=(8, 5))

# Plot the Gross Profit Margin line
plt.plot(years, gpm, marker='o', label='Gross Profit Margin')

# Plot the Operating Margin line
plt.plot(years, opm, marker='o', label='Operating Margin')

# Plot the Net Profit Margin line
plt.plot(years, npm, marker='o', label='Net Profit Margin')

# Add a title to the chart with increased font size
plt.title('Technoprom Ltd.: Financial Ratio Trends by Year (%)', fontsize=14)

# Label the axes
plt.xlabel('Fiscal Year')
plt.ylabel('Margin (%)')

# Add a horizontal line at 0 to separate profit from loss visually
plt.axhline(0, color='black', linestyle='--', linewidth=1.5)

# Display the legend to distinguish the lines
plt.legend()

# Enable grid for better readability
plt.grid(True)

# Automatically adjust layout for a cleaner appearance
plt.tight_layout()

# Save the pie chart to a file (PNG format)
plt.savefig('images/technoprom_financial_ratio_trends.png')

# Show the final chart
plt.show()

