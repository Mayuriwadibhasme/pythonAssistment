prices = input("Enter item prices separated by spaces: ")
price_tuple = tuple(map(float, prices.split()))

print("\nPrice Tuple:", price_tuple)
print("Total number of items sold:", len(price_tuple))
print("Cheapest item price:", min(price_tuple))
print("Costliest item price:", max(price_tuple))
print("Price list in ascending order:", tuple(sorted(price_tuple)))

costliest = max(price_tuple)
count_costliest = price_tuple.count(costliest)
print("Number of costliest items sold:", count_costliest)
