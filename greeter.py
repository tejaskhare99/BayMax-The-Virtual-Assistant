import datetime
import pyttsx3
# from inputcomm import inputCommand

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def output(audio):
    # print(audio) # For printing out the output
    engine.say(audio)
    engine.runAndWait()

# output("Hi, What is your name?")
user = "Tejas"
assistant = "Beymax"


def greet():
    hour = datetime.datetime.now().hour
    if (hour >= 6) and (hour < 12):
        output(f"Hello, Good Morning {user}, I am {assistant}. How may I assist you?")
    elif (hour >= 12) and (hour < 18):
        output(f"Hi, Good afternoon {user}, I am {assistant}. How may I assist you?")
    elif (hour >= 18) and (hour < 21):
        output(f"Hey, Good Evening {user}, I am {assistant}. How may I assist you?")