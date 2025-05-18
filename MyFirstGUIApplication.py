import tkinter as tk
import tkinter.messagebox as messagebox

def show_message():
    # messagebox.showinfo("Message","Hello you have clicked the button")
    messagebox.showinfo("Message",textbox.get(1.0, tk.END))

def show_form2():
    form2 = tk.Tk()
    button2 = tk.Button(form2, text="Click ME", command=lambda:form2.destroy())
    button2.pack()

form = tk.Tk()
textbox = tk.Text(form)
textbox.grid(row=0, column=0)

button = tk.Button(form, text="Click Me", command=show_message)
button.grid(row=1, column=0)

button2 = tk.Button(form, text="Open form 2", command=show_form2)
button2.grid(row=1,column=1)

form.mainloop() # is used only for first window