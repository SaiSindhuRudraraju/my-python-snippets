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