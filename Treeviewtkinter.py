import tkinter as tk
from tkinter import ttk
import json

class PhoneBook:
    def __init__(self, name, phonenumber):
        self.name = name
        self.phonenumber = phonenumber

    def get_FirstLetter_Of_Name(self):
        return self.name[0].upper()

phonebook_dictionary = dict()

def converter(obj):
    if isinstance(obj, PhoneBook):
        return {
            "name": obj.name,
            "phonenumber": obj.phonenumber
        }

def toPhonebookObject(dct):
    if 'name' in dct and 'phonenumber' in dct:
        return PhoneBook(dct['name'], dct['phonenumber'])
    return dct

def save_dictObject():
    with open('phonebook.txt', 'w') as fp:
        json.dump(phonebook_dictionary, fp, default=converter)

def load():
    try:
        with open('phonebook.txt', 'r') as fp:
            existingcontacts = json.load(fp, object_hook=toPhonebookObject)
            for key, contacts in existingcontacts.items():
                phonebook_dictionary[key] = contacts
    except FileNotFoundError:
        pass


def add_contact_gui():
    name = name_entry.get()
    phonenumber = phone_entry.get()

    if not name or not phonenumber:
        return

    contact = PhoneBook(name, phonenumber)
    first_letter = contact.get_FirstLetter_Of_Name()

    if first_letter in phonebook_dictionary:
        phonebook_dictionary[first_letter].append(contact)
    else:
        phonebook_dictionary[first_letter] = [contact]

    update_treeview()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def update_treeview():
    treeview.delete(*treeview.get_children())

    for key in sorted(phonebook_dictionary.keys()):
        parent = treeview.insert("", "end", text=key)
        for contact in phonebook_dictionary[key]:
            treeview.insert(parent, "end", text=f"{contact.name} - {contact.phonenumber}")

def on_closing():
    save_dictObject()
    root.destroy()

load()

root = tk.Tk()
root.title("Phone Book")

tk.Label(root, text="Name:").pack(pady=(10, 0))
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone Number:").pack(pady=(5, 0))
phone_entry = tk.Entry(root)
phone_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact_gui)
add_button.pack(pady=10)

treeview = ttk.Treeview(root)
treeview.pack(pady=10, fill=tk.BOTH, expand=True)

update_treeview()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()