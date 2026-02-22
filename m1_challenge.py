contacts = []


def add_contact(name, number):
    contacts.append({"name": name, "number": number, "favorite": False})
    print(f"{name} has been added to your contacts.")


def view_contacts(contacts):
    if not contacts:
        print("\nYour contact list is empty.")
        return
    print("\nYour Contacts:")
    for index, contact in enumerate(contacts, start=1):
        status = "Favorite" if contact["favorite"] else "Not Favorite"
        print(f"{index}. {contact['name']} - {contact['number']} ({status})")


def edit_contact(contacts):
    view_contacts(contacts)
    name = input("Enter the index of the contact you want to edit: ")
    try:
        index = int(name) - 1
        if 0 <= index < len(contacts):
            new_name = input("Enter new name: ")
            new_number = input("Enter new number: ")
            contacts[index]["name"] = new_name
            contacts[index]["number"] = new_number
            print(f"\n{contacts[index]['name']} has been updated.")
        else:
            print("Invalid index. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def set_favorite(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    name = input("\nEnter the index of the contact you want to set as favorite: ")
    index = int(name) - 1
    if 0 <= index < len(contacts):
        contacts[index]["favorite"] = True
        print(f"{contacts[index]['name']} has been set as favorite.")
    else:
        print("Invalid index. Please try again.")


def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    name = input("Enter the index of the contact you want to delete: ")
    index = int(name) - 1
    if 0 <= index < len(contacts):
        deleted_contact = contacts.pop(index)
        print(f"{deleted_contact['name']} has been deleted from your contacts.")
    else:
        print("Invalid index. Please try again.")


while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Set as Favorite")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter contact number: ")
        add_contact(name, phone)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        edit_contact(contacts)
    elif choice == "4":
        set_favorite(contacts)
    elif choice == "5":
        delete_contact(contacts)
    elif choice == "6":
        print("Exiting Program")
        break
    else:
        print("Invalid choice. Please try again.")
