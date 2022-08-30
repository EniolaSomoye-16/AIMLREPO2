import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import datetime 
import calendar
import wikipedia
# import pywhatkit
import playsound
import pyjokes

# to make it accept commands
def acceptCommands():
    # to make it recognize the commands correlating with the audio
    r = sr.Recognizer()
    # connnecting with the microphone of the computer
    with sr.Microphone() as source:
        # output to show if it could hear what the user is saying
        print('Listening....')
        # playsound("ontone.mp3")
        # r.pause_threshold = 0.8
        audio = r.listen(source)
        
        # We want the virtual assistant to act according to the commands given
    try:
        print('Recognizing....')
        # To understand the language i am using, so we have to set a query.
        Query = r.recognize_google(audio, language ='en-in')
    except Exception as e:
        print(e)
        return 'None'
    return Query

# the next thing is to define another function, the speak commands
def speak(audio):
    # using the pyttsx3 to activate the engine
    engine = pyttsx3.init()
    # using this to get the voice be it a male or a female eg; Quartana
    voices = engine.getProperty('voices')
# using another command to search for the voice
    engine.setProperty('voice',voices[0].id)
    # to make the virtual assistant speak
    engine.say(audio)
    # this method will accept the command which allow it to execute the commands
    engine.runAndWait()
    
    
def welcome():
    speak('Welcome!, I am Techna How may I help you?')
    
    # using some commands to enable to speak out, for example tell us the day
def tellDay():
    day = datetime.date.today()
    # to make the virtual assistant tell us the day and time according to the calendar
    speak(calendar.day_name[day.weekday()])
    
    # this is creating a query that makes it accept the commands
def AcceptQuery():
    # calling the greeting function we have created before
    welcome()
    # when it is true, let it do this
    while(True):
        query = acceptCommands().lower()
        
    while True:
        if "hello techna" in listen():
                playsound("ontone.mp3")
        
        if 'what day is it' in query:
            tellDay()
            continue
        
        
        else:
            speak("I am lost")
        # this is used to execute the codes
if __name__ == '__main__':
    AcceptQuery()

    
    
     
    
    
        
            
        