import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=6,phrase_time_limit=5)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


#To wish
def wish():
    hour= int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning, sir")

    elif hour>12 and hour<18:
        speak("good afternoon, sir")

    else:
        speak("good evening, sir")
    speak("Sir, I am Jarvis ,Please tell me How I can help you")

#To send mail
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("madhav04042001@gmail.com", "Agent@047")
    server.sendmail("madhav04042001@gmail.com", to, content)
    server.close()



if __name__=="__main__":
    wish()
    #takecommand()
    #speak("Hi ,Sir")
    while True:
    #while():


        query = takecommand().lower()

        #logic building tasks

        if "open notepad" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "F:\\Music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "find my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f" you ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open geeksforgeeks" in query:
            webbrowser.open("www.geeksforgeeks.com")

        elif "open github" in query:
            webbrowser.open("www.github.com")

        elif "open omegle" in query:
            webbrowser.open("www.omegle.com")

        elif "open google" in query:
            speak("sir, what should search for you ")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+917974095152", "this message is sent my mr.mayank through jarvis ",11,4)

        elif "play songs on youtube " in query:
            kit.playonyt("see you again")

        elif "send email to mayank" in query:
            try:
                speak("what should I say?")
                content = takecommand().lower()
                to = "madhav04042001@gmail.com"
                sendEmail(to,content)
                speak("Sir, Email has been sent to mr.mayank")

            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to sent this mail to mr.mayank ")


        elif "no thanks" in query:
            speak("thanks for using me sir, have a nice time")
            sys.exit()

        speak("sir, do you have another work")


