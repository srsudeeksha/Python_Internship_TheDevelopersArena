# Contact Book Program - Week 3 Task
# Demonstrates file handling and error handling in Python

FILE_NAME = "contacts.txt"

# Function to save a contact to file
def save_contact(name, phone):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(f"{name},{phone}\n")
        print(f"✅ Contact saved: {name} - {phone}")
    except Exception as e:
        print(f"❌ Error saving contact: {e}")

# Function to read all contacts from file
def read_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("📂 No contacts found.")
                return
            print("\n--- Contact List ---")
            for line in contacts:
                name, phone = line.strip().split(",")
                print(f"{name}: {phone}")
    except FileNotFoundError:
        print("❌ No contact file found. Please add a contact first.")
    except Exception as e:
        print(f"❌ Error reading contacts: {e}")

# Main program loop
while True:
    print("\n=== Contact Book Menu ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        save_contact(name, phone)
    elif choice == "2":
        read_contacts()
    elif choice == "3":
        print("👋 Exiting Contact Book. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
