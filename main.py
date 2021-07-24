import requests
import os
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# a random location in Taipei
lat = "25.064262"
lon = "121.520546"

# Call Weather One Call API by hourly
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# register for a free account at https://openweathermap.org/ to get an API key
owp_api_key = os.environ.get("OWM_API_KEY")

# Find these values at https://twilio.com/user/account
twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
send_number = os.environ.get("SEND_NUMBER")
receive_number = os.environ.get("RECEIVE_NUMBER")

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": owp_api_key,
    "exclude": "current,minutely,daily"
}

# Check if it Will Rain in the Next 12 Hours
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
# 確認每個小時的氣象狀態碼是否小於600
# Weather condition codes at https://openweathermap.org/weather-conditions
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 600:
        print("bring an umbrella")
        will_rain = True

if will_rain:
    try:
        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages \
            .create(
            body = "今天可能會下雨，記得要帶雨傘! ☔️",
            from_= send_number,
            to = receive_number
        )
    except TwilioRestException as ex:
        # a generic error message
        print(ex)
        print("Make sure the TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER and TARGET_NUMBER are set properly.")
    else:
        # print the status for verification
        print(message.status)
