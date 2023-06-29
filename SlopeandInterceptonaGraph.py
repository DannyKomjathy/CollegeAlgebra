# Slope and Intercept on a Graph

# Calculate the slope of a line given two points (x1, y1) and (x2, y2)
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Calculate the y-intercept of a line given the slope and a point (x, y)
def calculate_intercept(slope, x, y):
    intercept = y - slope * x
    return intercept

# Example points
x1 = 2
y1 = 4
x2 = 5
y2 = 7

# Calculate the slope
slope = calculate_slope(x1, y1, x2, y2)
print("Slope:", slope)

# Choose a point (x, y) on the line
x = 3
y = 5

# Calculate the intercept
intercept = calculate_intercept(slope, x, y)
print("Intercept:", intercept)
