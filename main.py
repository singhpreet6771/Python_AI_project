import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source)
        print('listening...')
        audio = r.listen(source, timeout=5)
    try:
        print('Recognizing....')
        command = r.recognize_google(audio, language="en-in")
        command = command.lower()
        print(command)
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
            return command
    except Exception as e:
        print(e)


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
