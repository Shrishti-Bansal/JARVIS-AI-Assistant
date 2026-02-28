import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification

# -------- Text To Speech Setup --------
def speak(audio):
    print("Assistant:", audio)
   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 1.0)


    engine.say(audio)
    engine.runAndWait()
    engine.stop()

# -------- Speech Recognition --------
def command():
    content = " "
    
    while content==" ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("You said....", content)
            return content.lower()

        except Exception as e:
            print("Sorry, I did not understand.")
            return None
   
    return content

        


# -------- Main Assistant --------
def main_process():

    speak("Jarvis activated")

    while True:
        request = command()
        if request is None:
            continue
        request = request.lower()

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
            speak("Current time is " + str(now_time))

        elif "date" in request:
            now_date = datetime.datetime.now().strftime("%d/%m/%Y")
            speak("Current date is " + str(now_date))
        
        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task!="":
                speak("Adding task:" + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "show tasks" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.readlines()

                if not tasks:
                    speak("No tasks available")
                else:
                    speak("Here are your tasks")
                    for task in tasks:
                        speak(task)

            except FileNotFoundError:
                speak("Task list not found")
        
        elif "show work" in request:
            with open("todo.txt", "r") as file:
                    task=file.read()
            notification.notify(
                title="Today's work",
                message=task
            )
        elif "exit" in request or "stop" in request:
            speak("Goodbye")
            break


main_process()