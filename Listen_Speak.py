import speech_recognition as sr
import pyttsx3
def Speak_hi(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    # Assuming you have a Hindi voice installed, select it
    for voice in voices:
        if "hindi" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 170)
    engine.say(Text)
    engine.runAndWait()
def Speak_en(Text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.say(Text)
    engine.runAndWait()
def Listen():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source,0,5)
    
    try:
        print("Recognizing..")
        query= r.recognize_google(audio)

    except:
        return ""
    
    query=str(query)
    return query.lower()
import sys
import speech_recognition as sr

def Listen_hi():
    # Set the default encoding to utf-8
    sys.stdout.reconfigure(encoding='utf-8')

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening to Hindi speech...")

        try:
            audio = recognizer.listen(source, timeout=5)
            print("Recognition in progress...")

            query = recognizer.recognize_google(audio, language="hi-IN")

        except sr.WaitTimeoutError:
            print("No speech detected. Timeout.")
            query="Null"

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            query="Null"

        except sr.UnknownValueError:
            print("Speech recognition could not understand the audio.")
            query="Null"
        
    return query
# z=Listen()
# print(z)
# Speak_en(z)
# x=Listen_hi()
# print(x)
# Speak_hi(x)