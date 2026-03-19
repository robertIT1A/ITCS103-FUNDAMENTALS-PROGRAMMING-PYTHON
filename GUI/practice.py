import tkinter as tk

window = tk.Tk()

window.title("Enrollment Form")
# window.geometry("500x500")
window.resizable(True,True)

header =tk.Label(window, text="Enrollment Form",
                 font=(25))
header.grid(row=0, column=0,columnspan=3,pady=10)


form = tk.Frame(window)
form.grid(row=1,column=0,columnspan=3)

name = tk.Label(form,text="Name",font=(15))
name.grid(row=0,column=0)

Adress = tk.Label(form,text="Adress",font=(15))
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
var = tk.IntVar()
Male = tk.Radiobutton(form,text="Male",
                      value="Male",
                      variable=var)
Male.grid(row=1,column=2)

Female = tk.Radiobutton(form,text="Female",
                      value="Female",
                      variable=var)
Female.grid(row=1,column=3)

submit = tk.Button(form,text="Submit")
submit.grid(row=2,column=2,columnspan=2,rowspan=2)



# new window

popup = tk.Toplevel(window)
popup.transient(window)
window.mainloop()