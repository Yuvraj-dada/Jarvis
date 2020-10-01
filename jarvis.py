import pyttsx3
import datetime
import pyaudio
import wikipedia
import speech_recognition as sr
import random
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wiki(a):
    result=wikipedia.summary(a,sentences=2)
    speak(result)
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morniong sir')
    elif hour>=12 and hour<18:
        speak('good after noon')
    else:
        speak('good eveing')
    speak('I am jarvis sir please tell me how may i help you')

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('recognising...')
        query=r.recognize_google(audio,language='en-in')
        print('user said',query)
    except Exception as e:
        speak('say again please')
        print('say again...')
        return "None"
    return query
wishme()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)
    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

    
def remember():
    speak("what do you want me to remember sir")
    data = takeCommand()
    speak("You told me to remember that " + data)
    remember = open('remember.txt', 'w')
    remember.write(data)
    speak("I remember that now")
    remember.close()
    
    
    
while True:
    query = takecommand().lower()
    if 'wikipedia' in query:
        wiki(query)
    elif ('hey jarvis') in query:
        speak("hello sir,what can i do for you?")
    elif 'who made you' in query:
        speak("Mr.Yuvraj has made me")
     elif 'time' in query:
        time()
    elif 'date' in query:
        date()
    elif 'remember ' in query:
        remember()
        speak("do you want me to remember something new sir?")
        ask = takeCommand()
        if (ask == 'yes'):
            remember()
        else:
            quit()
    elif 'exit' in query:
        speak("Ok sir exiting")
        quit()
