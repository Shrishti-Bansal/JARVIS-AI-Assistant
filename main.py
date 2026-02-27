import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime

# -------- Text To Speech Setup --------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 185)


def speak(audio):
    print("Assistant:", audio)
    engine.say(audio)
    engine.runAndWait()


# -------- Speech Recognition --------
def command():
    content = " "
    
    while content==" ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something...")
            #r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("You said....", content)
            return content.lower()

        except Exception as e:
            print("Sorry, I did not understand.")
    
    return content

        


# -------- Main Assistant --------
def main_process():

    

    while True:
        request = command().lower()


        if "hello" in request:
            speak("Welcome, how are you doing?")

        elif "play music" in request:
            speak("Playing music for you")
            song = random.randint(1, 3)

            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=3tmd-ClpJxA")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g")
            else:
                webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")

        elif "time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + now_time)

        elif "date" in request:
            now_date = datetime.datetime.now().strftime("%d/%m/%Y")
            speak("Current date is " + now_date)

        elif "exit" in request or "stop" in request:
            speak("Goodbye")
            break


main_process()