class Contact:
    """
    Class to represent a contact of the PhoneBook
    """

    def __init__(self, name, surname, phone):
        self._name = name
        self._surname = surname
        self._phone = phone

    def get_name(self):
        """
        Return contact's name
        """
        return self._name

    def get_surname(self):
        """
        Return contact's surname
        """
        return self._surname

    def get_phone(self):
        """
        Return contact's phone number
        """
        return self._phone

    def set_name(self, name):
        """
        Modify contact's name
        """
        self._name = name

    def set_surname(self, surname):
        """
        Modify contact's surname
        """
        self._surname = surname

    def set_phone(self, phone):
        """
        Modify contact's phone number
        """
        self._phone = phone

    def to_dict(self):
        """
        Return contact info in a dictionary
        """
        return {
                    "name": self._name,
                    "surname": self._surname,
                    "phone": self._phone
                }

    def __repr__(self):
        return f"Name: {self._name}\nSurname: {self._surname}\nPhone number: {self._phone}"
