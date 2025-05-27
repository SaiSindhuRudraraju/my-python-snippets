import tkinter as tk
import tkinter.messagebox as messagebox
'''
def show_message():
    #messagebox.showinfo("index", listbox.curselection())
    messagebox.showinfo("Message", listbox.get(listbox.curselection()))
'''

def show_message():
    for item in listbox.curselection():
        selected_item = listbox.get(item)
        messagebox.showinfo("Message", selected_item)
        
root = tk.Tk()
root.title("Listbox with Scrollbar")

# Frame to hold listbox and scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=10)
#listbox.config(selectmode=tk.SINGLE)    #Single selection mode
listbox.config(selectmode=tk.MULTIPLE)    #Multiple selection mode
listbox.bind('<<ListboxSelect>>', lambda event: show_message()) #Bind selection event
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Configure scrollbar to control listbox
scrollbar.config(command=listbox.yview)

# Insert sample items
for i in range(100):
    listbox.insert(tk.END, f"Item {i+1}")

root.mainloop()