# Basic Algebra - Solving Equations (One Variable)

# Solve a linear equation of the form ax + b = 0
def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        x = -b / a
        return x

# Solve a quadratic equation of the form ax^2 + bx + c = 0
def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return x1, x2

# Solve a general equation using sympy library (supports various types of equations)
# Make sure to install sympy library (pip install sympy) before running this code
def solve_equation(expression):
    from sympy import symbols, Eq, solve
    x = symbols(x)
    equation = Eq(expression, 0)
    solutions = solve(equation, x)
    return solutions

# Solve a linear equation
linear_solution = solve_linear_equation(2, -4)
print("Linear Equation Solution:", linear_solution)

# Solve a quadratic equation
quadratic_solution = solve_quadratic_equation(1, -3, 2)
print("Quadratic Equation Solution:", quadratic_solution)

# Solve a general equation
general_equation = solve_equation(2*x**2 - 5*x + 2)
print("General Equation Solution:", general_equation)
