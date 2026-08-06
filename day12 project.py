# What are Exception?
# Exception are error that occur during the exicution of a program

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("result: ", result)
except ZeroDivisionError:
    print("Error! Devision zero is not allowed. ")
except ValueError:
    print("Error! invalid input. Enter valid a number. ")

# Using try,except,else, and finally
try:
    # Code that might an exception
except:
    # Code to handle the execption
else:
    # Execute if no exception occurs
finally:
    # Always execute, even if an exception occurs

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("result: ", result)
except ZeroDivisionError:
    print("Error! Devision zero is not allowed. ")
else:
    print("No exception occurs. Result: ",result )
finally:
    print("Finally block executed. Program ended. ")

# Handling multiple exceptions

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("result: ", result)
except (ZeroDivisionError , ValueError):
    print("Error! Devision zero is not allowed or invalid input. ")

# Raising Custom Exception

def withdraw(amount):
    if amount < 0:
        raise ValueError("Invalid withdrawal amount - Amount cannot be negative")
    print(f"Youhave withdraw ${amount}")

try:
    withdraw(-50)
except ValueError as e:
    print(e)


# Day 12 project: Safe Calculator
# Step 1: Define Calculator Functions
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    raise ZeroDivisionError("Cannot divide by zero")
  return x / y

# Step 2: Display Menu
def show_menu():
  print("\n--- Safe Calculator Menu ---")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")

# Step 3: Main Program
while True:
  show_menu()
  choice = input("Enter your choice (1-5): ")

  if choice == '5':
    print("Exiting the calculator. Goodbye!")
    break

  try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
      print("Result:", add(num1, num2))
    elif choice == '2':
      print("Result:", subtract(num1, num2))
    elif choice == '3':
      print("Result:", multiply(num1, num2))
    elif choice == '4':
      print("Result:", divide(num1, num2))
    else:
      print("Invalid choice. Please select a valid option.")

  except ValueError:
    print("Invalid input. Please enter valid numbers.")
  except ZeroDivisionError as e:
    print(f"Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")
  finally:
    print("Thank you for using the Safe Calculator!... Restarting...")