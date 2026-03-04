numbers = input("Enter integers separated by spaces: ")
tuple_data = tuple(map(int, numbers.split()))

print("\nTuple entered:", tuple_data)
print("Total number of items in Tuple:", len(tuple_data))
print("Last item in Tuple:", tuple_data[-1])
print("Tuple in reverse order:", tuple_data[::-1])

if 5 in tuple_data:
    print("Yes, Tuple contains 5")
else:
    print("No, Tuple does not contain 5")

if len(tuple_data) > 2:
    modified_tuple = tuple_data[1:-1]
    sorted_tuple = tuple(sorted(modified_tuple))
    print("Tuple after removing first & last, then sorting:", sorted_tuple)
else:
    print("Not enough elements to remove first and last.")
