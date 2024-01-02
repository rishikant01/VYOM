import pyttsx3
import wikipedia
from Listen_Speak import Listen,Speak_en

def query():
    voice=pyttsx3.init()
    In = Listen()
    result = wikipedia.summary(In,sentences=3)
    print(result)
    Speak_en(result)
    voice.runAndWait()

while True:
    query()
    user_input = input('To continue press y: ')
    if user_input != 'y':
        break