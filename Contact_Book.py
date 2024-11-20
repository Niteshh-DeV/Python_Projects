# Contact book dictionary to store contact details
contact_book = {}

def add_contact():
    name = input("Enter contact name: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact_book[name] = {"phone": phone, "email": email}
        print(f"Contact for {name} added successfully.")

def view_contacts():
    if not contact_book:
        print("No contacts available.")
    else:
        print("\nContacts:")
        for name, details in contact_book.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")

def search_contact():
    name = input("Enter the name to search: ")
    if name in contact_book:
        print(f"\nName: {name}, Phone: {contact_book[name]['phone']}, Email: {contact_book[name]['email']}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact for {name} deleted successfully.")
    else:
        print("Contact not found.")

def contact_book_app():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    contact_book_app()