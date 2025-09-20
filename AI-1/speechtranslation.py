import speech_recognition as sr
import pyttsx3
from googletrans import Translator
import random



def speak(text,rate=150,volume=1):
    engine=pyttsx3.init()
    engine.setProperty("rate",rate)
    engine.setProperty("volume",volume)
    engine.say(text)
    engine.runAndWait()

def speech_to_text(timeout=5,phrase_time_limit=7):
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        greeting=["hello, how may i help you", "go ahead im listening","say something i will translate", "speak something i will help"]
        msg=random.choice(greeting)
        print(msg)
        speak(msg)

        try:
            audio=recognizer.listen(source,timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            print("timeout! u didnt say anything")
            return ""
        
    try:
        print("recognizing speech")
        text=recognizer.recognize_google(audio,language="en-US")
        print("you said this",text)
        return text
    
    except:
        speak("i didnt understand that")
        return ""
    
def translate1(text,target_language="es"):
    translator=Translator()

    try:
        translation=translator.translate(text,dest=target_language)
        return translation.text
    
    except:
        speak("couldnt fetch the translated text")
        return ""
    
def display():
   print("available languages are these")
   d={1:"hi", 2:"ta", 3:"te", 4:"ml",5:"gu",6:"pa",7:"bn", 8:"fr", 9:"ma", 10:"de"}

   print(d)
   ch=int(input("enter your choice"))
   return d.get(ch,"es")

def main():
    target_languages = display()
    text = speech_to_text()
    translated_text = translate1(text, target_languages)
    if translated_text:
        print("Translated text:", translated_text)
        speak(translated_text)
    else:
        print("Translation failed.")
    print("sentence spoken out")

main()
                



    
            
    
    
