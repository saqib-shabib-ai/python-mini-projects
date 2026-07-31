#What are Dictionaries
#The syntax of how you create dictionaries
my_dic = {
    "key1": "value1",
    "key2": "value2",
    "key3":"value 3",
}

#creating a simple contact
contact = {
    "name": "saqib shabib",
    "phone No": "123-456-789",
    "Email": "saqib@example.com"
}
#print(contact)
print(contact.get("Email"))  #accessing value

contact["phone No"]= "111-222-333"  #Modifying dictionary value
print(contact)

#Adding new key

contact["Address"] = "township"
print(contact)

#Removing Key
del contact["Email"]
print(contact)

#Looping through Dictionary
for key, value in contact.items():
    print(f"{key}: {value}")

#checking for key exist
if "Email" in contact:
    print("Email found!. ")
else:
    print("Email not found!. ")

#Day 8 Project: Contact Book
#Step 1: Initialize an empty contact book
contacts = {}

#step 2:Display the menu
def show_menu():
    print("\n---Contact Book Menu---")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")

#Step 3: Add a contact
def add_contact():
    name = input("Enter your name for contact: ")
    phone = input("Enter contact number: ")
    Email = input("Enter contact Email: ")
    contacts[name]= {"phone": phone, "Email": Email }
    print(f"contact {name} has been added successfully. ")
    
#Step 4: View  All contact
def view_contect():
    if contacts:
        print("\n---Contact list---")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"phone: {details['phone']}")
            print(f"Email: {details['Email']}")
    else:
        print("Your contact book is empty. ")

#Step 5: Search a Contact
def search_contact():
    name = input("Enter the name of the contact you want to search: ")
    if name in contacts:
        print(f"\n---Contect Details for {name}---")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print(f"Contact {name} is not found in your contact book")

#Step 6: Edit a contact
def edit_contact():
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        Email = input("Enter new Email: ")
        contacts[name] = {"phone": phone, "Email": Email}
        print(f"contact {name} has been updated successfully! ")
    else:
        print(f"Contact {name} is not found in your contact book")

#Step 7:Delete a Contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully!")
    else:
        print(f"Contact {name} not found in your contact book.")

#Step 8:Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6):")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contect()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thanks for using the contact book , Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")


