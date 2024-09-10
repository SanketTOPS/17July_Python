import tkinter
from tkinter import ttk

screen=tkinter.Tk()
screen.title("Myapp")
screen.geometry("400x500")
screen.config(background="lightblue")

"""lbl_f=tkinter.Label(text="Firstname:").pack()
lbl_l=tkinter.Label(text="Lastname:").pack()"""

"""lbl_f=tkinter.Label(text="Firstname:").place(x=0,y=0)
lbl_l=tkinter.Label(text="Lastname:").place(x=0,y=30)"""

lbl_f=tkinter.Label(text="Firstname:",bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=0,column=0,sticky='w')
lbl_l=tkinter.Label(text="Lastname:",bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=1,column=0,sticky='w')

txt_f=tkinter.Entry().grid(row=0,column=1,sticky='w')
txt_l=tkinter.Entry().grid(row=1,column=1,sticky='w')

male=tkinter.Radiobutton(value=0, text='Male',bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=2,column=0,sticky='w')
female=tkinter.Radiobutton(value=1,text='Female',bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=2,column=1,sticky='w')

ch1=tkinter.Checkbutton(text="Python",bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=3,column=0,sticky='w')
ch2=tkinter.Checkbutton(text="JAVA",bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=4,column=0,sticky='w')
ch3=tkinter.Checkbutton(text="PHP",bg='lightblue',fg='red',font='Fixedsys 16 bold').grid(row=5,column=0,sticky='w')

city=["Rajkot","Ahmedabad","Surat","Baroda"]
select_city=ttk.Combobox(values=city).grid(row=6,column=0)

def btnCLick():
    print("Button Clicked!")

btn=tkinter.Button(text="Submit",font='Fixedsys 16 bold',command=btnCLick).place(x=180,y=200)

screen.mainloop()