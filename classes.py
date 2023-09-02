from collections import UserDict


class AddressBook(UserDict):
    def __init__(self): 
        self.data = {}

    def add_record(self, record):
        self.record = record
        self.data[self.record.name.value] = self.record
        result = f'Record {self.record.name.value} added to address book'
        print(result)
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
        print(result)
        return result


    def remove_phone(self, phone):
        if len(self.phones) > 0:
            for id, obj in enumerate(self.phones):
                if obj == phone:
                    self.phones.pop(id)
                    result = f'Number {phone.value} remuved from phone list of {self.name.value}'
                    break
                else:
                    result = f'Number {phone.value} is not in the phone list of {self.name.value}'
        else:
            result = f'Contact {self.name.value} does not have any phone number'
        print(result)
        return result
    

    def change_phone(self, phone, new_phone):
        if len(self.phones) > 0:
            for id, obj in enumerate(self.phones):
                if obj == phone:
                    obj = new_phone
                    result = f'Number {phone.value} changed to {new_phone.value} in phone list of {self.name.value}'
                    break
                else:
                    result = f'Number {phone.value} is not in the phone list of {self.name.value}'
        else:
            result = f'Contact {self.name.value} does not have any phone number'
        print(result)
        return result


class Field:
    pass


class Name(Field):
    
    def __init__(self, value):
        self.value = value


class Phone(Field):
    
    def __init__(self, value):
        self.value = value