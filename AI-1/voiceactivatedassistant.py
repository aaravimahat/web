import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import subprocess

def speak(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
   
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)

    try:
      command=r.recognize_google(audio)
      print(f"you said {command}")
      return command.lower()
    
    except sr.UnknownValueError:
        speak("i didnt catch it, sorry")

    except sr.RequestError:
        speak("there was a problem in internet connection")

    return ""

def b(command):
    if "hello" in command:
        speak("hello, what may i do for you?")

    elif "time" in command:
        now=datetime.now().strftime("%H:%H")
        speak(f"the time is {now}")

    elif "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")

    elif "open spotify" in command:
        speak("opening spotify")
        webbrowser.open("https://open.spotify.com/")

    elif "open instagram" in command:
        speak("opening instagram")
        webbrowser.open("https://www.instagram.com/")

    elif "open google" in command:
        speak("opening google")
        webbrowser.open("https://www.google.com/")

    elif "open calculator" in command:
        subprocess.Popen(["open", "-a", "Calculator"])


    elif "stop" in command or "exit" in command:
        speak("Goodbye")
        return False
    
    else:
        speak("i dont know how to do that")
    return True

def main():
    speak("voice assistant is activated, how may i help you")
    while True:

        command=get_audio()
        if command and not b(command):
            break
main()
    


