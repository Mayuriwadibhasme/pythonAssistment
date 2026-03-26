import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("company_sales_data.csv")

plt.figure(figsize=(8,5))
plt.plot(data['month_number'], data['total_profit'], marker='o', color='blue')
plt.title("Company Profit per Month")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

plt.figure(figsize=(10,6))
plt.plot(data['month_number'], data['facecream'], marker='o', label='Face Cream')
plt.plot(data['month_number'], data['facewash'], marker='o', label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], marker='o', label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], marker='o', label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], marker='o', label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], marker='o', label='Moisturizer')
plt.title("Product Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
bar_width = 0.4
plt.bar(data['month_number'], data['facecream'], width=bar_width, label='Face Cream', align='center')
plt.bar(data['month_number']+0.4, data['facewash'], width=bar_width, label='Face Wash', align='center')
plt.title("Face Cream vs Face Wash Sales")
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()
plt.show()

total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]
products = ['Face Cream','Face Wash','Toothpaste','Bathing Soap','Shampoo','Moisturizer']

plt.figure(figsize=(7,7))
plt.pie(total_sales, labels=products, autopct='%1.1f%%')
plt.title("Total Sales Distribution (Last Year)")
plt.show()
