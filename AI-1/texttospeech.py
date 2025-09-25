import speech_recognition as sr
from googletrans import Translator
import pyttsx3

def a(text,language="en"):
    eng=pyttsx3.init()
    eng.setProperty("rate", 100)
    eng.setProperty("volume",1)
    voices=eng.getProperty("voices")
    if language== "en":

     voices=eng.setProperty("voice",voices[0].id)
    else :
       eng.setProperty("voice",voices[1].id)

    eng.say(text)
    eng.runAndWait()


def STT():
   recognizer=sr.Recognizer()
   with sr.Microphone() as b:
      print("speak now in english")
      audio=recognizer.listen(b)

   try:
      print("recognizing speech")
      text=recognizer.recognize_google(audio,language="en")
      print(f"you said{text}")
      return text
   
   except sr.UnknownValueError:
      print("couldnt undestand audio")
      return " "
   
   except sr.RequestError as e:
      print(f"couldnt request results {e}")
      return ""
   
def translate(text, target_language="es"):
   translator=Translator()
   translation=translator.translate(text,dest=target_language)
   print(f"Translated text{translation.text}")
   return translation.text


def display():
   print("available languages are these")
   d={1:"ne", 2:"ta", 3:"te", 4:"ml",5:"gu",6:"pa",7:"bn", 8:"fr", 9:"ma", 10:"de"}
   print(d)
   ch=int(input("enter your choice"))
   return d.get(ch,"es")
def main():
   target_languages=display()
   text=STT()
   translated_text=translate(text,target_languages)
   a(translated_text,language="en")
   print("sentence spoken out")

main()



   





