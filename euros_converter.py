import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
roof=Tk()
roof.geometry("400x400")
a=StringVar()
c=StringVar()
def Convert():
    m=int(c.get())*87.76
    messagebox.showinfo("Converted",str(m)+" euros")
Entry(roof,textvariable=a,width=30).grid(row=1,column=1,padx=20,pady=20,ipadx=40,ipady=70)
Button(roof,text="convert to Euros",command=Convert,fg="white",bg="red").grid(row=3,column=1,padx=20,pady=20)
combo=ttk.Combobox(roof,width=25,textvariable=c)
combo['values']=(1,2,3,4)
combo.grid(row=2,column=1,padx=25,pady=25)
combo.current()
roof.mainloop()
