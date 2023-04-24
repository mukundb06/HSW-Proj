#PYTHON CALCULATOR
#FUNCTIONS PERFORMED
#ADDITION
#SUBTRACTION
#MULTIPLICATION
#DIVISION

import Addition
import Subtraction
import Multiplication
import Division

print("Select function.")
print("1.Addition")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")

while True:
    
    choice = input("Enter choice(1/2/3/4): ")

    
    if choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(n1, "+", n2, "=", Addition.add(n1, n2))

        elif choice == '2':
            print(n1, "-", n2, "=", Subtraction.subtract(n1, n2))

        elif choice == '3':
            print(n1, "*", n2, "=", Multiplication.multiply(n1, n2))

        elif choice == '4':
            print(n1, "/", n2, "=", Division.divide(n1, n2))
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
