prices = [29.99, 45.50, 12.75, 38.20]
discount_rate = [0.90, 0.80, 0.85, 0.95]
#discount_one = 0.90
#discount_two = 0.80
#discount_tree = 0.85
#discount_four = 0.95
for cost in range(len(prices)):
    if cost == 0:
        discount = 0.10
    elif cost == 1:
        discount = 0.20
    elif cost == 2:
        discount = 0.15
    elif cost == 3:
        discount = 0.05
    prices[cost] = prices[cost] * (1- discount)
    print(f"Updated price for item {cost}: ${prices[cost]:.2f}")

    #print("new price:", {prices[cost]} * range(discounts)[cost])
    #print("new price:",prices)