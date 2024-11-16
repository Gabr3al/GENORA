import requests
from datetime import datetime
from googlesearch import search

class GeneralFunctions:
    def get_weather(self, city="YOUR_CITY"):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=[YOUR_API_KEY]&units=metric"
        
        try:
            response = requests.get(url)
            weather_data = response.json()
            
            if response.status_code == 200:
                description = weather_data["weather"][0]["description"]
                temperature = weather_data["main"]["temp"]
                feels_like = weather_data["main"]["feels_like"]
                humidity = weather_data["main"]["humidity"]
                city = weather_data["name"]
                country = weather_data["sys"]["country"]

                weather_data = {
                    "description": description,
                    "temperature": temperature,
                    "feels_like": feels_like,
                    "humidity": humidity,
                    "city": city,
                    "country": country
                }
                return weather_data
            else:
                return {"weather":"Unable to retrieve weather data. Response not 200"}
        except Exception as e:
            return {"weather":"Unable to retrieve weather data."}
    
    def google_search(self, query, num_results=3):
        try:
            results = list(search(query, num_results=num_results, advanced=True))
            return [{"title": r.title, "description": r.description, "url": r.url} for r in results]
        except Exception as e:
            print("There was an Error performing a web search")
            return []
        

    



