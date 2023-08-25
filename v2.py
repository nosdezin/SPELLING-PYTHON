import speech_recognition as sr
import gtts
from playsound import playsound
import random 

def Recog(time):
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Fale!")
        audio_data = r.record(source, duration=time)
        print("Reconhecendo...")
        text = r.recognize_google(audio_data)
        print("o que você falou:",text)

def getWord(file):
    dd = []
    maxl = -1
    with open(file) as f:
        for line in f.readlines():
            dd.append(line.replace("\n",""))
            maxl += 1
    return dd[random.randint(0,maxl)]

isLoop = True
# dict | novasfalas | daytheday | frases
message = getWord("listas/novasfalas.txt")

tts = gtts.gTTS(message)
tts.save(f"audios/{message}.mp3")
playsound(f"audios/{message}.mp3")

while isLoop:
    resp = int(input("[1]ouvir denovo\n[2]desistir\n[3]soletrar\n>>"))
    if resp == 1:
        playsound(f"audios/{message}.mp3")
    elif resp == 2:
        print("Palavra:",message)
        isLoop = False
    else:
        Recog(len(message))
        print("Sua mensagem:",message)
        isLoop = False