from classes import AddressBook, Record, Name, Phone


book = AddressBook()
book.add_record("Ivan")
print(book.data)
print(book.data["Ivan"].phones)
book.data["Ivan"].add_phone(11111111)
book.data["Ivan"].add_phone(22222222)
print(book.data["Ivan"].phones)
print(book.data["Ivan"].phones[0].value)
print(book.data["Ivan"].phones[1].value)
book.data["Ivan"].change_phone(33333333, 44444444)
print(book.data["Ivan"].phones[0].value)
print(book.data["Ivan"].phones[1].value)
book.data["Ivan"].change_phone(11111111, 44444444)
print(book.data["Ivan"].phones[0].value)
print(book.data["Ivan"].phones[1].value)
book.data["Ivan"].remove_phone(11111111)
print(book.data["Ivan"].phones)
print(book.data["Ivan"].phones[0].value)
print(book.data["Ivan"].phones[1].value)
book.data["Ivan"].remove_phone(44444444)
print(book.data["Ivan"].phones)
book.data["Ivan"].remove_phone(22222222)
print(book.data["Ivan"].phones)
book.data["Ivan"].remove_phone(22222222)
book.data["Ivan"].change_phone(11111111, 44444444)





