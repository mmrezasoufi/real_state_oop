from base import BaseClass


class User(BaseClass):

    def __init__(self, firstname, lastname, phone_number, *args, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
