from classes import AddressBook, Record, Name, Phone
import functools
import re

help = """
Available commands:
hello : print \"How can I help you?\"
add [name] [phone] : Add a new record to address book or new phone to contact phone list
change [name] [old_phone] [new_phone] : Change phone num for contact in address book
phone [name] : Show phone list of contact
show all : Show address book
good bye, close, exit : print \"Good bye!\" and exit
"""


address_book = AddressBook()

def is_contact_exist(name):
    contact_list = []
    for key in address_book.keys():
        contact_list.append(key)
    if name in contact_list:
        result = True
    else:
        result = False
    
    return result


def is_phone_exist(name, phone):
    phone_list = address_book[name].phones
    phone_values = []
    for number in phone_list:
        phone_values.append(number.value)
    if phone in phone_values:
        result = True
    else:
        result = False
    
    return result




def input_error(func):

    @functools.wraps(func)
    def inner(param_list):

        if func.__name__ == "phone":
            if len(param_list) > 0:
                name = param_list[0]
                if is_contact_exist(name):
                    result = func(param_list)
                else:
                    result = f"Contact \"{name}\" does not exist in the address book\n"
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 argument: name.\nFor example: {func.__name__} [name]\n\nTRY AGAIN!!!"""

        elif func.__name__ == "add":
            if len(param_list) > 0:
                if len(param_list) == 1:
                    name = param_list[0]
                    is_con_exist = is_contact_exist(name)
                    if is_con_exist:
                        result = f"Contact \"{name}\" already exists in address book\n"
                    else:
                        result = func(param_list)
                elif len(param_list) > 1:
                    name = param_list[0]
                    phone = param_list[1]
                    match = re.fullmatch(r'\+\d{12}', phone)
                    if match:
                        result = func(param_list)
                    else:
                        result = f"""Entered value \"{phone}\" is not correct.\nPhone must start with \"+\" and must have 12 digits.\nFor example: \"+380681235566\"\n\nTRY AGAIN!!!"""
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 or 2 arguments: name and phone.\nFor example: {func.__name__} [name] - To add a new contact without phones\nFor example: {func.__name__} [name] [phone] - To add a new contact with phones, or add new phone to contact\n\nTRY AGAIN!!!"""
        
        elif func.__name__ == "change":
            if len(param_list) > 2:
                name = param_list[0]
                is_con_exist = is_contact_exist(name)
                if is_con_exist:
                    old_phone = param_list[1]
                    is_ph_exist = is_phone_exist(name, old_phone)
                    if is_ph_exist:
                        new_phone = param_list[2]
                        match = re.fullmatch(r'\+\d{12}', new_phone)
                        if match:
                            result = func(param_list)
                        else:
                            result = f"""Entered value \"{new_phone}\" is not correct.\nPhone must start with \"+\" and must have 12 digits.\nFor example: \"+380681235566\"\n\nTRY AGAIN!!!"""
                    else:
                        result = f"Phone \"{old_phone}\" does not exist in the phone list of contact \"{name}\"\n"  
                else:
                    result = f"Contact \"{name}\" does not exist in the address book\n"
            else:
                result = f"""Command \"{func.__name__}\" reqired 3 arguments: name, phone and new_phone.\nFor example: {func.__name__} [name] [phone] [new_phone]\n\nTRY AGAIN!!!"""
        
        return result
    return inner
    

@input_error
def add(param_list):
    if len(param_list) == 1:
        name = Name(param_list[0])
        phone = None
        address_book.add_record(Record(name, phone))
        result = f"Added new contact \"{name.value}\" without phones to address book\n"
    elif len(param_list) > 1:
        name = Name(param_list[0])
        phone = Phone(param_list[1])
        is_cont_exist = is_contact_exist(name.value)
        if not is_cont_exist:
            address_book.add_record(Record(name, phone))
            result = f"Added new contact \"{name.value}\" with phone \"{phone.value}\" to address book\n"
        else:
            is_ph_exist = is_phone_exist(name.value, phone.value)
            if not is_ph_exist:
                address_book[name.value].add_phone(phone)
                result = f"Added new phone \"{phone.value}\" to contact \"{name.value}\"\n"
            else:
                result = f"Phone \"{phone.value}\" already exists into the contact \"{name.value}\"\n"

    
    return result


@input_error
def change(param_list):
    

    name_str = param_list[0]
    phone_str = param_list[1]
    new_phone_str = param_list[2]
    new_phone_obj = Phone(new_phone_str)
    record = address_book[name_str]
    phone_list = record.phones
    for obj in phone_list:
        if obj.value == phone_str:
            phone_obj = obj
            result = record.change_phone(phone_obj, new_phone_obj)
            break
    
    return result


@input_error
def phone(param_list):

    name = param_list[0]
    phone_list = address_book[name].phones
    value_list = []
    for phone_obj in phone_list:
        value_list.append(phone_obj.value)
    result = f"Phone list of contact \"{name}\" is \"{value_list}\"\n"
    return result


def hello(param_list):

    result = "How can I help you?\n"
    return result


def exit(param_list):

    result = "exit"
    return result


def show_all(param_list):

    result = "All contacts:\n"
    for name, record in address_book.data.items():
        phones = record.phones
        phone_values = []
        for phone in phones:
            phone_values.append(phone.value)
        
        result += f"Name: {name}, Phones: {phone_values}\n"
    return result


commands = {
        "good bye": exit,
        "close": exit,
        "exit": exit,
        "show all": show_all,
        "show_all": show_all,
        "hello": hello,
        "add": add,
        "change": change,
        "phone": phone,
    }


def parser(string: str):

    lower_string = string.lower()
    for keyword, command in commands.items():
        if keyword in lower_string:
            param_list = string.split()
            for param in param_list:
                if param.lower() in keyword:
                    param_list.remove(param)
                    command = command.__name__
            return command, param_list

    return None, ""


def handler(command):
    return commands[command]


def main():

    while True:
        source_command = input("Enter command: ")
        command, param_list = parser(source_command)
        if not command:
            print(f"YOU ENTERED A WRONG COMMAND!!!\n{help}\nTRY AGAIN!!!")
            continue

        result = handler(command)(param_list)
        if result == 'exit':
            print("Good bye!")
            break
        else:
            print(result)


if __name__ == "__main__":
    main()


