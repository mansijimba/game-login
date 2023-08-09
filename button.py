from tkinter import*
from PIL import ImageTk, Image

butt=Tk()
butt.geometry("450x430")
butt.resizable(0,0)

butt.configure(bg='lavender')

img1 = Image.open("start_btn.png")
img2 = Image.open("exit_btn.png")

resized_img1 = img1.resize((120, 70), Image.ANTIALIAS)
resized_img2 = img2.resize((120, 70), Image.ANTIALIAS)

img1_obj = ImageTk.PhotoImage(resized_img1)
img2_obj = ImageTk.PhotoImage(resized_img2)

def onstart_click():
    print("Start Clicked")
def onexit_click():
    print("Exit CLicked")

button1 = Button(butt, text="Click Me", image=img1_obj, command=onstart_click)
button1.place(x=50,y=140)
button2 = Button(butt, text="Click Me", image=img2_obj, command=onexit_click)
button2.place(x=270,y=140)




butt.mainloop()