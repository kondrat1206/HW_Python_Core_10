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


def input_error(func):

    def inner(word_list):

        if func.__name__ != "phone":
            if len(word_list) > 1:
                name = word_list[0]
                phone = word_list[1]
                match = re.fullmatch(r'\+\d{12}', phone)
                if match:
                    result = func(word_list)
                else:
                    result = f"""Entered value \"{phone}\" is not correct.\nPhone must start with \"+\" and must have 12 digits.\nFor example: \"+380681235566\"\n\nTRY AGAIN!!!"""
            else:
                result = f"""Command \"{func.__name__}\" reqired 2 arguments: name and phone.\nFor example: {func.__name__} [name] [phone]\n\nTRY AGAIN!!!"""
        else:
            if len(word_list) > 0:
                name = word_list[0]
                if name in phone_book:
                    result = func(word_list)
                else:
                    result = f"Contact \"{name}\" does not exist in the phone book\n"
            else:
                result = f"""Command \"{func.__name__}\" reqired 1 argument: name.\nFor example: {func.__name__} [name]\n\nTRY AGAIN!!!"""
        return result
    return inner
    

@input_error
def add(word_list):

    name = word_list[0]
    phone = word_list[1]
    phone_book[name] = str(phone)
    result = f"Added new contact \"{name}\" with phone \"{phone}\" to phone book\n"
    return result


@input_error
def change(word_list):

    name = word_list[0]
    if name in phone_book:
        phone = word_list[1]
        phone_book[name] = str(phone)
        result = f"Changed phone for \"{name}\" to new phone \"{phone}\" in the phone book\n"
    else:
        result = f"Contact \"{name}\" does not exist in the phone book\n"
    return result


@input_error
def phone(word_list):

    name = word_list[0]
    phone = phone_book[name]
    result = f"Phone of contact \"{name}\" is \"{phone}\"\n"
    return result


def hello(word_list):

    result = "How can I help you?\n"
    return result


def exit(word_list):

    result = "exit"
    return result


def show_all(word_list):

    result = "All contacts:\n"
    for name, phone in phone_book.items():
        result += f"Name: {name}, Phone: {phone}\n"
    return result


commands = {
    "hello" : hello,
    "exit" : exit,
    "add" : add,
    "change" : change,
    "phone" : phone,
    "show_all" : show_all
}


def parser(string: str):

    word_list = string.split(' ')
    if "hello" in word_list:
        command, word_list = "hello", word_list
    elif ("good" in word_list and "bye" in word_list) or "close" in word_list or "exit" in word_list:
        command, word_list = "exit", word_list
    elif "show" in word_list and "all" in word_list:
        command, word_list = "show_all", word_list
    elif "add" in word_list:
        word_list.remove("add")
        command, word_list = "add", word_list
    elif "change" in word_list:
        word_list.remove("change")
        command, word_list = "change", word_list
    elif "phone" in word_list:
        word_list.remove("phone")
        command, word_list = "phone", word_list
    else:
        command, word_list = None, word_list
    
    return command, word_list


def handler(command):

    return commands[command]


    

def main():

    while True:
        source_command = input("Enter command: ").lower()
        command, word_list = parser(source_command)
        if not command:
            print(f"YOU ENTERED A WRONG COMMAND!!!\n{help}\nTRY AGAIN!!!")
            continue

        result = handler(command)(word_list)
        if result == 'exit':
            print("Good bye!")
            break
        else:
            print(result)


if __name__ == "__main__":
    main()