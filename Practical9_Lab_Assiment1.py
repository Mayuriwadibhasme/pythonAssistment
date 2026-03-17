class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0.0
        self.address = ""

    def get_input(self):
        self.name = input("Enter employee name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def print_info(self):
        print("\nEmployee Information")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Salary  : {self.salary}")
        print(f"Address : {self.address}")


class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("Enter department: ")

    def print_info(self):
        super().print_info()
        print(f"Department : {self.department}")


# Process information of 10 managers
managers = []
for i in range(10):
    print(f"\n--- Enter details for Manager {i+1} ---")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n========= Manager Details =========")
for i, m in enumerate(managers, start=1):
    print(f"\nManager {i}:")
    m.print_info()
