import tkinter as tk
import tkinter.messagebox as messagebox

class MyForm1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        button = tk.Button(self, text="Click Me", command=lambda: self.show_message(button))
        button.pack()
        self.mainloop()

    def show_message(self, button):
        messagebox.showinfo("Message",button["text"])

form1 = MyForm1()
