produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]
print(groceries)
for section in groceries:
    print("section name:", section)
    for item in section:
        print(f"Item name:{item}")
    print("")