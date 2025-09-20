import speech_recognition as sr
import pyttsx3
import datetime

tts_engine=pyttsx3.init()
tts_engine.setProperty("rate",130)
tts_engine.setProperty("volume",1)

def speak(text):
    print("assistant",text)
    tts_engine.say(text)
    tts_engine.runAndWait()

def process_query(query):
    query=query.lower()
    if "time" in query:
        now=datetime.datetime.now().strftime("%H:%M")
        return f"the current time is{now}"
    
    elif "date" in query:
        today=datetime.datetime.now().strftime("%B %d,%y")
        return f"the current date is{today}"

    else:
        return "im sorry, i didnt understand"
    
recognizer=sr.Recognizer()
mic=sr.Microphone()

print("listening..say time or date (ctrl+c to stop)")

with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    try:
        while True:
            print("you can speak now")
            audio=recognizer.listen(source)

            try:
                text=recognizer.recognize_google(audio)
                print("you said",text)

                reply=process_query(text)
                speak(reply)

            except sr.RequestError:
                print("network error,please check your internet connection")
                speak("network error,please check your internet connection")

            except sr.UnknownValueError:
                print("sorry couldnt understand this")
                speak("sorry couldnt understand this")
    except KeyboardInterrupt:
        print("exiting")
        speak("goodbye")

            

        

