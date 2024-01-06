from collections import UserDict


class PhoneError(Exception):
    pass


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone):
        if Phone.is_valid(phone):
            super().__init__(phone)
        else:
            raise PhoneError

    @staticmethod   
    def is_valid(phone):

        if len(phone) == 10 and str(phone).isdigit():
            return True
        else:
            return False

        


class Record:
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []

        if not phone == None:
            self.phones.append(Phone(phone))

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i, ph in enumerate(self.phones):
            if ph.value == phone:
                self.phones.pop(i)

    def edit_phone(self, old_phone, new_phone):
        for i, ph in enumerate(self.phones):
            if ph.value == old_phone:
                self.phones[i] =  Phone(new_phone)

    def find_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone:
                return ph

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        for key in self.data:
            if key == name:
                return self.data[key]

    def delete(self, name):
        for key in self.data:
            if key == name:
                return self.data[key]
            
    def __str__(self):
        return str([str(i) for i in self.data.values()])


# if __name__ == '__main__':
#     jane_record = Record('Jane')
#     jane_record.add_phone('2222222222')
#     jane_record.add_phone('1111111111')

#     martin_record = Record("Martin", '1111111111')
#     martin_record.add_phone('8888888888')



#     book = AddressBook()
#     book.add_record(jane_record)
#     book.add_record(martin_record)
#     print(book)
#     print(book.find('Jane'))
