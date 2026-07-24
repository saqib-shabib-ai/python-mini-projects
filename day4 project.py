#user input with input()
name = input("Enter your name: ")
print(f"Hello, {name}!")
 
#Type conversion (int() and float())
Num1 = input("Enter a number: ")
Num1 = int(Num1)
print(f"Number thripled :{Num1 * 3} ")

#String formating with f-strings
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 + num2
print(f"the result of {num1} and {num2} is {result}")

#Basic arithmetic Operations
a = 10
b = 15
print(f"Addition: {a + b}")
print(f"subtrection: {a - b}")
print(f"multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor division: {a // b}")
print(f"modulus: {a % b}")
print(f"Exponentiaton: {a ** b}")


#Simple colculator
#Step 1: Taking user input
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

#step 2 :perform arithmetic
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 !=0 else "cannot divided by zero"

#step 3: display the result
print(f"Addition: {number1} + {number2} = {addition}")
print(f"Subtrction: {number1} - {number2} = {subtraction}")
print(f"Multiplication: {number1} * {number2} = {multiplication}")
print(f"Division: {number1} / {number2} = {division}")