import tkinter as tk

window = tk.Tk()

window.title("D2")
window.geometry("500x500")
window.resizable(True,True)
window.config(bg="yellow")

title = tk.Label(window,
                 text="Your mood for today",
                 )
title.pack()

def sad_pic():
    new_img = tk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\ITCS102_1A\ITCS103_1A\discussion\D2_photo\sad.png")
    new_img = new_img.subsample(4, 4)
    
    img_label.config(image=new_img, text="I'm sad")
    
    # "Anchor" the image so Python doesn't delete it (Garbage Collection)
    img_label.image = new_img

def happy_pic():
    new_img = tk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\ITCS102_1A\ITCS103_1A\discussion\D2_photo\happy.png")
    new_img = new_img.subsample(4, 4)
    
    img_label.config(image=new_img, text="I'm happy")
    
    # "Anchor" the image so Python doesn't delete it (Garbage Collection)
    img_label.image = new_img

img = tk.PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\ITCS102_1A\ITCS103_1A\discussion\D2_photo\cute.png")
img = img.subsample(2,2)
img_label = tk.Label(window,image=img,text="Im sad")
img_label.pack()


# button
btn =  tk.Frame(window)
btn.pack(pady=20)

sad = tk.Button(btn, text="Sad", command=sad_pic)
sad.pack(side="left",padx=10, pady=10)

happy = tk.Button(btn, text="Happy", command=happy_pic)
happy.pack(side="left",padx=10, pady=10) 
# side left para pumunta sa left side




window.mainloop()
