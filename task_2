def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    with open("contacts.txt", "a") as file:
        file.write(f"{name}:{phone}\n")
    print("Contact saved!\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
            else:
                print("\nSaved Contacts:")
                for line in contacts:
                    name, phone = line.strip().split(":")
                    print(f"Name: {name}, Phone: {phone}")
                print()
    except FileNotFoundError:
        print("No contacts file found. Add a contact first.\n")


def main():
    while True:
        print("=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
