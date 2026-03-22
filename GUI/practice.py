import tkinter as tk
import json
import random

window = tk.Tk()

window.title("Enrollment Form")
# window.geometry("500x500")
window.resizable(True,True)


def show():
    popup = tk.Toplevel(window)
    popup.transient(window)
    name = name_entry.get()
    adress = address_entry.get()
    Contact = Contact_entry.get()
    dob = DoB_entry.get()
    Var = var.get()
    student_list = [name, adress, Contact, dob, Var]
    num =  random.randint(1,10000)



    info = tk.Label(popup,text="Student Information")
    info.grid(row=0,column=0,columnspan=3)
    name = tk.Label(popup,text=f"Name: {name}")
    name.grid(row=1,column=0)
    adress = tk.Label(popup,text=f"Address: {adress}")
    adress.grid(row=2,column=0)
    Contact = tk.Label(popup,text=f"Contact: {Contact}")
    Contact.grid(row=3,column=0)
    dob = tk.Label(popup,text=f"Date of Birth: {dob}")
    dob.grid(row=4,column=0)
    Var = tk.Label(popup,text=f"Gender: {Var}")
    Var.grid(row=5,column=0)

    with open(f'student_record{num}.json','w') as new_file:
        json.dump(student_list, new_file, indent=4)








header =tk.Label(window, text="Enrollment Form",
                 font=(25))
header.grid(row=0, column=0,columnspan=3,pady=10)


form = tk.Frame(window)
form.grid(row=1,column=0,columnspan=3)

name = tk.Label(form,text="Name",font=(15))
name.grid(row=0,column=0)

Adress = tk.Label(form,text="Address",font=(15))
Adress.grid(row=1,column=0)

name_entry = tk.Entry(form)
address_entry = tk.Entry(form)

name_entry.grid(row=0,column=1)
address_entry.grid(row=1,column=1)


Contact = tk.Label(form,text="Contact",font=(15))
Contact.grid(row=2,column=0)

DoB = tk.Label(form,text="Date of Birth")
DoB.grid(row=3,column=0)

Contact_entry = tk.Entry(form)
DoB_entry = tk.Entry(form)

Contact_entry.grid(row=2,column=1)
DoB_entry.grid(row=3,column=1)

gender = tk.Label(form,text="Gender")
gender.grid(row=0, column=2,columnspan=2)
var = tk.StringVar()
Male = tk.Radiobutton(form,text="Male",
                      value="Male",
                      variable=var)
Male.grid(row=1,column=2)

Female = tk.Radiobutton(form,text="Female",
                      value="Female",
                      variable=var)
Female.grid(row=1,column=3)

submit = tk.Button(form,text="Submit",command=show)
submit.grid(row=2,column=2,columnspan=2,rowspan=2)



# memu

menu_bar = tk.Menu(window) # menu variable
window.config(menu=menu_bar) # lalagay mo sa window config
file_menu = tk.Menu(menu_bar, tearoff=1) # para pagpinindot ito lalabas

file_menu.add_command(label="Open") # para sa mga lalabas
menu_bar.add_cascade(label="File", menu=file_menu) # to show

window.mainloop()
