# Factoring, Common Factors, and Factoring Square Roots

import math

# Find the factors of a given number
def find_factors(number):
    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    return factors

# Find the common factors of two numbers
def find_common_factors(number1, number2):
    factors1 = set(find_factors(number1))
    factors2 = set(find_factors(number2))
    common_factors = factors1.intersection(factors2)
    return common_factors

# Factorize a number
def factorize(number):
    factors = find_factors(number)
    factors.sort()
    return factors

# Factorize a square root
def factorize_square_root(number):
    factorized_number = ''
    factors = factorize(number)
    for factor in factors:
        factorized_number += str(factor) + '√'
    return factorized_number

# Example usage

# Find factors of a number
number = 36
factors = find_factors(number)
print("Factors of", number, ":", factors)

# Find common factors of two numbers
number1 = 24
number2 = 36
common_factors = find_common_factors(number1, number2)
print("Common factors of", number1, "and", number2, ":", common_factors)

# Factorize a number
number = 120
factorized_number = factorize(number)
print("Factorized form of", number, ":", factorized_number)

# Factorize a square root
number = 75
factorized_sqrt = factorize_square_root(number)
print("Factorized form of √", number, ":", factorized_sqrt)
