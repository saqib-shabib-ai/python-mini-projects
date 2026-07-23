# Storing in a variable
name = "saqib"
nameOFperson = "saqib shabib"

# Storing an age in a variable
age = 19

# Sting
name = "saqib"

# Integer
age = 19

# Float
height = 5.9

# Boolean
Is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(Is_student))

# Type conversion
age = "19"
Myage = int(age)
print(Myage + 3)

# Three different method of adding string
# No1
name = "saqib shabib"
print("hello " + name + " how are you!")
# No2
name = "saqib"
print("hello my friend, {}!".format(name))
# No3
name = "saqib shabib"
print(f"hello,{name}")

#genralized greeting program
# step 1: Ask your details
name = input("enter your name: ")
age = int(input("enter your age: "))
colour = input("enter your favorite colour: ")

#Step 2: Genrate a personlized greeting message
print("\n----Personlized Greeting----")
print(f"Hello, {name}!")
print(f"You are {age} years old and {colour} is a beautiful color!")
print(f"you are now ready to start python adventures")