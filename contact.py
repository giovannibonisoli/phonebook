class Contact:
    """
    Class to represent a contact of the PhoneBook
    """

    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone

    def to_dict(self):
        """
        Return contact info in a dictionary
        """
        return {
                    "name": self.name,
                    "surname": self.surname,
                    "phone": self.phone
                }

    def __repr__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nPhone number: {self.phone}"
