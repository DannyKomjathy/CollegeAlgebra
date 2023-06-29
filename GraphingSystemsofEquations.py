import numpy as np
import matplotlib.pyplot as plt

# Graphing Systems of Two Equations

# Define the equations
def equation1(x):
    return 2*x + 1

def equation2(x):
    return -3*x + 5

# Generate x values
x_values = np.linspace(-10, 10, 100)

# Generate y values for each equation
y_values1 = equation1(x_values)
y_values2 = equation2(x_values)

# Plot the equations
plt.plot(x_values, y_values1, label='2x + 1')
plt.plot(x_values, y_values2, label='-3x + 5')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphing Systems of Two Equations')

# Add legend
plt.legend()

# Show the graph
plt.show()
