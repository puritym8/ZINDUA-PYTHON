class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactsList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def update_contact(self, name, new_phone_number, new_email):
        contact = self.search_contact(name)
        if contact:
            contact.phone_number = new_phone_number
            contact.email = new_email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts found.")

def main():
    contacts_list = ContactsList()
    
    while True:
        print("\nChoose an option:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Display all contacts")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            contact = Contact(name, phone_number, email)
            contacts_list.add_contact(contact)
        elif choice == '2':
            name = input("Enter contact name to search: ")
            contact = contacts_list.search_contact(name)
            if contact:
                print(f"Contact found - Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
            else:
                print("Contact not found.")
        elif choice == '3':
            name = input("Enter contact name to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            contacts_list.update_contact(name, new_phone_number, new_email)
        elif choice == '4':
            name = input("Enter contact name to delete: ")
            contacts_list.delete_contact(name)
        elif choice == '5':
            contacts_list.display_all_contacts()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
