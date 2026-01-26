grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15), 
    "Apples": ("Produce", 1.50, 50)
}
eggs_details = grocery_inventory.get("Eggs")
print(eggs_details[1])
if eggs_details[1]>5:
    print("Eggs are too expensive, reducing the price by $1.")
    eggs_details_list = list(eggs_details)
    eggs_details_list[1] = eggs_details_list[1] - 1
    eggs_details = tuple(eggs_details_list)
    print(eggs_details)
    grocery_inventory.update({"Eggs": eggs_details})
    print(grocery_inventory)
else:
    print("The price of Eggs is reasonable.")
grocery_inventory["Tomatoes"] = "Produce", 1.20, 30
print("Inventory after adding Tomatoes:", grocery_inventory)
milk_details = grocery_inventory.get("Milk")
if milk_details[2]<10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    milk_details_list = list(milk_details)
    milk_details_list[2] = milk_details_list[2] + 20
    milk_details = tuple(milk_details_list)
    print(milk_details)
    grocery_inventory.update({"Milk": milk_details})
    print(grocery_inventory)
else:
    print("Milk has sufficient stock.")
apples = grocery_inventory.get("Apples")
if apples[1]>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
print("Updated inventory:" , grocery_inventory)
