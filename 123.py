from tkinter import *

op=0
n1=0
opf=False
def lst(nm):
    if int(lab['text'])!=0 and opf==False:
        lab['text']=lab["text"]+nm
    else:
        lab['text']=nm

def opst(opv):
    global op
    global n1
    global opf
    n1=int(lab['text'])
    op=opv
    opf=True

def equal():
    n2=int(lab['text'])
    if op=="1":
        lab['text']=n1+n2
    elif op=="2":
        lab['text']=n1-n2
    elif op=="3":
        lab['text']=n1*n2
    elif op=="4":
        lab['text']=n1/n2

window=Tk()
window.title("lable")
window.geometry("500x400+100+50")
window.rowconfigure(1,weight=1)
window.rowconfigure(2,weight=1)
window.rowconfigure(3,weight=1)
window.rowconfigure(4,weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)

lab=Label(window,text="0",justify=RIGHT,anchor=E)
lab.grid(row=0,column=0,columnspan=4,sticky=EW)

bt7=Button(window,text="7",command=lambda:lst("7"))
bt7.grid(row=1,column=0,sticky=NSEW)
bt8=Button(window,text="8",command=lambda:lst("8"))
bt8.grid(row=1,column=1,sticky=NSEW)
bt9=Button(window,text="9",command=lambda:lst("9"))
bt9.grid(row=1,column=2,sticky=NSEW)
bt4=Button(window,text="4",command=lambda:lst("4"))
bt4.grid(row=2,column=0,sticky=NSEW)
bt5=Button(window,text="5",command=lambda:lst("5"))
bt5.grid(row=2,column=1,sticky=NSEW)
bt6=Button(window,text="6",command=lambda:lst("6"))
bt6.grid(row=2,column=2,sticky=NSEW)
bt1=Button(window,text="1",command=lambda:lst("1"))
bt1.grid(row=3,column=0,sticky=NSEW)
bt2=Button(window,text="2",command=lambda:lst("2"))
bt2.grid(row=3,column=1,sticky=NSEW)
bt3=Button(window,text="3",command=lambda:lst("3"))
bt3.grid(row=3,column=2,sticky=NSEW)
bt0=Button(window,text="0",command=lambda:lst("0"))
bt0.grid(row=4,column=0,sticky=NSEW)
btpoint=Button(window,text=".",command=lambda:lst("."))
btpoint.grid(row=4,column=1,sticky=NSEW)
btequal=Button(window,text="=",command=equal)
btequal.grid(row=4,column=2,sticky=NSEW)
btexcept=Button(window,text="/",command=lambda:opst("4"))
btexcept.grid(row=1,column=3,sticky=NSEW)
btmp=Button(window,text="*",command=lambda:opst("3"))
btmp.grid(row=2,column=3,sticky=NSEW)
btadd=Button(window,text="+",command=lambda:opst("1"))
btadd.grid(row=3,column=3,sticky=NSEW)
btdda=Button(window,text="-",command=lambda:opst("2"))
btdda.grid(row=4,column=3,sticky=NSEW)
window.mainloop()