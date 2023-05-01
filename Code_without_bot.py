import requests
import datetime
import os

api_weather_token = os.getenv('api_weather_token')

def get_weather(city, api_weather_token):

    weather_on_sky = {
    "Clear": "Ясно",
    "Clouds": "Облачно",
    "Rain": "Дождь",
    "Drizzle": "Морось",
    "Thunderstorm": "Гроза",
    "Snow": "Снег",
    "Mist": "Туман"
    }

    try:
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_weather_token}&units=metric")
        weather_json = req.json()

        city = weather_json["name"]
        cur_weather = weather_json["main"]["temp"]

        weather_description = weather_json["weather"][0]["main"]
        if weather_description in weather_on_sky:
            wd = weather_on_sky[weather_description]
        else:
            wd = "Погода слишком непредсказуемая =("

        humidity = weather_json["main"]["humidity"]
        pressure =  round((weather_json["main"]["pressure"] / 1.333), 2)
        wind = weather_json["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(weather_json["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(weather_json["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(weather_json["sys"]["sunset"]) - datetime.datetime.fromtimestamp(weather_json["sys"]["sunrise"])

        print(f"Сейчас: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f"Погода в городе: {city}\nТемпература: {cur_weather} C° {wd}\nВлажность: {humidity} %\n"
              f"Давление: {pressure} мм.рт.ст\nВетер: {wind} м/с\nВосход солнца: {sunrise_timestamp}\n"
              f"Закат солнца: {sunset_timestamp}\nПродолжительность дня: {lenght_of_the_day}\n"
              f"Хорошоего дня и надевайтесь по погоде =)"
              )

    except Exception as ex:
        print(ex)
        print('Проверьте название города')



def main():
    city = input('Введите город: ')
    get_weather(city, api_weather_token)

if __name__ == '__main__':
    main()
