from django.shortcuts import render
import urllib.request
import json


def index(response):
    if response.method == "POST":
        city = response.POST.get("city")
        source = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric"
                                        f"&lang=hi&appid=token_key").read()
        list_of_data = json.loads(source)
        data = {
            "country": str(list_of_data["sys"]["country"]),
            "coordinates": str(list_of_data["coord"]["lon"]) + str(", ") + str(list_of_data["coord"]["lat"]),
            "temp": str(list_of_data["main"]["temp"]) + str("°C"),
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "main": str(list_of_data["weather"][0]["main"]),
            "description": str(list_of_data["weather"][0]["description"]),
            "icon": list_of_data["weather"][0]["icon"],
        }
        return render(response, "weatherapp/index.html", data)
    else:
        return render(response, "weatherapp/index.html", {})
