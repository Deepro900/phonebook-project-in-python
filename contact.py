# Contact Manager
contacts = []

def add_contact():
    print("\n--- Add a New Contact ---")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Address": address
    }
    contacts.append(contact)
    print(f"Contact for {name} added successfully!\n")

def view_contacts():
    if not contacts:
        print("\nNo contacts available.\n")
        return

    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"Contact {idx}:")
        for key, value in contact.items():
            print(f"  {key}: {value}")
        print()

