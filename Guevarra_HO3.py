import tkinter as tk

window = tk.Tk()
window.title("Simple Claculator")
window.config(bg="black")
window.resizable(False,False)

def add():
    value1 = input1.get()
    value2 = input2.get()
    x = int(value1)
    y = int(value2)
    sum = x + y
    header ['text'] = f"The sum of {x} + {y} is {sum}"
def sub():
    value1 = input1.get()
    value2 = input2.get()
    x = int(value1)
    y = int(value2)
    sum = x - y
    header ['text'] = f"The Different of {x} - {y} is {sum}"

def times():
    value1 = input1.get()
    value2 = input2.get()
    x = int(value1)
    y = int(value2)
    sum = x * y
    header ['text'] = f"The Times of {x} x {y} is {sum}"

def div():
    value1 = input1.get()
    value2 = input2.get()
    x = int(value1)
    y = int(value2)
    sum = x / y
    header ['text'] = f"The Division of {x} / {y} is {sum}"

header = tk.Label(window,text="Sample Calculator",background="blue",fg="white",font=(15))
header.grid(row=0,column=0,columnspan=5,pady=15)

entry1 = tk.Label(window,text="Enter 1st Number:",background="blue",fg="white")
entry2 = tk.Label(window,text="Enter 2nd Number:",background="blue",fg="white")
input1 = tk.Entry(window)
input2 = tk.Entry(window)

entry1.grid(row=1,column=0,columnspan=2,pady=2)
entry2.grid(row=2,column=0,columnspan=2,pady=2)
input1.grid(row=1,column=3,columnspan=2,pady=2)
input2.grid(row=2,column=3,columnspan=2,pady=2)


btn_add = tk.Button(window,text="Add",command=add,background="blue",fg="white")
btn_Subtract = tk.Button(window,text="Subtract",command=sub,background="blue",fg="white")
btn_Multiple = tk.Button(window,text="Multiple",command=times,background="blue",fg="white")
btn_Division = tk.Button(window,text="Division",command=div,background="blue",fg="white")





btn_add.grid(row=3,column=1,pady=5)
btn_Subtract.grid(row=3,column=3,pady=5)
btn_Multiple.grid(row=4,column=1,pady=5)
btn_Division.grid(row=4,column=3,pady=5)
window.mainloop()
