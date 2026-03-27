import pandas as pd

df = pd.read_excel("employee_reports.txt")

automotive_employees = df[df['Department'] == 'Automotive']
print("Employees in Automotive domain:\n", automotive_employees[['Employee ID','Employee Name']])

emp_id = int(input("Enter Employee ID: "))
emp_details = df[df['Employee ID'] == emp_id]
if not emp_details.empty:
    print("\nDetails of Employee ID", emp_id, ":\n", emp_details)
else:
    print("\nNo employee found with ID", emp_id)

developers = df[df['Designation'].str.contains("Developer", case=False)]
print("\nList of Developers:\n", developers[['Employee ID','Employee Name','Department','Designation']])
