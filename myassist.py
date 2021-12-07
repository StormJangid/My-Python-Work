import pyttsx3
import wikipedia
import speech_recognition as sr
import os, fnmatch
import webbrowser
import datetime
import random
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def find(pattern, path):
    file = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                file.append(os.path.join(root, name))
    return file


def wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)


def youtube():
    webbrowser.open("youtube.com")


def ongoogle(query):
    if "search" in query:
        query = query.replace("search", "")
    query = query.replace("on google", "")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def google():
    webbrowser.open("google.com")


def yahoo():
    webbrowser.open("yahoo.com")


def music():
    music_dir = "D:\\Audio\\Arijit singh audio\\Arijit Singh Mega Hits (100 Songs) [DJMaza.Life]"
    songs = os.listdir(music_dir)
    l = len(songs) - 1
    rand = random.randrange(0, l)
    print(songs[rand])
    os.startfile(os.path.join(music_dir, songs[rand]))


def musicyt():
    webbrowser.open(
        "https://www.youtube.com/watch?v=gvyUuxdRdR4&list=RDCLAK5uy_n9Fbdw7e6ap-98_A-8JYBmPv64v-Uaq1g&start_radio=1")


def thetime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")


def vscode():
    codePath = "C:\\Users\\darkstorm\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)


def pycharm():
    codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe"
    os.startfile(codePath)


def stackoverflow():
    webbrowser.open("stackoverflow.com")


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            wikipedia(query)

        elif 'open youtube' in query:
            youtube()

        elif 'on google' in query:
            ongoogle(query)

        elif 'open google' in query:
            google()

        elif 'open yahoo' in query:
            yahoo()

        elif 'on youtube' in query or 'on youtube' in query or 'on youtube' in query:
            if 'music on youtube' in query or 'song on youtube' in query or 'songs on youtube' in query:
                musicyt()
            else:
                query = query.replace("play", "")
                query = query.replace("on youtube", "")
                chromedriver = 'C:\\Users\\darkstorm\\Downloads\\chromedriver_win32\\chromedriver.exe'
                driver = webdriver.Chrome(chromedriver)

                query_string = query
                URL = "http://www.youtube.com/results?search_query=" + query_string

                driver.get(URL)

                element = driver.find_element_by_id("thumbnail")

                element.click()

        elif 'play music' in query or 'play song' in query or 'play a song' in query or 'play songs' in query:
            music()

        elif 'the time' in query:
            thetime()

        elif 'open vscode' in query or 'open vs code' in query:
            vscode()

        elif 'open pycharm' in query:
            pycharm()

        elif 'open stackoverflow' in query or 'open stack over flow' in query or 'open stack overflow' in query or \
                'open stackover flow' in query:
            stackoverflow()

        elif 'stop jarvis' in query or 'stop service' in query or 'stop the service' in query:
            break
