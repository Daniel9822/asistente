import requests
import os
from dotenv import load_dotenv

class Weather():
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('WEATHER_API_KEY')
        
    def get(self, city):
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.key}")
        if response.status_code == 200:
            print("Todo bien! Respuesta:")
            print(response)
            result = {}
            result["temperatura"] = str(response.json()["main"]["temp"]) + " grados farenheit"
            # result["condicion"] = response.json()["current"]["condition"]["text"]
            return result
            #return response.json()
        else:
            print(f"Oops, algo salió mal al llamar al API del clima. Codigo fue: {response.status_code}")