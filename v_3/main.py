from collections import UserDict
import re
import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def __init__(self, phone):
        super().__init__(phone)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        Phone.is_valid(new_value)
        self._value = new_value

    @staticmethod   
    def is_valid(phone):

        if not len(phone) == 10:
            raise ValueError
        
        for i in phone:
            if not i.isdigit():
                raise ValueError
            


class Birthday(Field):
    def __init__(self, birthday):
        super().__init__(birthday)

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        Birthday.is_valid(new_value)
        self._value = new_value


    @staticmethod
    def is_valid(birthday):
        
        if birthday == None:
            return 
        else:
            pattern = r'\d{2}-\d{2}-\d{4}\b'
            if re.match(pattern, birthday) != None:
                return 
            
        raise ValueError

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday)
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


    def days_to_birthday(self):
        birthday = self.birthday.value
        date_now = datetime.datetime.now().date()
        lst_n = str(date_now).split("-")
        lst_b = birthday.split("-")
        date_b = datetime.date(int(lst_n[0]), int(lst_b[1]), int(lst_b[0]))
        diff = date_b - date_now
        return f'{str(diff).split(" ")[0]} days'

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def __iter__(self, n=5):
        data_values = list(self.data.values())
        for i in range(0, len(data_values), n):
            yield data_values[i:i+1]

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
