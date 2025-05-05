import json

class PhoneBook:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def get_FirstLetter_Of_Name(self):
        return self.name[0].upper()

phonebook_dictionary = dict()

def add_contact():

    name = input("Enter Name: ")
    phonenumber = input("Enter Phone Number: ")

    contact = PhoneBook(name, phonenumber)

    first_letter = contact.get_FirstLetter_Of_Name()

    if first_letter in phonebook_dictionary.keys():
        phonebook_dictionary[first_letter].append(contact)
    else:
        phonebook_dictionary[first_letter] = [contact]

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

def converter(obj):
    if isinstance(obj, PhoneBook):
        return {
            "name": obj.name,
            "phonenumber": obj.phonenumber
        }

def save_dictObject():
    fp =  open('phonebook.txt', 'w')
    json.dump(phonebook_dictionary, fp, default=converter)
    fp.close()

def toPhonebookObject(dct):
    #print(dct)
    if 'name' in dct and 'phonenumber' in dct:
        return PhoneBook(dct['name'], dct['phonenumber'])
    return dct

def load():
    try:
        fp = open('phonebook.txt', 'r')
        existingcontacts = json.load(fp, object_hook=toPhonebookObject)

        for key, contacts in existingcontacts.items():
            phonebook_dictionary[key] = contacts

        print("Phone book loaded successfully.")

    except FileNotFoundError:
        print("No contacts till now. Please add your contacts.")

load()

while True:
    print("Do you want to add a new contact or see phone book?")
    choice = input("Enter your choice: Options: Add, Show, No: ").lower()

    if choice == "add":
        add_contact()
    elif choice == "show":
        show_contacts()
    elif choice == "no":
        save_dictObject()
        print("Bye Bye")
        break
    else:
        print("Invalid option, please try again.\n")




'''

#commented

#load_dictObject()
def load_dictObject():
    try:
        with open('phonebook.txt', 'r') as fp:
            data = json.load(fp)
            for key, contacts in data.items():
                for contact_data in contacts:
                    contact = PhoneBook(contact_data['name'], contact_data['phonenumber'])
                    if key in phonebook_dictionary:
                        phonebook_dictionary[key].append(contact)
                    else:
                        phonebook_dictionary[key] = [contact]
        print("Phone book loaded successfully.")
    except FileNotFoundError:
        print("No contacts till now. Please add your contacts.")

def loadtest():
    try:
        fp =  open('phonebook.txt', 'r')
        existingcontacts =  json.load(fp)
        #print(existingcontacts)
        #print("*************")
        #print(existingcontacts.items())

        for key, contacts in existingcontacts.items():
            print(key)
            print(" : ")
            print(contacts)

            listofcontacts = []
            for contact in contacts:
                listofcontacts.append(PhoneBook(contact['name'], contact['phonenumber']))
                
            phonebook_dictionary[key] = listofcontacts

            print("***")
        print("Phone book loaded successfully.")

    except FileNotFoundError:
        print("No contacts till now. Please add your contacts.")
'''