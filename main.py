import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# Loading data from the Excel sheets 
file_path = './Dummy.xlsx'
data = pd.read_excel(file_path)
# print(type(data['Amount'][0]))
data['Date'] = pd.to_datetime(data['Date'])
x = data['Category']
y = data['Amount']

# # Sorting the data from dates
if not data['Date'].is_monotonic_increasing:  
    print('Sorting.....')
    data.sort_values(by='Date', inplace=True)
else:
    print('Dates are already in correct order')

# Spending for current month
currentMonth = datetime.now().strftime('%B')
Spent_Amount = 0
for index, row in data.iterrows():
    if row['Month'] == currentMonth and row['Status'] == 'Expense':
        Spent_Amount+= row['Amount']

print(f'Amount Spent on {currentMonth}:{Spent_Amount}')

#Group by category
data['Category'] = data['Category'].str.strip().str.lower()
category_spending = data.groupby('Category')['Amount'].sum()
print(category_spending)
    
# create a pie chart based on categories
plt.figure(figsize=(6,6))
category_spending.plot.pie(autopct='%1.1f%%')
plt.title('Incomes and Spendings')
plt.ylabel('') 
plt.show()

data['Week'] = data['Date'].dt.isocalendar().week
weekly_spending = data.groupby('Week')['Amount'].sum()
plt.figure(figsize=(10, 5))
weekly_spending.plot(kind='line', marker='o')
plt.title('Weekly Spending Trend')
plt.xlabel('Week Number')
plt.ylabel('Spending ($)')
plt.grid(True)
plt.show()