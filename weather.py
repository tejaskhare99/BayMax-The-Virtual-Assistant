import requests
from greeter import output

def weather():
    city = "ottawa"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")