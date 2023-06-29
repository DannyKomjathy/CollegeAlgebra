import numpy as np
import matplotlib.pyplot as plt

# Polynomial Graphs

# Define the polynomial function
def polynomial_function(x):
    return x**3 - 2*x**2 - 5*x + 6

# Generate x values
x_values = np.linspace(-5, 5, 100)

# Generate y values for the polynomial function
y_values = polynomial_function(x_values)

# Plot the polynomial function
plt.plot(x_values, y_values, label='y = x^3 - 2x^2 - 5x + 6')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Graph')

# Add grid
plt.grid(True)

# Add legend
plt.legend()

# Show the graph
plt.show()
