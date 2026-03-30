import tkinter as tk 

window = tk.Tk()

def validate():
    name = name_entry.get()
    email = email_entry.get()
    raido = level.get()
    # subs = check.get()
    if check.get() == 1:
        sub = "Subscribed"
    else:
        sub = "not sub"

    under = tk.Label(window,text=f"{name}{email}{raido}{sub}")
    under.grid(row=5,column=0)


# loob
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
# labas
file_menu = tk.Menu(menu_bar, tearoff=0)
# gawa
file_menu.add_command(label="Exit")
file_menu.add_command(label="Help")
# tawag
menu_bar.add_cascade(label="File", menu=file_menu)


name = tk.Label(window,text="Name:")
mail = tk.Label(window,text="Email:")
name.grid(row=0,column=0)
mail.grid(row=1,column=0)

name_entry =tk.Entry(window)
name_entry.grid(row=0,column=1)
email_entry =tk.Entry(window)
email_entry.grid(row=1,column=1)

level = tk.StringVar()
gold = tk.Radiobutton(window,
                      text="Gold",
                      value="Gold",
                      variable=level)
Silver = tk.Radiobutton(window,
                      text="Silver",
                      value="Silver",
                      variable=level)
Basic = tk.Radiobutton(window,
                      text="Basic",
                      value="Basic",
                      variable=level)

gold.grid(row=2,column=0)
Silver.grid(row=2,column=1)
Basic.grid(row=2,column=2)

check = tk.IntVar()
sub = tk.Checkbutton(window,text="Subscribe to Newsletter",variable=check)
sub.grid(row=3,column=0)

btn = tk.Button(window,text="Register",command=validate)
btn.grid(row=4,column=0)


window.mainloop()
