# # What is file Reading in Python?
# # Reading Files using open() Function
# '''with open("filename.txt", "r") as file:  # Syntax
#     content = file.read()
#     print(content)'''


# # Example
# with open("sample.txt", "r") as file:  #sample.txt is a file name
#     content = file.read()
#     print(content)

# # You can access each line at a time
# with open("sample.txt", "r") as file:  
#     for line in file:
#         print(line.strip()) 

# # Reading Modes(r, rb, r+)
# with open("sample.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

# # Handling File Reading Errors
# try:
#     with open("non_exist_file.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found")

# # Another Example
# try:
#     with open("sample.txt", "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("File not found")

# Day 15 Project: Recipe viewers App

# Step 1:Load Recipe from File
def load_recipe(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            recipes = content.split("\n\n")
            recipe_dict = {}
            for recipe in recipes:
                lines = recipe.split("\n")
                if len(lines) >= 3:
                    name = lines[0].strip()
                    ingredients = lines[1].replace('ingredients: ','').strip()
                    instructions = lines[2].replace('instructions: ','').strip()
                    recipe_dict[name] = {"ingredients": ingredients, "instructions": instructions}
            return recipe_dict
    except FileNotFoundError:
        print("File not found. ")
        return{}

# Step 2: Display Recipe Menu
def show_menu():
    print("\n---- Recipe Viewer Menu ----")
    print("1. View Recipe by Name")
    print("2. List All Recipes")
    print("3. Exit")

# Step 3: Recipes Details
def view_recipe(recipes):
    name = input("Enter the name of recipe: ").strip()
    if name in recipes:
        print(f"\n--- Recipe {name} Details ----")
        print(f"ingredients: {recipes[name]['ingredients']}")
        print(f"instructions: {recipes[name]['instructions']}")
    else:
        print("recipe not found.")

# Step 4: Main Program
recipe_file = "Recipes.txt"
recipes = load_recipe(recipe_file)

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        view_recipe(recipes)
    elif choice == '2':
        print("\n--- All Recipes ----")
        for name in recipes:
            print(name)
    elif choice == '3':
        print("Exiting the Program. ")
        break
    else:
        print("Invalid Choice. Please Try Again. ")