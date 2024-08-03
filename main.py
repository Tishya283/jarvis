import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests
recognizer=sr.Recognizer()
engine=pyttsx3.init()
# newsapi="24e73fcaabf64dc7ad0cfc758cacd08e"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open watsapp" in c.lower():
        webbrowser.open("https://watsapp.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link =music.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=24e73fcaabf64dc7ad0cfc758cacd08e")
        if r.status_code == 200:
            headlines = r.json()
            titles = [article['title'] for article in headlines['articles']]    
            for title in titles:
                speak(title)

    # else:

        


if __name__=="__main__":
    speak("Initializing jarvis....")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        # recognize speech using Sphinx
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yaa")
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
            
    
        except Exception as e:
            print("error; {0}".format(e))
