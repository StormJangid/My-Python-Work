import requests
import json

b = requests.get(
    "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=fb95d9890b044400babba855591efbf3")
a = json.loads(b.text)
articles = a["articles"]


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    speak("News of today")
    i = 1
    for article in articles:
        print(f"{i}.{article['title']}")
        speak(article["title"])
        speak("Going on Next News.")
        i = i + 1
