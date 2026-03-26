import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("new_recruitments.csv")

# a) Bar Chart
plt.figure(figsize=(8,5))
plt.bar(data['Company'], data['Recruitments'], color='skyblue')
plt.title("New Recruitments by Company")
plt.xlabel("Company")
plt.ylabel("Number of Recruitments")
plt.show()

# b) Pie Chart
plt.figure(figsize=(7,7))
plt.pie(data['Recruitments'], labels=data['Company'], autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
colors = ['gold','lightcoral','lightblue','lightgreen','pink','orange','violet','cyan']
explode = [0.1 if company == 'Amazon' else 0 for company in data['Company']]
plt.figure(figsize=(7,7))
plt.pie(data['Recruitments'], labels=data['Company'], autopct='%1.1f%%', colors=colors, explode=explode, shadow=True)
plt.title("Customized Recruitment Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure(figsize=(7,7))
plt.pie(data['Recruitments'], labels=data['Company'], autopct='%1.1f%%', wedgeprops=dict(width=0.4))
plt.title("Recruitment Doughnut Chart")
plt.show()

# Comparison: IBM vs Amdocs
ibm = data[data['Company'] == 'IBM']['Recruitments'].values[0]
amdocs = data[data['Company'] == 'Amdocs']['Recruitments'].values[0]

plt.figure(figsize=(6,4))
plt.bar(['IBM','Amdocs'], [ibm, amdocs], color=['blue','green'])
plt.title("Recruitments Comparison: IBM vs Amdocs")
plt.ylabel("Number of Recruitments")
plt.show()
