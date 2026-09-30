# Ask the user to enter a number
number = float(input("Enter a number: "))

# Classify the number
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")