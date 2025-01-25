def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Get input from the user
n = int(input("Enter a non-negative integer: "))

# Calculate and print the factorial
print(f"The factorial of {n} is {factorial(n)}")
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#EITHER THE CODE ABOVE OR THE SHORTCUT BELOW:
"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
import math 
n= int(input("Enter the number you want the factorial of:"))
if n<1:
    print("Factorial doesn't exist for negative numbers")
else:
    print(f"The factorial of {n} is {math.factorial(n)}")