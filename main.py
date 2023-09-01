from classes import AddressBook, Record, Name, Phone
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
    if "good bye" in string.lower() or "close" in string.lower() or "exit" in string.lower():
        command, param_list = "exit", ""
        return command, param_list
    elif "show all" in string.lower():
        command, param_list = "show_all", ""
        return command, param_list
    elif "hello" in string.lower():
        command, param_list = "hello", ""
        return command, param_list
    for word in word_list:
        if "add" == word.lower():
            word_list.remove(word)
            command, param_list = "add", word_list
            return command, param_list
        elif "change" == word.lower():
            word_list.remove(word)
            command, param_list = "change", word_list
            return command, param_list
        elif "phone" == word.lower():
            word_list.remove(word)
            command, param_list = "phone", word_list
            return command, param_list
    else:
        command, param_list = None, ""
        return command, param_list


def handler(command):

    return commands[command]


def main():

    while True:
        source_command = input("Enter command: ")
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


