name = "Mayuri"
emp_id = "E101"
department = "HR"
basic_salary = 30000

da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary
gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - 500

print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("Net Salary:", net_salary)
