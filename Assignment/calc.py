from tkinter import *
from tkinter import Image

#create a main screen.
#set the image icon in main screen.
#set the title for main screen.
#set the configuration of main screen.
#set the background color of main scrren.
window=Tk()

window.iconbitmap('D:\img\calc.ico')
window.title("Simple Calculator")
window.geometry("329x371")
window.config(bg="#f5f5f5")

#Create the illustration of variable class that is StringVar().
input=StringVar()

#globally declare the name variable among all the functions
name=""

#function to update expression inside entry box.
def btn_press(num):
    global name
    name=name+str(num)
    input.set(name)

#function to evaluate the final value.
def equal():
    try:
        global name
        total=str(eval(name))
        input.set(total)
        name=""
    except:
        input.set("error")
        name=""

#function to clear contents of entry box.
def clear():
    global name
    name=""
    input.set("0")

#create the text entry box.
#set the configuration of entry box.
entry=Entry(window,font=("Arial Narrow",20),text=input,bg="#ffffff",bd=8)
entry.grid(row=0,column=0,columnspan=4,padx=2,pady=7,ipadx=34,ipady=6)

#defining and putting buttons in the particular place inside the main screen.
#when user press the button,command related to that button gets execute.
b1=Button(window,text="1",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(1))
b1.place(x=10,y=255)
b2=Button(window,text="2",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(2))
b2.place(x=90,y=255)
b3=Button(window,text="3",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(3))
b3.place(x=170,y=255)

b4=Button(window,text="4",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(4))
b4.place(x=10,y=195)
b5=Button(window,text="5",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(5))
b5.place(x=90,y=195)
b6=Button(window,text="6",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(6))
b6.place(x=170,y=195)

b7=Button(window,text="7",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(7))
b7.place(x=10,y=135)
b8=Button(window,text="8",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(8))
b8.place(x=90,y=135)
b9=Button(window,text="9",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(9))
b9.place(x=170,y=135)

b0=Button(window,text="0",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press(0))
b0.place(x=10,y=315)

add=Button(window,text="+",padx=28,pady=15,bg="#d1c4e9",command=lambda:btn_press("+"))
add.place(x=250,y=135)
subtract=Button(window,text="-",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press("-"))
subtract.place(x=250,y=195)
multiply=Button(window,text="*",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press("*"))
multiply.place(x=250,y=255)
division=Button(window,text="/",padx=30,pady=15,bg="#d1c4e9",command=lambda:btn_press("/"))
division.place(x=250,y=315)

btn_clear=Button(window,text="Clear",padx=134,pady=15,font=("Arial",11),bg="#d1c4e9",command=clear)
btn_clear.place(x=8,y=73)
btn_equal=Button(window,text="=",padx=69,pady=15,bg="#d1c4e9",command=equal)
btn_equal.place(x=90,y=315)

#start the program
window.mainloop()
