# Solving Quadratic Equations

import math

# Solve a quadratic equation using the quadratic formula
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        # Two real and distinct solutions
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # One real solution (repeated root)
        x = -b / (2*a)
        return x
    else:
        # Complex solutions
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return x1, x2

# Example quadratic equation coefficients
a = 2
b = -5
c = -3

# Solve the quadratic equation
solution = solve_quadratic(a, b, c)

# Print the solution
print("Solution:")
if isinstance(solution, tuple):
    # Two distinct solutions or complex solutions
    print("x1 =", solution[0])
    print("x2 =", solution[1])
else:
    # One repeated solution
    print("x =", solution)
