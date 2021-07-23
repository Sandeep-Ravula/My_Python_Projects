# GUI program to generate the OTP password of given length

from tkinter import *
import random, re, datetime
root = Tk()
root.title("Einsttein'S password generator")
root.geometry("500x500")
root.config(bg = "powderblue")
heading = Label(root, text="Password Generator :", font = ("None 28 bold underline"), bg = "Powderblue", fg = "darkblue")
heading.config(anchor=CENTER)
heading.pack()

count_label = Label(root, text = "How many character's count :", font = ("None 15 bold"),bg="green").place(x=10, y=100)

pass_len = IntVar()
pass_len.set('')
Entry(root, textvariable = pass_len, font = ("None 15 bold"), width = 3, bg="pink").place(x=400,y=100)
pswd = StringVar()
pswd.set('')
pswd_display = Entry(root, textvariable=pswd, font=("None 18 bold"), bg = "white", fg="black").place(x=100, y=200)

def show_pswd():
    cap = ''.join([chr(i) for i in range(65,91)])
    low = ''.join([chr(i) for i in range(97, 123)])
    numb = ''.join(list(map(str, list(range(0,10)))))
    sp = "!@#$%^&*()?><|?/"

    final_pswd = ''.join([random.choice(cap+low+sp+numb) for p in range(pass_len.get())])

    while not re.match(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)', final_pswd):
        final_pswd = ''.join([random.choice(cap + low + sp + numb) for p in range(pass_len.get())])
    else:
        print("validated")
    f=open('password_log.txt', 'a')
    f.write('At  '+ str(datetime.datetime.now())+'   -------->>>  '+'Generated password :'+final_pswd+'\n')
    pswd.set(final_pswd)

def clear_it():
    pswd.set('')
    pass_len.set('')

btn_show_pswd = Button(root, text="Generate Passwrd", font=("None 15 bold"), fg="blue", bg="red", command=show_pswd).place(x=60,y=300)
btn_clear = Button(root, text = "clear", font=("None 15 bold"), fg="blue", bg="red", command=clear_it).place(x=300, y=300)

root.mainloop()
