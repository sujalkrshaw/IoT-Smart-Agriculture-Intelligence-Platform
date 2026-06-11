import requests
import random
import time

API_KEY = "0KHV2ZAZYJDCFE85"

temperature = random.randint(22,40)
humidity = random.randint(40,90)
soil = random.randint(0,4095)
water = random.randint(0,4095)

pump = 1 if soil < 2000 else 0

url = "https://api.thingspeak.com/update"

payload = {
    "api_key": API_KEY,
    "field1": temperature,
    "field2": humidity,
    "field3": soil,
    "field4": water,
    "field5": pump
}

response = requests.post(url, data=payload)

print("ThingSpeak Response:", response.text)

print("ThingSpeak Response:", response.text)

time.sleep(15)