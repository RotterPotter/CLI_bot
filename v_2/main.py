from collections import UserDict


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
            raise ValueError

    @staticmethod   
    def is_valid(phone):

        if not len(phone) == 10:
            return False
        
        for i in phone:
            if not i.isdigit():
                return False
            
        return True


        
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
                return
            
        raise ValueError
    
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
                del self.data[key]
                return 
            
    def __str__(self):
        return str([str(i) for i in self.data.values()])
