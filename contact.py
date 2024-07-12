import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
        self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.contacts = [Contact(**contact) for contact in data]

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([vars(contact) for contact in self.contacts], file, indent=2)

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def edit_contact(self, index, name, phone, email):
        if 1 <= index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.name = name
            contact.phone = phone
            contact.email = email
            self.save_contacts()
            print("Contact updated successfully.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 1 <= index <= len(self.contacts):
            del self.contacts[index - 1]
            self.save_contacts()
            print("Contact deleted successfully.")
        else:
            print("Invalid contact index.")

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.view_contacts()
            index = int(input("Enter the index of the contact to edit: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            manager.edit_contact(index, name, phone, email)
        elif choice == '4':
            manager.view_contacts()
            index = int(input("Enter the index of the contact to delete: "))
            manager.delete_contact(index)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()