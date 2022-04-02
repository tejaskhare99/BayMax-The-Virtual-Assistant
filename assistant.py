from inputcomm import inputCommand
from greeter import output
import datetime
import os
import psutil
from gk import wolform
from weather import weather
import clipboard
from greeter import greet 
import pyjokes
import pywhatkit
import smtplib
import time as ti
import webbrowser 
from news import news

greet()
while True:
    query = inputCommand().lower()
    if ("time" in query):
        output("Current time is " +
               datetime.datetime.now().strftime("%I:%M"))

    elif ('date' in query):
        output("Current date is " + str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))

    elif ("search" in query):
        output("what you want to search?")
        webbrowser.open("https://www.google.com/search?q="+inputCommand())

    elif ("youtube" in query):
        output("What you want to search on Youtube?")
        pywhatkit.playonyt(inputCommand())

    elif ('weather' in query):
        weather()

    elif ("news" in query):
        news()

    elif ("covid" in query):
        r = requests.get(
            'https://coronavirus-19-api.herokuapp.com/all').json()
        output(
            f'Confirmed Cases: {r["cases"]} \nDeaths: {r["deaths"]} \nRecovered {r["recovered"]}')

    elif "cpu" in query:
        output(f"Cpu is at {str(psutil.cpu_percent())}")

    elif ("joke" in query):
        output(pyjokes.get_joke())


    elif "offline" in query:
        hour = datetime.datetime.now().hour
        if (hour >= 21) and (hour < 6):
            output(f"Good Night {user}! Have a nice Sleep")
        else:
            output(f"Bye {user}, Have a good day")
        quit()

    # else: 
    elif query:
        wolform(query)


        


