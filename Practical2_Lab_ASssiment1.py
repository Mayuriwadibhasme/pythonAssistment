# Part (a): Calculate current using Ohm's Law
V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (R): "))

I = V / R
print("Current (I):", I, "A")

# Part (b): Display nature of current
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")
