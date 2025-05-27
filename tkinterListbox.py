import tkinter
import tkinter.messagebox as messagebox
from tkinter import Listbox, Scrollbar, Entry, Button, Tk, END

form = Tk()
form.geometry("300x200")

listbox = Listbox(form)
listbox.grid(row=1, column=0)
listbox.config(width=20,height=6)
listbox.insert(0,"C")
listbox.insert(1,"C++")
listbox.insert(2,"C#")
listbox.insert(3,"Java")
listbox.insert(4,"Python")
listbox.insert(5,"Javascript")
listbox.insert(6,"Ruby")
listbox.insert(7,"PHP")

scrollbar = Scrollbar(form)
scrollbar.grid(row=1, column=1, sticky='ns')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

form.mainloop()