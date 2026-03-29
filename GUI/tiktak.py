import tkinter as tk

window = tk.Tk()
window.title("Tiktak")

lagay = tk.Entry(window)
lagay.grid(row=2, column=0)

def pili(target_btn):
    user_input = lagay.get().upper()
    
    if user_input == "X" or user_input == "O":
        target_btn.config(text=user_input)
        lagay.delete(0, tk.END)
    else:
        print("Please only type X or O!")

head = tk.Label(window,text="Tic Tac Toe")

frame = tk.Frame(window)

btnA = tk.Button(frame,text="A", command=lambda: pili(btnA))
btnB = tk.Button(frame,text="B", command=lambda: pili(btnB))
btnC = tk.Button(frame,text="C", command=lambda: pili(btnC))

btnD = tk.Button(frame,text="D", command=lambda: pili(btnD))
btnE = tk.Button(frame,text="E", command=lambda: pili(btnE))
btnF = tk.Button(frame,text="F", command=lambda: pili(btnF))

btnG = tk.Button(frame,text="G", command=lambda: pili(btnG))
btnH = tk.Button(frame,text="H", command=lambda: pili(btnH))
btnI = tk.Button(frame,text="I", command=lambda: pili(btnI))

head.grid(row=0,column=0)
frame.grid(row=1,column=0)
btnA.grid(row=0,column=0,ipadx=5)
btnB.grid(row=0,column=1,ipadx=5)
btnC.grid(row=0,column=2,ipadx=5)

btnE.grid(row=1,column=0,ipadx=5)
btnD.grid(row=1,column=1,ipadx=5)
btnF.grid(row=1,column=2,ipadx=5)

btnG.grid(row=2,column=0,ipadx=5)
btnH.grid(row=2,column=1,ipadx=5)
btnI.grid(row=2,column=2,ipadx=5)


window.mainloop()
