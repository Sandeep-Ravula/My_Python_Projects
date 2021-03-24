from tkinter import Label, Tk
import time

#initiating a tool-kit window , assiging to root
root=Tk()
root.title("Digital Clock")
root.geometry("500x150")
# for the start left top cordinate of the windows should be fixed
root.resizable(0,0)

# customized configurations for the display
text_font=("Boulder",68,'bold')
background="#f2e750"
foreground="#363529"
border_width=25

label=Label(root,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def digital_clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,digital_clock) # after every 200 milli_seconds it refreshes

digital_clock()

root.mainloop()