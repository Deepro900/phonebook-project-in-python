from contact import contacts

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