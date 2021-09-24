import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root=Tk()
m=StringVar()
n=StringVar()
root.geometry("350x220")
root.title("Login Page")
def click():
    if m.get()=="sandeep" and n.get()=="April@25041996":
        messagebox.showinfo("Login","Success")
        #print("login successful")
    else:messagebox.showinfo("Login","Username and Password is not matching")
Label(root,text="Username :",bg="black",fg="white",width=15).grid(row=0,column=0,padx=10,pady=20)

Entry(root,textvariable=m,width=15).grid(row=0,column=1,padx=10,pady=20)

Label(root,text="Password :",bg="black",fg="white",width=15).grid(row=1,column=0,padx=10,pady=20)

Entry(root,textvariable=n,width=15,show="*").grid(row=1,column=1,padx=10,pady=20)
#e2.pack()
Button(root,text="Login",command=click,bg="blue",fg="white",width=10).grid(row=3,column=1,padx=5,pady=10)

root.mainloop()