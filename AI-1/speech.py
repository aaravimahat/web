import sys,wave,threading,time,speech_recognition as sr
import pyaudio
import numpy as np

import matplotlib.pyplot as plt
stop=threading.Event()


def wait():
    input("press enter to stop")
    stop.set()

def spinner():
    spinnerc="|/-\\"
    i=0

    while not stop.is_set():
        sys.stdout.write("\rrecording.."+spinnerc[i%len(spinnerc)])
        sys.stdout.flush()
        i=i+1
        time.sleep(0.1)
    sys.stdout.write("recording has stopped")

def pressed():
    p=pyaudio.PyAudio()
    format=pyaudio.paInt16
    channels=1
    frames_per=1024
    rate=16000
    stream=p.open(format=format,channels=channels,rate=rate, input=True,frames_per_buffer=frames_per)
    a=[]
    threading.Thread(target=wait).start()
    threading.Thread(target=spinner).start()

    while not stop.is_set():
        try:
            data=stream.read(frames_per)
            a.append(data)

        except Exception as e:
            print(e)
            break

    stream.stop_stream()
    stream.close()
    sample_width=p.get_sample_size(format)
    p.terminate
    audio_data=b''.join(a)
    return audio_data,rate,sample_width

def save1(data,rate,width,filename="a.wav"):
    with wave.open(filename,"wb") as bc:
        bc.setnchannels(1)
        bc.setframerate(rate)
        bc.setsampwidth(width)
        bc.writeframes(data)
    print("saved successfully",filename)

def transcribe(data,rate,width,filename="text.txt"):
    a=sr.Recognizer()
    audio=sr.AudioData(data,rate,width)
    try:
        text=a.recognize_google(audio)
    except sr.UnknownValueError:
        print("google speech couldnt understand audio")

    except sr.RequestError as e:
        print("couldnt request from the server")

    with open (filename,"w") as f:
        f.write(text)

    print("saves as", filename)

def wave1(data,rate):
    samples=np.frombuffer(data,dtype=np.int16)
    time=np.linspace(0,len(samples)/rate, num=len(samples))
    plt.figure(1)
    plt.title("AUDIO")
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.plot(time,samples)
    plt.show()



def main():
    audio_data,rate,width=pressed()
    save1(audio_data,rate,width)
    transcribe(audio_data,rate,width)
    wave1(audio_data,rate)

main()





    
        
