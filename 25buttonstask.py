import tkinter as tk
import tkinter.messagebox as messagebox

class MyForm1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")

        btnNum = 1
        for i in range(5): 
            for j in range(5):

                btn = tk.Button(self, text=str(btnNum))
                btn.config(command=lambda b=btn: self.show_message(b))
                btn.grid(row=i, column=j)
                btnNum += 1
        
        self.mainloop()

    def show_message(self, button):
        messagebox.showinfo("Message", button["text"])

form1 = MyForm1()
