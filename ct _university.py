import tkinter as tk
import webbrowser
from tkinter.ttk import *
import speech_recognition as sr
from playsound import playsound
from PIL import Image,ImageTk
import os
import random
top= tk.Tk()
top.title("PERSONAL ASSISTANT")
top.geometry("999x999")
#image for the background
x=ImageTk.PhotoImage(Image.open(r'C:/Users/swanish/Desktop/background1.png'))
back=tk.Label(top,image=x)
back.image=x
back.place(x=2, y=3)
# image for the logo
ct_photo=tk.PhotoImage(file=r"C:\Users\swanish\Desktop\logo.png")
#function to connect the logo with the link
def callweb1(url):
    webbrowser.open(url)
but=tk.Button(top,text="CT",image=ct_photo,command=lambda:callweb1("https://ctuniversity.in/"))
but.grid(row=0,sticky='w',column=0)
t=ct_photo.subsample(4,6)
but.config(image=t)
# Entry box for text message
e1=tk.Entry(top,bg='light grey',fg='black')
e1.place(x=660,y=365,anchor='center')
e1.config(width=49)
#image of search and microphone on the button
photo3=tk.PhotoImage(file=r"C:/Users/swanish/Desktop/search1.png")
photo4=tk.PhotoImage(file=r"C:/Users/swanish/Desktop/microphone3.png")
#function to call 
def callweb2(url1):
    webbrowser.open(url1)

but1=tk.Button(top,text=" ",image=photo3,width=19,command=lambda:callweb2("https://www.google.com/search?q=" +e1.get()))
but1.place(x=820,y=360)
t1=photo3.subsample(12,8)
but1.config(image=t1)
but2 = tk.Button(top,text=' ',width =29,image= photo4,command =(lambda:social()))
but2.place(x=850,y=360)
t2= photo4.subsample(15,10)
but2.config(image=t2)
but3=tk.Button(top,text="EXIT",width=20 ,bg='light grey',fg='black',command=top.destroy)
but3.place(x=700,y=650,anchor='center')

e2 = tk.Entry(top,bg='light grey',fg='black')
e2.place(x=660,y=390,anchor = 'center')
e2.config(width=49)

btn2= tk.StringVar()
speech= sr.Recognizer()


greeting_dict = {'hello': 'hello', 'hi': 'hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}

mp3_greeting_list = ["C:/Users/swanish/Desktop/audio file/mp3/AI/greeting command me.mp3",
                     "C:/Users/swanish/Desktop/audio file/mp3/AI/greetingi am your AI.mp3"]

open_mp3_launch_list = ["C:/Users/swanish/Desktop/audio file/mp3/AI/open_1.mp3", "C:/Users/swanish/Desktop/audio file/mp3/AI/open_2.mp3"]


def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def buttonClick():
    with sr.Microphone() as source:
        message =""
        try:
            audio = speech.listen(source = source,timeout =20,phrase_time_limit =5)
            message = str(speech.recognize_google(audio))
            
            e1.delete(0,'end')
            e1.insert(0,message)
            
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            pass
    return message

def callback():
    voice_note = e1.get()
    if(voice_note.split(" ")[0] == 'open'):
        key =  voice_note.split(" ")[1]
        
        webbrowser.open('http://google.com/search?q=' + key)

    else:
        
        webbrowser.open('http://google.com/search?q=' + e1.get())

def is_valid_note(greeting_dict, voice_note):
    for key, value in greeting_dict.items():
        try:
            if value == voice_note.split(" ")[0]:
                return True
                break
            elif key == voice_note.split(" ")[1]:
                return True
                break
        except IndexError:
            pass
    return False
def social():
    buttonClick()
    voice_note = e1.get()
    if is_valid_note(greeting_dict, voice_note):
        e2.insert(0,"I Am Greeting")
        e2.delete(0,'end')
        play_sound(mp3_greeting_list)
    elif (voice_note=="open FB or open Facebook"):
        webbrowser.open("https://www.facebook.com/")
    elif (voice_note=="open Twitter"):
        webbrowser.open("https://twitter.com/")
    elif (voice_note=="open Instagram"):
        webbrowser.open("https://www.instagram.com/?hl=en")
    elif (voice_note=="open hike"):
        webbrowser.open("https://www.hike.com//")
    elif (voice_note=="open Fipkart"):
        webbrowser.open("https://www.flipkart.com/")
    elif (voice_note=="open Amazon"):
        webbrowser.open("https://www.amazon.in/")
    elif (voice_note=="open Myntra"):
        webbrowser.open("https://www.myntra.com/")
    elif (voice_note=="open youtube"):
        webbrowser.open("https://www.youtube.com/")
    elif (voice_note=="open Gmail"):
        webbrowser.open("https://www.google.com/gmail/")
    elif (voice_note=="open WhatsApp Web"):
        webbrowser.open("https://web.whatsapp.com/")
        
    
    elif is_valid_note(open_launch_dict, voice_note):
        play_sound(open_mp3_launch_list)
        but1.flash()
        but1.invoke()
    elif "by" in voice_note:
        playsound('C:/Users/swanish/Desktop/SKbye.mp3')
        but3.invoke()
        exit()
        
        
    '''        
            continue
    elif "by" in voice_note:
            
        exit()
    '''
if(e1 == ""):
    print("please write something")
else:
    top.bind('<Return>',callback)




if __name__ == "__main__":
    playsound('C:/Users/swanish/Desktop/audio file/greeting_welcome.mp3')
    top.mainloop()

    

                                                                                                                                                     
