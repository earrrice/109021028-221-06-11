from tkinter import *

flag=True

def bttxt(n):
    global flag
    if n == 0 and bt0.cget("text")=="":#讓重複按沒有效果
        if flag:
            bt0.config(text="O")
        else:
            bt0.config(text="X")
        #bt0.config(state=DISABLED)#字出現後鎖住，但是顏色會變淡
    elif n == 1 and bt1.cget("text")=="":
        if flag:
            bt1.config(text="O")
        else:
            bt1.config(text="X")
    elif n == 2 and bt2.cget("text")=="":
        if flag:
            bt2.config(text="O")
        else:
            bt2.config(text="X")
    elif n == 3 and bt3.cget("text")=="":
        if flag:
            bt3.config(text="O")
        else:
            bt3.config(text="X")
    elif n == 4 and bt4.cget("text")=="":
        if flag:
            bt4.config(text="O")
        else:
            bt4.config(text="X")
    elif n == 5 and bt5.cget("text")=="":
        if flag:
            bt5.config(text="O")
        else:
            bt5.config(text="X")
    elif n == 6 and bt6.cget("text")=="":
        if flag:
            bt6.config(text="O")
        else:
            bt6.config(text="X")
    elif n == 7 and bt7.cget("text")=="":
        if flag:
            bt7.config(text="O")
        else:
            bt7.config(text="X")
    elif n == 8 and bt8.cget("text")=="":
        if flag:
            bt8.config(text="O")
        else:
            bt8.config(text="X")
    flag=not flag

    if bt0.cget("text")==bt1.cget("text") and bt0.cget("text")==bt2.cget("text"):
        if bt0.cget("text")=="O":
            print("O win")
        elif bt0.cget("text")=="X":
            print("X win")
    elif bt3.cget("text")==bt4.cget("text") and bt3.cget("text")==bt5.cget("text"):
        if bt3.cget("text")=="O":
            print("O win")
        elif bt3.cget("text")=="X":
            print("X win")
    elif bt6.cget("text")==bt7.cget("text") and bt6.cget("text")==bt8.cget("text"):
        if bt6.cget("text")=="O":
            print("O win")
        elif bt6.cget("text")=="X":
            print("X win")
    elif bt0.cget("text")==bt3.cget("text") and bt0.cget("text")==bt6.cget("text"):
        if bt0.cget("text")=="O":
            print("O win")
        elif bt0.cget("text")=="X":
            print("X win")
    elif bt1.cget("text")==bt4.cget("text") and bt1.cget("text")==bt7.cget("text"):
        if bt1.cget("text")=="O":
            print("O win")
        elif bt1.cget("text")=="X":
            print("X win")
    elif bt2.cget("text")==bt5.cget("text") and bt2.cget("text")==bt8.cget("text"):
        if bt2.cget("text")=="O":
            print("O win")
        elif bt2.cget("text")=="X":
            print("X win")
    elif bt0.cget("text")==bt4.cget("text") and bt0.cget("text")==bt8.cget("text"):
        if bt0.cget("text")=="O":
            print("O win")
        elif bt0.cget("text")=="X":
            print("X win")
    elif bt2.cget("text")==bt4.cget("text") and bt2.cget("text")==bt6.cget("text"):
        if bt2.cget("text")=="O":
            print("O win")
        elif bt2.cget("text")=="X":
            print("X win")

window=Tk()
window.title("lable")
window.geometry("500x400+100+50")
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)

bt0=Button(window,text="",command=lambda:bttxt(0))
bt0.grid(row=0,column=0,sticky=NSEW)
bt1=Button(window,text="",command=lambda:bttxt(1))
bt1.grid(row=0,column=1,sticky=NSEW)
bt2=Button(window,text="",command=lambda:bttxt(2))
bt2.grid(row=0,column=2,sticky=NSEW)
bt3=Button(window,text="",command=lambda:bttxt(3))
bt3.grid(row=1,column=0,sticky=NSEW)
bt4=Button(window,text="",command=lambda:bttxt(4))
bt4.grid(row=1,column=1,sticky=NSEW)
bt5=Button(window,text="",command=lambda:bttxt(5))
bt5.grid(row=1,column=2,sticky=NSEW)
bt6=Button(window,text="",command=lambda:bttxt(6))
bt6.grid(row=2,column=0,sticky=NSEW)
bt7=Button(window,text="",command=lambda:bttxt(7))
bt7.grid(row=2,column=1,sticky=NSEW)
bt8=Button(window,text="",command=lambda:bttxt(8))
bt8.grid(row=2,column=2,sticky=NSEW)
window.mainloop()