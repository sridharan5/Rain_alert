import requests
from twilio.rest import Client

api_key = "YOUR API KEY"
lat = 11.738701
lon = 78.960907
account_sid = "YOUR ACCOUNT_SID"
auth_token = "YOUR AUTH_TOKEN"
#Twillio eg number
from_number = "+124845026105"
value = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=value)
weather_details = response.json()
hour = weather_details["hourly"][:12]
weather_id = [i["weather"][0]['id'] for i in hour]
is_rain = False
for egle in weather_id:
    if egle < 700:
        is_rain = True
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella..☂ Alert message from sri code 🙂.",
        from_=from_number,
        to='your number here'
    )
    print(message.status)


