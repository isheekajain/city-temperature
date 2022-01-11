import requests
from django.shortcuts import render
from .forms import UserForm
from django.core.mail import send_mail

API_KEY = "your api key"
API_ADDRESS = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q="


# Create your views here.
def home(request):
    form = UserForm
    return render(request, "index.html", {'form': form})


def sending_mail(request):

    global icon
    form = UserForm(request.POST)
    name = request.POST.get('username').title()
    email = request.POST.get('email')
    city = request.POST.get('city')
    url = API_ADDRESS+city
    json_data = requests.get(url).json()
    temperature = round(json_data['main']['temp'] - 273.15, 2)
    weather_id = json_data['weather'][0]['id']
    # weather = json_data['weather'][0]['description']

    if form.is_valid():
        form.save()

        if weather_id >= 200:
            icon = '⛈'
        elif weather_id >= 300:
            icon = "🌧️"
        elif weather_id >= 500:
            icon = "🌧️"
        elif weather_id >= 600:
            icon = "❄"
        elif weather_id >= 700:
            icon = "🌫️"
        elif weather_id >= 800:
            icon = "☁"
        subject = f'Hi {name}, interested in our services'
        message = f'The temperature in {city} is {temperature} degree celcius {icon}'
        send_mail(
            subject,
            message,
            'eshpractice@gmail.com',
            [email],
            fail_silently=False,
        )
    return render(request, "confirm.html")
