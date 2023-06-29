# Simple and Compound Interest Formulas

# Calculate simple interest
def calculate_simple_interest(principal, rate, time):
    # Simple interest formula: I = P * r * t
    interest = principal * rate * time
    return interest

# Calculate compound interest
def calculate_compound_interest(principal, rate, time):
    # Compound interest formula: A = P * (1 + r/n)^(n*t)
    # Where A is the final amount, P is the principal, r is the interest rate,
    # t is the time in years, and n is the number of compounding periods per year.
    n = 1  # Assume annual compounding
    amount = principal * (1 + rate/n)**(n*time)
    interest = amount - principal
    return interest

# Example values
principal = 1000
rate = 0.05
time = 3

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Calculate compound interest
compound_interest = calculate_compound_interest(principal, rate, time)

# Print the results
print("Principal:", principal)
print("Rate:", rate)
print("Time:", time)
print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
