import speech_recognition as sr
from greeter import output


def inputCommand():
    # query = input() # For getting input from CLI
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.pause_threshold = 0.8
        try:
            query = r.recognize_google(r.listen(source), language="en-IN")
        except Exception as e:
            output("Sorry I am not trained to handle that command or I could not hear it properly")
    return query
