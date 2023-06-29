import math

# Exponents and Logarithms

# Calculate the value of an exponentiation
def calculate_exponentiation(base, exponent):
    value = base ** exponent
    return value

# Calculate the logarithm of a number
def calculate_logarithm(number, base):
    value = math.log(number, base)
    return value

# Example values
base = 2
exponent = 3
number = 8
log_base = 2

# Calculate the value of an exponentiation
exponentiation_value = calculate_exponentiation(base, exponent)

# Calculate the logarithm of a number
logarithm_value = calculate_logarithm(number, log_base)

# Print the results
print("Base:", base)
print("Exponent:", exponent)
print("Exponentiation Value:", exponentiation_value)
print("Number:", number)
print("Logarithm Base:", log_base)
print("Logarithm Value:", logarithm_value)
