#How to create a list
shopping_list = ["Milk","Eggs","Breads"]
print(shopping_list)

#List Operations: Adding, Removing, and Accessing items

#Accessing elements
fruit_list = ["mango","apple","cherry"] 
print(fruit_list[0])

#Append and insert Function
shopping_list = ["Milk","Eggs","Breads"]

shopping_list.append("Butter")
shopping_list.insert(0,"juice")

print(shopping_list)

#Remove function
shopping_list.remove("Breads") #remove function is used for removine specific item
print(shopping_list)

#Pop function
shopping_list.pop()
print(shopping_list)

#Using loop in list
for item in shopping_list:
    print(f"-{item}")

#Specifing index through loops
for index, item in enumerate(shopping_list):
    print(f"{index}. {item}")

#Day 8 project: Shopping list App

#Step 1: Initialize an empty shopping list
Shopping_list = []

#Step 2: Define the main menu
def show_menu():
    print("\n---Shopping List Menu---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear the list")
    print("5. Exit")

#Step 3: The main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n---Shopping List---")
        if not Shopping_list:
            print("Your shopping list is empty. ")
        else:
            for index, item in enumerate(Shopping_list):
                print(f"{index + 1}. {item}")

    elif choice == "2":
        item = input("Enter the item to add: ")
        Shopping_list.append(item)
        print(f"{item} has been added to shopping list. ")

    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in Shopping_list:
            Shopping_list.remove(item)
            print(f"{item} has been removed form the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")

    elif choice == "4":
        Shopping_list.clear()
        print("The shopping has been cleared. ")

    elif choice == "5":
        print("Goodbye! Happy Shopping! ")
        break

    else:
        print("Invalid choice please try again. ")
        