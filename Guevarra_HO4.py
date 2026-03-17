import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.config(bg="green")
# window.geometry("300x300")
window.resizable(True,True)

def check():
    first = fname.get()
    middle = mname.get()
    last = lname.get()
    ages = int(birth_year.get())
    taon = 2026 - ages



    
    if radio_val.get() == 1: 
        Gender ["text"] = f"Gender: Male"    
        form ["bg"] = "blue"
    elif radio_val.get() == 0: 
        Gender ["text"] = f"Gender: Female"
        window ["bg"] = "pink"


    

    name ["text"] = f"Name: {first} {middle} {last}"
    age ["text"] = f"Age: {taon}"
    # Gender ["text"] = f"Gender: {radio_vals}"
    asn ["text"] = f"You are {taon} Years old"



header = tk.Label(window, text="Profile Builder", font=(16))
header.grid(row=0, column=0)

form = tk.Frame(window,bg="green")
form.grid(row=1,column=0,padx=40)

fname = tk.Entry(form)
mname = tk.Entry(form)
lname = tk.Entry(form)

fname.grid(row=1, column=0)
mname.grid(row=1, column=1)
lname.grid(row=1, column=2)

fname_label = tk.Label(form,text="First Name")
mname_label  = tk.Label(form,text="Middle Name")
lname_label  = tk.Label(form,text="Last Name")
fname_label.grid(row=2, column=0)
mname_label.grid(row=2, column=1)
lname_label.grid(row=2, column=2)


birth_year = tk.Entry(form)
birth_year.grid(row=3, column=0)

birth_year_label = tk.Label(form,text="Birth Year")
birth_year_label.grid(row=4, column=0)

asn = tk.Label(form, text="Calculating the Year.....",font=(16))
asn.grid(row=3, column=2,columnspan=2,rowspan=2)

gender = tk.Label(form,text="Gender")
gender.grid(row=5, column=0)

radio_val = tk.IntVar()
Female = tk.Radiobutton(form,text="Female",value=0,variable=radio_val)
Female.grid(row=5, column=1)

Male = tk.Radiobutton(form,text="Male",value=1,variable=radio_val)
Male.grid(row=5, column=2)






btn = tk.Button(window, command=check,text="Submit")
btn.grid(row=2,column=0)







new_win = tk.Toplevel()


info = tk.Label(new_win,text="Student Info")
info.grid(row=0, column=0)

name = tk.Label(new_win,text="Name:")
age = tk.Label(new_win,text="Age:")
Gender = tk.Label(new_win,text="Gender:")

name.grid(row=1,column=0)
age.grid(row=2,column=0)
Gender.grid(row=3,column=0)
window.mainloop()
