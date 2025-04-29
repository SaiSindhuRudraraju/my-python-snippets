import json

class PhoneBook:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def get_FirstLetter_Of_Name(self):
        return self.name[0].upper()

    def __str__(self):
        return f"Name: {self.name}, Phone Number: {self.phonenumber}"

phonebook_dictionary = dict()

def converter(obj):
    if isinstance(obj, PhoneBook):
        return {
            'name': obj.name,
            'phonenumber': obj.phonenumber
        }

def toobject(dct):
    return PhoneBook(dct['name'], dct['phonenumber'])

def load_phonebook():
    try:
        fp = open('contacts.json', 'r')
        allContacts = fp.readlines()
        for contacts in allContacts:
            contact = json.loads(contacts, object_hook=toobject)
            first_letter = contact.get_FirstLetter_Of_Name()
            if first_letter in phonebook_dictionary:
                phonebook_dictionary[first_letter].append(contact)
            else:
                phonebook_dictionary[first_letter] = [contact]
        fp.close()
        print("Your contacts loaded")
    except FileNotFoundError:
        pass


def add_contact():
    name = input("Enter Name: ")
    phonenumber = input("Enter Phone Number: ")

    contact = PhoneBook(name, phonenumber)

    first_letter = contact.get_FirstLetter_Of_Name()

    if first_letter in phonebook_dictionary.keys():
        phonebook_dictionary[first_letter].append(contact)
    else:
        phonebook_dictionary[first_letter] = [contact]

    fp = open('contacts.json', 'a')
    json_string = json.dumps(contact, default=converter)
    fp.write(json_string + "\n")
    fp.close()

    print(f"Contact added.\n")


def show_contacts():
    if len(phonebook_dictionary) == 0:
        print("Phone book is empty.\n")
        return

    for key in phonebook_dictionary.keys():
        print(f"{key}:")
        index = 1
        for contact in phonebook_dictionary[key]:
            print(f"    Contact {index}:")
            print(f"        Name: {contact.name}")
            print(f"        Phone Number: {contact.phonenumber}")
            index += 1


load_phonebook()


while True:
    print("Do you want to add a new contact or see phone book?")
    choice = input("Enter your choice: Options: Add, Show, No: ").lower()

    if choice == "add":
        add_contact()
    elif choice == "show":
        show_contacts()
    elif choice == "no":
        print("Bye Bye")
        break
    else:
        print("Invalid option, please try again.\n")
        