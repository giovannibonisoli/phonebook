import os

from utils import read_json, write_json, file_exists
from contact import Contact

class PhoneBook:
    """
    Class to implement the phonebook
    """

    def __init__(self, path):
        self.file_path = os.path.join(path, "contacts.json")
        if not file_exists(self.file_path):
            write_json(self.file_path, [])

        self.contacts = self.load_contacts()


    def load_contacts(self):
        """
        Load contacts from JSON
        """
        dict_contacts = read_json(self.file_path)
        return [Contact(contact["name"], contact["surname"], contact["phone"]) for contact in dict_contacts]


    def save_contacts(self):
        """
        Save contacts in the JSON
        """
        write_json(self.file_path, [contact.to_dict() for contact in self.contacts])


    def add_contact(self, new_contact):
        """
        Add a new contact
        """
        self.contacts.append(new_contact)
        self.save_contacts()


    def edit_contact(self, old_contact, name, surname, phone):
        """
        Edit the selected contact
        """

        new_name = old_contact.name if name == "" else name
        new_surname = old_contact.surname if surname == "" else surname
        new_phone = old_contact.phone if phone == "" else phone

        index = self.contacts.index(old_contact)
        self.contacts[index] = Contact(new_name, new_surname, new_phone)
        self.save_contacts()


    def delete_contact(self, contact):
        """
        Delete the selected contact
        """

        self.contacts.remove(contact)
        self.save_contacts()


    def find_contacts(self, name=None, surname=None):
        """
        Find contact by name, surname or both
        """
        matching_contacts = []
        for contact in self.contacts:
            if name and surname:
                if name == contact.name and surname == contact.surname:
                    matching_contacts.append(contact)

            elif name:
                if name == contact.name:
                    matching_contacts.append(contact)

            elif surname:
                if surname == contact.surname:
                    matching_contacts.append(contact)

        return matching_contacts


    def visualize_all_contacts(self):
        """
        Visualize all the contacts in the phonebook
        """
        print("CONTACT LIST")

        if len(self.contacts) == 0:
            print("Empty")
        else:
            for i, contact in enumerate(self.contacts):
                print(i+1)
                print(contact)
                print("\n")


    def __repr__(self):
        return f"Phonebook saved in \"{os.path.abspath(self.file_path)}\""


if __name__ == "__main__":
    phonebook = PhoneBook("")
    print(phonebook)
    phonebook.add_new_contact(Contact("Mario", "Rossi", "3489843320"))
    phonebook.add_new_contact(Contact("Alice", "Bianchi", "3392478495"))
    phonebook.visualize_all_contacts()
