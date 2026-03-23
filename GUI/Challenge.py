import tkinter as tk 

window = tk.Tk()

window.title("Smart Unit Converter")

def sub():
    value = int(ask.get())
    if choice.get() == 1:
        f = (value * 1.8) + 32
        result ["text"] = f"{f}"
    elif choice.get() == 0:
        m = value * 0.621371
        result ["text"] = f"{m}"
    else:
        result ["text"] = f"Number only"


head = tk.Label(window,text="Smart Units Converter")
result = tk.Label(window,text="Enter the value")

ask = tk.Entry(window)

choice = tk.IntVar()
heat = tk.Radiobutton(window,text="Celsius to Fahrenheit",value=1,variable=choice)
distance = tk.Radiobutton(window, text="Kilometers to Miles", value=0, variable=choice)
btn = tk.Button(window,text="Convert",command=sub)


head.grid(row=0,column=0,columnspan=3)
result.grid(row=1,column=0,columnspan=3)
ask.grid(row=2,column=0,columnspan=3)
heat.grid(row=3,column=0)
distance.grid(row=4,column=0)
btn.grid(row=5,column=0,columnspan=3,rowspan=2)
window.mainloop()