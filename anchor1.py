from tkinter import *

window=Tk()
window.title("lable")
window.geometry("500x400+100+50")
lab = Label(window,
            text="AAA",
            #anchor="nw",#字的位置(東西南北
            anchor=SE,#可以用大寫且不用雙引號
            width=30,
            height=20,
            bg="#ccffdd",
            fg="#ff0000")
lab.pack()
window.mainloop()