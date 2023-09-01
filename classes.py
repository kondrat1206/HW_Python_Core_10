from collections import UserDict


class AddressBook(UserDict):
    def __init__(self): 
        self.data = {}

    def add_record(self, name):
        self.record = Record(name)
        self.data[self.record.name.value] = self.record
        result = f'Record {self.record.name.value} added to address book'
        print(result)
        return result


class Record:
    def __init__(self, name): 
        self.name = Name(name)
        self.phones = []


    def add_phone(self, value):
        self.phones.append(Phone(value))
        result = f'Number {value} added to phone list of {self.name.value}'
        print(result)
        return result


    def remove_phone(self, value):
        if len(self.phones) > 0:
            for id, obj in enumerate(self.phones):
                if obj.value == value:
                    self.phones.pop(id)
                    result = f'Number {value} remuved from phone list of {self.name.value}'
                    break
                else:
                    result = f'Number {value} is not in the phone list of {self.name.value}'
        else:
            result = f'Contact {self.name.value} does not have any phone number'
        print(result)
        return result
    

    def change_phone(self, value, new_value):
        if len(self.phones) > 0:
            for id, obj in enumerate(self.phones):
                if obj.value == value:
                    obj.value = new_value
                    result = f'Number {value} changed to {new_value} in phone list of {self.name.value}'
                    break
                else:
                    result = f'Number {value} is not in the phone list of {self.name.value}'
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