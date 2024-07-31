from phonebook import PhoneBook
from utils import is_valid_phone_number

from contact import Contact

def show_main_menu():
    print("\n")
    print("1. Visualize contacts")
    print("2. Contact search")
    print("3. Add new contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Quit")
    print("\n")


def get_menu_option(text, options_number=1):
    try:
        option_number = int(input(text))
        assert option_number in range(1, options_number+1), f"Option {option_number} is not avalaible"
        return option_number

    except ValueError:
        print("Insert a numeric value corresponding to one of the listed options")
        return -1

    except AssertionError as e:
        print(e)
        return -1

def input_phone_number(instruction_text="Insert the phone number: "):
    while True:
        phone = input(instruction_text)
        if phone == "" or is_valid_phone_number(phone):
            return phone
        else:
            print("Invalid number! Respect standard formats for phone numbers:")
            print("123-456-7890")
            print("(123) 456-7890")
            print("123 456 7890")
            print("123.456.7890")
            print("+91 (123) 456-7890\n")


def search_phonebook_contacts(phonebook):

    while True:
        name = input("Insert name (Press Enter to leave empty): ")
        surname = input("Insert surname (Press Enter to leave empty): ")

        if name == "" and surname == "":
            return []
        else:
            return phonebook.find_contacts(name=name or None, surname=surname or None)


def contact_manager():
    print("Welcome to ContactEase Phonebook!")
    phonebook = PhoneBook("")

    while True:
        show_main_menu()
        choice_number = get_menu_option("Choose an option:", options_number=6)
        if choice_number == 1:
            # List al the contacts
            phonebook.visualize_all_contacts()


        elif choice_number == 2:
            # Search contact by name, surname or both
            found_contacts = search_phonebook_contacts(phonebook)
            if len(found_contacts) == 0:
                print("No contacts found!")
            else:
                print("\nCONTACTS FOUND:")
                for i, contact in enumerate(found_contacts):
                    print(i+1)
                    print(contact, "\n")


        elif choice_number == 3:
            # Insert a new contact
            name = input("Insert name (Press Enter to leave empty): ")
            surname = input("Insert surname (Press Enter to leave empty): ")

            if name == "" and surname == "":
                print("No information inserted!")
            else:
                phone = input_phone_number()
                if phone == "":
                    print("No phone number inserted!")
                else:
                    new_contact = Contact(name, surname, phone)
                    phonebook.add_contact(new_contact)
                    print("New contact inserted!")


        elif choice_number == 4:
            # Edit a contact
            found_contacts = search_phonebook_contacts(phonebook)

            if len(found_contacts) == 0:
                print("No contacts matching inserted information!")
            else:
                while True:
                    print("\nHere are the contacts matching inserted information!")
                    for i, contact in enumerate(found_contacts):
                        print(i+1)
                        print(contact, "\n")

                    message_text = "Insert the number of contact you want to modify: "
                    contact_index = get_menu_option(message_text, options_number=len(found_contacts)) - 1

                    name = input("Insert new name (Press enter to leave unchanged): ")
                    surname = input("Insert new surname (Press enter to leave unchanged): ")
                    phone = input_phone_number("Insert new phone number (Press enter to leave unchanged): ")

                    if name == "" and surname == "" and phone == "":
                        print("No information changed!")
                    else:
                        phonebook.edit_contact(found_contacts[contact_index], name, surname, phone)
                        print("Contact changed!")
                    break


        elif choice_number == 5:
            # delete a contact
            found_contacts = search_phonebook_contacts(phonebook)
            if len(found_contacts) == 0:
                print("No contacts matching inserted information!")
            else:
                while True:
                    print("\nHere are the contacts matching inserted information!")
                    for i, contact in enumerate(found_contacts):
                        print(i+1)
                        print(contact)

                    message_text = "Insert the number of contact you want to delete: "
                    contact_index = get_menu_option(message_text, options_number=len(found_contacts)) - 1

                    phonebook.delete_contact(found_contacts[contact_index])
                    print("Deleted contact!")
                    break



        elif choice_number == 6:
            print("Goodbye!")
            break


if __name__ == "__main__":
    contact_manager()
