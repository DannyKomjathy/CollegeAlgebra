# Cost, Revenue, and Profit Equations

# Calculate the cost given the quantity
def calculate_cost(quantity):
    # Cost equation: C = 50 + 10q
    return 50 + 10 * quantity

# Calculate the revenue given the quantity
def calculate_revenue(quantity):
    # Revenue equation: R = 20q
    return 20 * quantity

# Calculate the profit given the quantity
def calculate_profit(quantity):
    cost = calculate_cost(quantity)
    revenue = calculate_revenue(quantity)
    # Profit equation: P = R - C
    return revenue - cost

# Example quantity
quantity = 10

# Calculate the cost, revenue, and profit
cost = calculate_cost(quantity)
revenue = calculate_revenue(quantity)
profit = calculate_profit(quantity)

# Print the results
print("Quantity:", quantity)
print("Cost:", cost)
print("Revenue:", revenue)
print("Profit:", profit)
