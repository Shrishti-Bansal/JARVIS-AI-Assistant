import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib, ssl
import openai_request as ai

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
        
        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")

        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        
        elif "wikipedia" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search wikipedia ", "")
            print(request)
            result = wikipedia.summary(request, sentences=2)
            print(result)
            speak(result)
        
        elif "search google" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search google ", "")
            webbrowser.open("https://www.google.com/search?q=" + request)
        
        elif "send whatsapp message" in request:
            pwk.sendwhatmsg("+910123456789", "Hi, what's up?", 2,3, 30)
            speak("Message sent successfully")
        
        # elif "send mail" in request:
        #     pwk.send_mail("absdolly@254gmail.com", user_config.user_pass, "For", "This is a test email", "xyz@254gmail.com")
        #     speak("Email sent successfully")
        
        elif "send email" in request:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("absdolly@254gmail.com", user_config.gmail_password)
            message = """
                This is the message.

                Thanks by Kode Gurukul.

                """
            s.sendmail("absdolly@254gmail.com", "xyz@254gmail.com", message)
            s.quit()
            speak("Email sent")
        
        elif "ask gpt" in request:
            request = request.replace("jarvis ", "")
            request = request.replace("search gpt ", "")
            print(request)
            response = ai.send_request_to_gpt(request)
            print(response)
            speak(response)
        
        elif "exit" in request or "stop" in request:
            speak("Goodbye")
            break


main_process()