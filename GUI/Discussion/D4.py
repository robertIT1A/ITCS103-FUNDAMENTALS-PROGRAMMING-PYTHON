import tkinter as tk

window = tk.Tk()

window.title("My Grid")
# window.geometry("500x500")
# window.resizable(True,True)
# window.config(bg="red")

info = tk.Label(window,text="User Information")
name = tk.Label(window,text="Name")
nEntry = tk.Entry(window)
Age = tk.Label(window,text="Age")
aEntry = tk.Entry(window)

info.grid(row=0, column=0,columnspan=3)
name.grid(row=1,column=0)
nEntry.grid(row=1, column=1,columnspan=2)
Age.grid(row=2, column=0)
aEntry.grid(row=2, column=1,columnspan=2)

tk.mainloop()
