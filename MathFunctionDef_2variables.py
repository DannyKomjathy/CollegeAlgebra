# Math Function Definition with Two Variables

# Define a math function with two variables
def math_function(x, y):
    # Example function: f(x, y) = x^2 + 2xy + y^2
    result = x**2 + 2*x*y + y**2
    return result

# Test the math function with sample values
x_value = 3
y_value = 4
function_result = math_function(x_value, y_value)
print("Function Result:", function_result)
