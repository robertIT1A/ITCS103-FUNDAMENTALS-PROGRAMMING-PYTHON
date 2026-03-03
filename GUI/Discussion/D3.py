import tkinter as pogi

window = pogi.Tk()

window.title("Forms")
window.geometry("600x600")
window.resizable(True,True)
window.config(bg="red")


def submit():
    first = first_name.get()
    last = last_name.get()

    show = pogi.Label(window,text=f"Name:{first} {last}")
    show.pack()


upper = pogi.Frame(window)
upper.pack(pady=10,padx=20)

header = pogi.Label(upper, text="Application Form")
header.pack()

name_input = pogi.Frame(upper)
name_input.pack(pady=5,padx=20)

tname = pogi.Label(name_input, text="Name")
tname.pack()

tfirst_name = pogi.Label(name_input, text="First")
tfirst_name.pack()


first_name = pogi.Text(name_input,height=2)
first_name.pack()


tlast_name = pogi.Label(name_input, text="Last")
tlast_name.pack(pady=5)

last_name = pogi.Text(name_input,height=2)
last_name.pack()


btn = pogi.Button(upper,text="Submit",command=submit)
btn.pack()


window.mainloop()