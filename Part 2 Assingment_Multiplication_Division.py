# Program to perform multiplication and division of two numbers

# Asking the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculating the multiplication
multiplication = num1 * num2

# Calculating the division
# Adding a check to avoid division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero is not allowed)"

# Displaying the results
print("The multiplication of", num1, "and", num2, "is:", multiplication)
print("The division of", num1, "by", num2, "is:", division)
