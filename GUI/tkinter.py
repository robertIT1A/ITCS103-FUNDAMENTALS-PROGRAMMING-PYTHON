import tkinter as gui

window = gui.Tk()

window.title("My First GUI") #Name 
window.geometry("1000x500") # prio size (wxh)
window.resizable(True,True) #adjust size True para ma adjust
window.configure(bg="red") #background color


# for label and text
label = gui.Label(window,text="Love",
                  font=("Poppins",35,"bold"),
                  bg="blue",
                  fg="white",
                  anchor="center")
label.pack(padx="10",pady="20")


# user input text
textbox = gui.Text(window,font=('Arial', 16),
                   height=2)
textbox.pack(padx="10",pady="20")

# for button
# button = gui.Button(window, text="Click Me!", font=("Ariel", 18))
# button.pack(padx=10, pady=10)

buttonframe = gui.Frame(window)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)


# grid of button
btn1 = gui.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=gui.W+gui.E)

btn2 = gui.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=gui.W+gui.E)

btn3 = gui.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=gui.W+gui.E)

btn4 = gui.Button(buttonframe, text="4", font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=gui.W+gui.E)

btn5 = gui.Button(buttonframe, text="5", font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=gui.W+gui.E)

btn6 = gui.Button(buttonframe, text="6", font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=gui.W+gui.E)
buttonframe.pack(fill='x') # si buttonframe ang tatawagin

anotherbtn = gui.Button(window, text="TEXT")
anotherbtn.place(x=300, y=300, height=100, width=100) # locastion ng button


window.mainloop() #important to appear 
