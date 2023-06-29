# Application of Linear Systems

# Solve a word problem involving linear systems
def solve_application():
    # Word problem:
    # A bakery sells two types of cakes: chocolate cakes and vanilla cakes.
    # The total revenue from selling 4 chocolate cakes and 3 vanilla cakes is $50.
    # The total revenue from selling 2 chocolate cakes and 5 vanilla cakes is $45.
    # Find the price of each type of cake.

    # Let x be the price of a chocolate cake
    # Let y be the price of a vanilla cake

    # Formulating the system of equations:
    # 4x + 3y = 50
    # 2x + 5y = 45

    # Solve the system of equations
    equation1 = [4, 3, 50]
    equation2 = [2, 5, 45]

    # Solve the system using the substitution method
    y = (equation1[2] - equation1[0] * equation2[1] / equation2[0]) / (equation1[1] - equation1[0] * equation2[1] / equation2[0])
    x = (equation2[2] - equation2[1] * y) / equation2[0]

    return x, y

# Solve the application problem
solution = solve_application()
chocolate_price = solution[0]
vanilla_price = solution[1]

# Print the solution
print("Solution:")
print("Price of a chocolate cake: $", chocolate_price)
print("Price of a vanilla cake: $", vanilla_price)
