def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error! Division by zero."

while True:
    print("\n--- CALC MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "6":
        print("Exiting CALC. Goodbye!")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    elif choice == "5":
        print("Result:", modulus(a, b))
    else:
        print("Invalid choice! Please try again.")
