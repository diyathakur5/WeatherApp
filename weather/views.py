import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(request):
    api_key = "94d46257097ff7cf8c1fe8b81c9fc2c6"  # Replace with your API key
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['name']  # Get city name from form
            response = requests.get(url.format(city, api_key)).json()  # Fetch data from API

            if response.get("cod") != 200:
                weather_data = {"error": "City not found!"}
            else:
                weather_data = {
                    "city": city,
                    "temperature": response["main"]["temp"],
                    "description": response["weather"][0]["description"],
                    "icon": response["weather"][0]["icon"],
                }
            return render(request, "weather.html", {"weather": weather_data, "form": form})

    else:
        form = CityForm()

    return render(request, "weather.html", {"form": form})
