# Percents, Decimals, and Fractions

# Convert a decimal to a percent
def decimal_to_percent(decimal):
    percent = decimal * 100
    return percent

# Convert a percent to a decimal
def percent_to_decimal(percent):
    decimal = percent / 100
    return decimal

# Convert a decimal to a fraction
def decimal_to_fraction(decimal):
    from fractions import Fraction
    fraction = Fraction(decimal).limit_denominator()
    return fraction

# Convert a fraction to a decimal
def fraction_to_decimal(fraction):
    decimal = fraction.numerator / fraction.denominator
    return decimal

# Convert a percent to a fraction
def percent_to_fraction(percent):
    fraction = percent_to_decimal(percent_to_decimal(percent))
    return fraction

# Convert a fraction to a percent
def fraction_to_percent(fraction):
    percent = decimal_to_percent(fraction_to_decimal(fraction))
    return percent

# Convert a percent to a mixed number
def percent_to_mixed_number(percent):
    whole = int(percent)
    decimal = percent % 1
    fraction = decimal_to_fraction(decimal)
    return f"{whole} {fraction}"

# Convert a mixed number to a percent
def mixed_number_to_percent(mixed_number):
    parts = mixed_number.split()
    whole = int(parts[0])
    fraction_parts = parts[1].split('/')
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    fraction = numerator / denominator
    decimal = whole + fraction
    percent = decimal_to_percent(decimal)
    return percent

# Convert a decimal to a mixed number
def decimal_to_mixed_number(decimal):
    whole = int(decimal)
    fraction = decimal % 1
    fraction = decimal_to_fraction(fraction)
    return f"{whole} {fraction}"

# Convert a mixed number to a decimal
def mixed_number_to_decimal(mixed_number):
    parts = mixed_number.split()
    whole = int(parts[0])
    fraction_parts = parts[1].split('/')
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    fraction = numerator / denominator
    decimal = whole + fraction
    return decimal

# Convert a fraction to a mixed number
def fraction_to_mixed_number(fraction):
    whole = fraction.numerator // fraction.denominator
    numerator = fraction.numerator % fraction.denominator
    mixed_number = f"{whole} {numerator}/{fraction.denominator}"
    return mixed_number

# Convert a mixed number to a fraction
def mixed_number_to_fraction(mixed_number):
    parts = mixed_number.split()
    whole = int(parts[0])
    fraction_parts = parts[1].split('/')
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    fraction = whole * denominator + numerator
    fraction = fraction / denominator
    fraction = fraction(fraction).limit_denominator()
    return fraction

# Convert a fraction to a mixed number
def fraction_to_mixed_number(fraction):
    whole = fraction.numerator // fraction.denominator
    numerator = fraction.numerator % fraction.denominator
    mixed_number = f"{whole} {numerator}/{fraction.denominator}"
    return mixed_number

# Convert a mixed number to a fraction
def mixed_number_to_fraction(mixed_number):
    parts = mixed_number.split()
    whole = int(parts[0])
    fraction_parts = parts[1].split('/')
    numerator = int(fraction_parts[0])
    denominator = int(fraction_parts[1])
    fraction = whole * denominator + numerator
    fraction
