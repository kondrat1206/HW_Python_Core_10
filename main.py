from classes import AddressBook, Record, Name, Phone
import functools
import re

help = """
Available commands:
hello : print \"How can I help you?\"
add [name] [phone] : Add a new record to contact list
change [name] [phone] : Change phone num in contact list
phone [name] : Show phone of user
show all : Show contact list
good bye, close, exit : print \"Good bye!\" and exit
"""


phone_book = {}
address_book = AddressBook()

def input_error(func):

    @functools.wraps(func)
    def inner(param_list):

        if func.__name__ == "phone":
            if len(param_list) > 0:
                name = param_list[0]
                if name in phone_book:
                    result = func(param_list)
                else:
                    result = f"Contact \"{name}\" does not exist in the phone book\n"
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 argument: name.\nFor example: {func.__name__} [name]\n\nTRY AGAIN!!!"""

        elif func.__name__ == "add":
            contact_list = []
            for key in address_book.keys():
                contact_list.append(key)
            if len(param_list) > 0:
                if len(param_list) == 1:
                    name = param_list[0]
                    if name in contact_list:
                        result = f"Contact \"{name}\" already exists in address book"
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
        
        else:
            if len(param_list) > 1:
                name = param_list[0]
                phone = param_list[1]
                match = re.fullmatch(r'\+\d{12}', phone)
                if match:
                    result = func(param_list)
                else:
                    result = f"""Entered value \"{phone}\" is not correct.\nPhone must start with \"+\" and must have 12 digits.\nFor example: \"+380681235566\"\n\nTRY AGAIN!!!"""
            else:
                result = f"""Command \"{func.__name__}\" reqired 2 arguments: name and phone.\nFor example: {func.__name__} [name] [phone]\n\nTRY AGAIN!!!"""
        
        return result
    return inner
    

@input_error
def add(param_list):
    if len(param_list) == 1:
        name = Name(param_list[0])
        phone = None
        address_book.add_record(Record(name, phone))
        result = f"Added new contact \"{name.value}\" without phones to phone book\n"
    elif len(param_list) > 1:
        name = Name(param_list[0])
        phone = Phone(param_list[1])
        address_book.add_record(Record(name, phone))
        result = f"Added new contact \"{name.value}\" with phone \"{phone.value}\" to phone book\n"
    
    return result


@input_error
def change(param_list):

    name = param_list[0]
    if name in phone_book:
        phone = param_list[1]
        phone_book[name] = str(phone)
        result = f"Changed phone for \"{name}\" to new phone \"{phone}\" in the phone book\n"
    else:
        result = f"Contact \"{name}\" does not exist in the phone book\n"
    return result


@input_error
def phone(param_list):

    name = param_list[0]
    phone = phone_book[name]
    result = f"Phone of contact \"{name}\" is \"{phone}\"\n"
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


