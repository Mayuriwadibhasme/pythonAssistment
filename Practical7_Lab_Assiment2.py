balance = 0.0

def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Deposited:", amount)
    print("Updated Balance:", balance)

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
        print("Updated Balance:", balance)
    else:
        print("Insufficient Balance!")

while True:
    print("\n--- BANK ACCOUNT MENU ---")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_balance()
    elif choice == "2":
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == "3":
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)
    elif choice == "4":
        print("Exiting... Thank you for using CALC Bank!")
        break
    else:
        print("Invalid choice! Please try again.")
