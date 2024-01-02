import pyttsx3
import wikipedia
from Listen_Speak import Listen,Speak_en
from Listen_Speak import Speak_en,Listen,Speak_hi
import os
import webbrowser
from requests import get
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
def query():
    voice=pyttsx3.init()
    In = Listen()
    result = wikipedia.summary(In,sentences=3)
    print(result)
    Speak_en(result)
    voice.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Speak_en("Good Morningn Sir")
        #Speak_hi("Jai Shri raam")
    elif hour>=12 and hour<=18:
        Speak_en("Good Afternoon Sir ")
        #Speak_hi("Jai Shri raam")
    else:
        Speak_en("Good Evening Sir ")
        #Speak_hi("Jai Shri raam")
    Speak_en("I am Your Assistant .")
    Speak_en("How can I help you.")
    
def commands(query):
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Google Chrome"))
    if "open your folder"  in query:
        npath="path"
        Speak_en("opening folder")
        os.startfile(npath)
    elif "geeks for geeks" in query:
        npath="path"
        Speak_en("opening folder")
        os.startfile(npath)
    elif "ip address" in query:
        ip=get('https://api.ipify.org').text
        Speak_en(f"Your Ip address is {ip}")
    elif "open google" in query:
        print("Sir what should i search on google")
        Speak_en("Sir what should i search on google")
        cm=Listen()
        webbrowser.open(f"{cm}")
    elif "search on google about" in query:
        Speak_en("Showing results")
        cm=Listen()
        webbrowser.open(f"{cm}")
    elif "no thanks" in query:
        Speak_en("ok sir, have a  good day")
while True:
    query()
    user_input = input('To continue press y: ')
    if user_input != 'y':
        break
