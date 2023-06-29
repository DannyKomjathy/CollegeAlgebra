# Ratios, Proportions, and Conversions

# Ratio calculation
def calculate_ratio(a, b):
    ratio = a / b
    return ratio

# Proportion calculation
def calculate_proportion(a, b, c):
    proportion = (a * c) / b
    return proportion

# Unit conversion
def convert_units(value, from_unit, to_unit):
    conversions = {
        'cm_to_inch': 0.393701,
        'inch_to_cm': 2.54,
        'km_to_mile': 0.621371,
        'mile_to_km': 1.60934,
        # Add more conversions as needed
    }
    conversion_factor = conversions.get(from_unit + '_to_' + to_unit)
    if conversion_factor is None:
        return None
    converted_value = value * conversion_factor
    return converted_value

# Calculate a ratio
ratio_value = calculate_ratio(4, 2)
print("Ratio:", ratio_value)

# Calculate a proportion
proportion_value = calculate_proportion(2, 3, 4)
print("Proportion:", proportion_value)

# Convert units
value_to_convert = 10
converted_value = convert_units(value_to_convert, 'cm', 'inch')
if converted_value is not None:
    print(value_to_convert, 'cm is equal to', converted_value, 'inches')
else:
    print("Conversion not available")
