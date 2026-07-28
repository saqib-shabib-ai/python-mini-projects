#What are function
#Defining a function
def function_name():
 #Code block inside the function
 print("Hello from the Function")

function_name()

#Now giving the name to the function
def greet():
 print("Hello!, Welcome to the python")

greet()

#Function Parameters and Arguments
def greet_user(name):
 print(f"Hello, {name}! Welcome to the python")

greet_user('Saqib shabib')

#More then one parameter
def add(a , b):
 print(f"The sum is: {a + b}")

add(10 , 10)

#Return statements
def multyply(a , b):
 return a * b

result = multyply(5 , 3)
print("The result is:", result)

#Basic math quiz game
import random

#Step 1: Define the math question function
def genarate_question():
 num1 = random.randint(1, 10)
 num2 = random.randint(1, 10)
 operator = random.choice(['+','-','*'])
 
 if operator == '+':
  answer = num1 + num2
 elif operator == '-':
  answer = num1 - num2
 else:
  answer = num1 * num2

 return f"{num1} {operator} {num2}", answer

#Step 2: The main quiz game Function
def math_quiz():
 score = 0
 rounds = 5

 print("\n--- Welcome to the math quiz game ---")
 print("You will be presented with math problem, and you need to provide the correct answers.")

 for i in range(rounds):
  question, correct_answer = genarate_question()
  print(f"\nQuestion {i + 1}: {question}")
  user_answer = int(input("Your answer: "))

  if user_answer == correct_answer:
   print("Correct")
   score += 1
  else:
   print(f"Wrong! The correct answer is {correct_answer}")

 print("---Game Over---")
 print(f"Your final score is: {score}/{rounds}")
 if score == rounds:
  print("Congrats!, You got all the answer correct.")
 elif score >= rounds // 2:
  print("Good job! , You did it well.")
 else:
  print("Keep precticing!, You will get better.")
#step 3: Run the Game
math_quiz()