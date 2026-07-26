# If ,elif,and else statement and comparision operators
number = 5

if number > 5:
    print("The number is greater then 5")
elif number == 5:
    print("The number is equal to 5")
else:
    print("The number is less then 5")

#Logical operators
a = 7
b = 20
if a >8 or b < 19:
    print("Both are true")
else:
    print("Both are false")
    
#nested If-Else statement
number = 4

if number > 5:
    print("the number is greater then 5")
elif number == 5:
    print("the number is equal to 5")
elif  number == 4:
    print("the number is equal to 4")
else:
    print("the number is less then 5")

#day 5 project: Number comparision tool
#step 1: taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
 #step 2 : compare the number and print the result
print("\n ----Comparision Results ----")
if num1 == num2:
    print(f"Both numbers are equal: {num1}")
elif num1 > num2:
    print(f"The {num1} is greater then {num2}")
else:
    print(f"The {num2} is greater then {num1}")

#step 3: checking for zero
if num1 == 0 or num2 == 0:
    print("\n One numbers is zero")
else:
    print("\n Both numbers are non-zero")