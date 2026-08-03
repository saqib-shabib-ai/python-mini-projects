# What are tuples
my_tuple = (1, 2, 3)

# Accessing elements
fruits = ("apple", "banana", "cherry")
print(fruits[0])

print(fruits[-1])

cordinates = (10, 20, 30)
x, y, z = cordinates
print(x)
print(y)
print(z)

# Tuples operation and unpacking
fruits = ("apple", "banana", "cherry")
print(len(fruits))

print(fruits + ("orange",))

# What are sets
my_set = {1, 2, 3}

ingredients = {"milk", "sugar","flour"}
ingredients.add("eggs")

print(ingredients)

ingredients.remove("sugar")
print(ingredients)

# Set operations (union,intersection,difference)
set_a = {"sugar", "milk", "flour"}
set_b = {"sugar", "water"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)

# Ingredient checker

# Step 1 : Define the recipe ingredient

recipe_ingredients = {"flour","sugar","butter","eggs","milk"}

# Step 2: Get user input for available ingredient

user_input = input("Enter the ingredient you have (saparated by commas):")
user_ingredients = set(user_input.split(","))

# Step 3: compare the ingredients

missing_ingredients =recipe_ingredients-user_ingredients
extra_ingredients = user_ingredients-recipe_ingredients

# step 4: Display results
print("\n--- Ingredients check Results ---")
if missing_ingredients:
    print(f"You are missing the following ingredients: {','.join(missing_ingredients)}")
else:
    print("You have all the ingredients needed. ")

if extra_ingredients:
    print(f"you have extra ingredients: {','.join(extra_ingredients)}")
else:
    print("You have all the ingredient needed.")
