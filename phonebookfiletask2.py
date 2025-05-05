import pickle
import os

class PhoneBook:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def get_FirstLetter_Of_Name(self):
        return self.name[0].upper()

phonebook_dictionary = dict()

def load_phonebook():
    global phonebook_dictionary
    if os.path.exists("phonebook.txt"):
        with open("phonebook.txt", "rb") as file:
            phonebook_dictionary = pickle.load(file)
    else:
        phonebook_dictionary = {}

def save_phonebook():
    with open("phonebook.txt", "wb") as file:
        pickle.dump(phonebook_dictionary, file)

def add_contact():
    name = input("Enter Name: ")
    phonenumber = input("Enter Phone Number: ")

    contact = PhoneBook(name, phonenumber)
    first_letter = contact.get_FirstLetter_Of_Name()

    if first_letter in phonebook_dictionary:
        phonebook_dictionary[first_letter].append(contact)
    else:
        phonebook_dictionary[first_letter] = [contact]

    print("Contact added.\n")

def show_contacts():
    if not phonebook_dictionary:
        print("Phone book is empty.\n")
        return

    for key in sorted(phonebook_dictionary.keys()):
        print(f"{key}:")
        for index, contact in enumerate(phonebook_dictionary[key], start=1):
            print(f"    Contact {index}:")
            print(f"        Name: {contact.name}")
            print(f"        Phone Number: {contact.phonenumber}")

# Load phonebook at start
load_phonebook()

# Main loop
while True:
    print("\nDo you want to add a new contact or see phone book?")
    choice = input("Enter your choice: Options: Add, Show, No: ").lower()

    if choice == "add":
        add_contact()
    elif choice == "show":
        show_contacts()
    elif choice == "no":
        save_phonebook()
        print("Phone book saved. Bye Bye!")
        break
    else:
        print("Invalid option, please try again.\n")
