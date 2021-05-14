import requests
import json
import sqlite3

city = input("შეიყვანეთ ქალაქის სახელი:")
key = "995f9cc15bfc6d67e8744e5a3ea39156"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

res = requests.get(url)

print(" Status Code: ", res.status_code, '\n', "Header", res.headers)

print(res)

resource = json.loads(res.text)
resp_json_structured = json.dumps(resource, indent=4)
with open ("Weather.json", "w") as file:
    json.dump(resource, file, indent=4)

temp = resource['main']['temp']
humidity = resource['main']['humidity']
wind_speed = resource['wind']['speed']
celsiuse = round(temp - 273.15, 0)
print(f'ტემპერატურა:{int(celsiuse)}C')
print(f'ტენიანობა:{humidity}%')
print(f'ქარის სიჩქარე:{wind_speed} მ/წ')

conn = sqlite3.connect("weather.sqlite")
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE Weather
#                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  CityName VARCHAR(50),
#                  Temp VARCHAR(50),
#                  Humidity VARCHAR(50),
#                  WindSpeed VARCAR(50));''')

cursor.execute("INSERT INTO Weather (CityName, Temp, Humidity, WindSpeed) VALUES (?, ?, ?, ?)", (city, celsiuse, humidity, wind_speed))
conn.commit()
conn.close()