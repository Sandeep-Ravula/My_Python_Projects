import speech_recognition as sr,pyttsx3,pywhatkit,datetime,wikipedia,re,os,time,smtplib,sys,tkinter as tk
from tkinter import *
from tkinter import ttk
from selenium import webdriver

chrome_wb=r"C:\Users\HP\Desktop\chromedriver_win32\chromedriver.exe"
Bot=pyttsx3.init()
def talk(speech):
    Bot.say(speech)
    Bot.runAndWait()
listener=sr.Recognizer()
pics=('pictures','pics','images','photos','bommalu')
wikis=('who','what')
mails=('mail','email')

voices=Bot.getProperty('voices')
Bot.setProperty('voice',voices[0].id)
d1='Iam Listening Mister Raavula'
d2="How can I help you"
def command_creation(d1,d2):
    try:
        with sr.Microphone() as source:
            print("Iam Listening Mister Ravula...")
            talk(d1)
            talk(d2)
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            print(' '+command)
    except:
        pass
    return(command)

dic={'sandeep':'sandeepsandy25041996@gmail.com','sateesh':'ravulasateesh.1991@gmail.com','satish':'ravulasateesh.1991@gmail.com','venkatesh':'venkieee213@gmail.com'}
def dynamic_sandeep_functioning(com):

        if 'play' in com:
            yt_song = com.replace('play', '')
            pywhatkit.playonyt(yt_song)
        elif any(mail in com for mail in mails):
            print('block-2 : {}'.format(com))
            m = re.match('^.*to\s(.*)$', com)
            receiver = m.group(1)
            print(receiver)
            mail_id = dic[receiver]
            message = command_creation('Hey Raavula', 'what message do you want to send')
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('sandeepmech367@gmail.com', 'Sandeepmail@367')
            print(mail_id)
            server.sendmail('sandeepmech367@gmail.com', mail_id, message)
            server.close()
            print("mail sent successful")
        elif 'hey' in com:
            print('hey sandeep')
        elif any(pic in com for pic in pics):
            word = re.match('^.*of\s(.*)$', com)
            word = word.group(1)
            talk("showing pictures of "+word)
            driver = webdriver.Chrome(chrome_wb)
            g = word.replace(' ', '+')
            link = 'https://www.google.com/search?q=' + g + '&rlz=1C1SQJL_enIN855IN855&sxsrf=ALeKk01QxFdZOTiQrVlMUQQFNbgSdvRSYg:1608380167878&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiNr8eEg9rtAhUD4zgGHYTxDP0Q_AUoAXoECCIQAw&biw=1366&bih=625'
            driver.get(link)
            driver.quit()
        elif 'hey' in com:
            talk('Tell sandeep')
        elif 'time' in com:
#            print("Mister Raavula, current time is " + datetime.datetime.now().strftime("%I:%M %p"))
            talk("Mister Raavula, current time is " + datetime.datetime.now().strftime("%I:%M %p"))
        elif any(wiki in com for wiki in wikis):
            w= re.match('^.*is\s(.*)$', com)
            w = w.group(1)
            print(w)
            talk(wikipedia.summary(w, 1))
        elif 'how are you' in com:
            talk("Iam fine Raavula, how are you")
            time.sleep(3)
            talk('oh okay ! can i know the reason Raavula')
            time.sleep(3)
        elif 'stop' in com:
            talk("shutting down the alexa")

        else:
            talk('I didnt get you Ravula, please repeat')
    #except:print('exception')


def run_sandeep():
    try:
        com=command_creation(d1,d2)
        print('******'+com)
        #if 'alexa' in com:
        dynamic_sandeep_functioning(com)


    except:pass
while(True):
    run_sandeep()

#root = Tk()

#def helloCallBack():
#tkMessageBox.showinfo( "Hello Python", "Hello World")

#B = tk.Button(root, text ="Alexa",command=btn())

#B.pack()
#root.mainloop()




