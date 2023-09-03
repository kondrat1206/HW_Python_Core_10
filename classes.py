from collections import UserDict


class AddressBook(UserDict):
    
    def __init__(self): 
        self.data = {}

    def add_record(self, record):

        self.record = record
        self.data[self.record.name.value] = self.record
        result = f'Record {self.record.name.value} added to address book'
        
        return result


class Record:

    def __init__(self, name, phone=None): 
        self.name = name
        self.phones = []
        if phone != None:
            self.phones.append(phone)


    def add_phone(self, phone):

        self.phones.append(phone)
        result = f'Number {phone.value} added to phone list of {self.name.value}'

        return result


    def remove_phone(self, phone):
        
        phone_num = phone.value
        for id, obj in enumerate(self.phones):
            if obj == phone:
                self.phones.pop(id)
                result = f'Number {phone_num} remuved from phone list of {self.name.value}'
                break
                
        return result
    

    def change_phone(self, old_phone, new_phone):

        old_num = old_phone.value
        new_num = new_phone.value
        old_phone.value = new_phone.value
        result = f'Number {old_num} changed to {new_num} in phone list of {self.name.value}\n'
                   
        return result


class Field:
    pass


class Name(Field):
    
    def __init__(self, value):
        self.value = value


class Phone(Field):
    
    def __init__(self, value):
        self.value = value