import tkinter as tk

window = tk.Tk()
window.title("Exam")
# window.config(bg="green")
window.resizable(True,True)


# pass shouh 8 character




acc = []
pas = []

acc1 = []
pas1 = []

def regester():
    
    def submit():
        
        user = user_entry.get()
        word = pass_entry.get()
        acc.append(user)
        pas.append(word)
        print(acc, pas)
        now = tk.Label(popup, text="You are now Register")
        now.grid(row=5,column=0,columnspan=3)

        


    def show():
        show = check.get()

        if show == 0:
            pass_entry ["show"] = "*"
        elif show == 1:
            pass_entry ["show"] = ""



    popup = tk.Toplevel(window)
    popup.transient(window)
    popup.config(bg="green")

    head = tk.Label(popup, text="Register")
    head.grid(row=0,column=0,columnspan=3)

    user = tk.Label(popup, text="Username:")
    passw = tk.Label(popup, text="Password:")
    user_entry = tk.Entry(popup)
    pass_entry = tk.Entry(popup,show="*")
    user.grid(row=1,column=0)
    passw.grid(row=2,column=0)
    user_entry.grid(row=1,column=1)
    pass_entry.grid(row=2,column=1)

    check = tk.IntVar()
    shows = tk.Checkbutton(popup,text="Show PassWord",variable=check,onvalue=1,offvalue=0,command=show)
    shows.grid(row=3,column=0)
    btn = tk.Button(popup,text="Register",command=submit)
    btn.grid(row=4,column=0,columnspan=3)

    
def log():
    def ass():
        user = user_entry.get()
        word = pass_entry.get()
        acc1.append(user)
        pas1.append(word)
   

        if acc1 == acc and pas1 == pas:
            cor = tk.Label(popup,text="Access Granted")
            cor.grid(row=5,column=0,columnspan=3)
        elif acc1 != acc or pas1 != pas:
            cor = tk.Label(popup,text="Access Denied")
            cor.grid(row=5,column=0,columnspan=3)
                
        



    def show():
        show = check.get()

        if show == 0:
            pass_entry ["show"] = "*"
        elif show == 1:
            pass_entry ["show"] = ""


    popup = tk.Toplevel(window)
    popup.transient(window)
    popup.config(bg="red")

    head = tk.Label(popup, text="Log in")
    head.grid(row=0,column=0,columnspan=3)

    user = tk.Label(popup, text="Username:")
    passw = tk.Label(popup, text="Password:")
    user_entry = tk.Entry(popup)
    pass_entry = tk.Entry(popup,show="*")
    user.grid(row=1,column=0)
    passw.grid(row=2,column=0)
    user_entry.grid(row=1,column=1)
    pass_entry.grid(row=2,column=1)

    check = tk.IntVar()
    shows = tk.Checkbutton(popup,text="Show PassWord",variable=check,onvalue=1,offvalue=0,command=show)
    shows.grid(row=3,column=0)
    btn = tk.Button(popup,text="Log in",command=ass)
    btn.grid(row=4,column=0,columnspan=3)





welcome = tk.Label(window,text="Welcome!",font=15)
register = tk.Button(window,text="Register",command=regester,bg="blue",font=15)
Log_in = tk.Button(window,text="Log in",command=log,bg="green" ,font=15)

welcome.pack()
register.pack(ipadx=22)
Log_in.pack(ipadx=30)


window.mainloop()

