
item1_price = 20
item2_price = 30
item3_price = 15
budget = 50
total_cost = item1_price + item2_price + item3_price

print(f"Total cost: ${total_cost}")

if total_cost <= budget:
    print("Within budget!")
    money_left = budget - total_cost
    print(f"Money left: ${money_left}")
else:
    print("Over budget!")
    money_needed = total_cost - budget
    print(f"More money needed: ${money_needed}")
