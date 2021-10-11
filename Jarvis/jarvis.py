import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("good morning")
        speak("good morning")

    elif hour>=12 and hour<18:
        print("good afternoon")
        speak("good afternoon")

    else:
        print("good evening")
        speak("good evening")

def takecommand():
    # it takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Rcognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
        
    except Exception as e:
        print(e)

        print("say that again please")
        return "none"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.helo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    print("hello, i am jarvis. welcome to my world")
    speak("hello, i am jarvis. welcome to my world")
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentencess=2)
            speak("according to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\\rohit\\music\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        elif 'email to rohit' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "rohit75870@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend rohit. I am not able to send this email")   
