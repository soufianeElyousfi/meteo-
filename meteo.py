import json
import requests


def loadWeather():
    city_name = input("Enter city name: ")
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    completUrl=base_url + "appid=" + api_key+ "&q=" + city_name
    response = requests.get(completUrl)
    data = json.loads(response.text)
    if data["cod"] != "404":
        temp=data['main']['temp']-273.15
        tempMin=data['main']['temp_min']-273.15
        tempMax=data['main']['temp_max']-273.15
        print("\n la temperature actuel %d C"
              "\n la temperature min =%d C"
              "\n la temperature max =%d C"
              %(temp,tempMin,tempMax))
    else:
        print(" City Not Found ")



if __name__ == "__main__":
  api_key = '6e5521baa48d790a72fc79a869c9e746'
  while True:
      loadWeather()
