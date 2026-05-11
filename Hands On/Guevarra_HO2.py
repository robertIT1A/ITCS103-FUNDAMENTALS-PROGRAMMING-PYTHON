import tkinter as pogi

window = pogi.Tk()

window.title("Roberto Guevarra's Profile")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg="#A020F0")


def profile():
    title = pogi.Label(window,text="Student Profile",
                    font=("Poppins",55),
                    bg="#A020F0",
                    fg="#D4AF37",
                    anchor="center")
    title.pack(pady=50)

    name = pogi.Label(window,text="Name : Roberto B. Guevarra Jr",
                    font=("Poppins",25),
                    bg="#A020F0",
                    fg="#E6B410",
                    anchor="w",width=100)
    name.pack(pady=10)

    age = pogi.Label(window,text="Age : 19 years old",
                    font=("Poppins",25),
                    bg="#A020F0",
                    fg="#E6B410",
                    anchor="w",width=100)
    age.pack(pady=10)

    course = pogi.Label(window,text="Course : BSIT",
                    font=("Poppins",25),
                    bg="#A020F0",
                    fg="#E6B410",
                    anchor="w",width=100)
    course.pack(pady=10)

    Birthday = pogi.Label(window,text="Birthday : August 2 2006",
                    font=("Poppins",25),
                    bg="#A020F0",
                    fg="#E6B410",
                    anchor="w",width=100)
    Birthday.pack(pady=10)

    Motto = pogi.Label(window,text="Motto : Think First before you Click",
                    font=("Poppins",25),
                    bg="#A020F0",
                    fg="#E6B410",
                    anchor="w",width=100)
    Motto.pack(pady=10)


    btn.pack_forget()


btn = pogi.Button(window,
                  text = "Click if you want to know Me!", command=profile,bg="#E6B410",
                    fg="#1A1A1A", )
btn.pack(pady=200)
window.mainloop()
