import pyttsx3

engine = pyttsx3.init()

print("Welcome to RoboSpeaker 1.1. Created by Sharath Nair")
while True:
    text = input("Enter the text: ")
    if text == "stop":
        break
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
