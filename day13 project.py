# Understanding Return Value in Function
# Syntax
'''def function_name():
    #Code
    return Value '''

#example
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

# Using function to Perform Calculation
def regtangle_area(width, height):
    return width * height

area = regtangle_area(10, 20)
print(area)

# How to return multiple value
def math_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition,subtraction,multiplication,division

result = math_operations(10, 5)
print(result)

# Best Prectices for Return values
# Temperature converter

# Step 1:Define Conversion Functions
def celsius_to_farhenheit(celsius):
    return(celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def farhenheit_to_celsius(farhenheit):
    return(farhenheit -32) * 5/9

def farhenheit_to_kelvin(farhenheit):
    return(farhenheit -32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return  kelvin - 273.15

def kelvin_to_farhenheit(kelvin):
    return(kelvin - 273.15) * 9/5 + 32

# Step 2: Display the Menu
def show_menu():
    print(f"\n--- Temperatur Converter Menu ---")
    print("1. Celsius to Farhenheit & Kelvin. ")
    print("2. farhenheit to celsius & kelvin. ")
    print("3. kelvin to celsius & farhenheit. ")
    print("4. Exit. ")

# Step 3: Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4):")

    if choice == "1":
        celsius = float(input("Enter Temperature in Celsius: "))
        print(f"Farhenheit: {celsius_to_farhenheit(celsius):.2f}")
        print(f"Kelvin: {celsius_to_kelvin(celsius):.2f}")
    elif choice == "2":
        farhenheit = float(input("Enter Temperature in farhenheit: "))
        print(f"celcius: {farhenheit_to_celsius(farhenheit):.2f}")
        print(f"kelvin: {farhenheit_to_kelvin(farhenheit):.2f}")
    elif choice == "3":
        kelvin = float(input("Enter Temperature in kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(kelvin):.2f}")
        print(f"Fahenheit: {kelvin_to_farhenheit(kelvin):.2f}")
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("invalid choice. Please select the valid option.")
