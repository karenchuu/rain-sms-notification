# ☀️ rain-notification
The goal of this project is to build an Heroku which sends a SMS message every morning to a user's phone, summarising today's rain notification.

## Demo
![](https://raw.githubusercontent.com/karenchuu/oss/main/202208232156575.jpg)
## Features
* Heroku automatically triggered every morning at 8:00 am to send a short SMS message
* SMS message summarises the latest weather forecast for Taipei.
## Built with
* [OpenWeather](https://openweathermap.org/api/one-call-api) - API used to Hourly forecast for 48 hours (Zhongshan Dist., Taipei City weather)
* [Twilio](https://www.twilio.com/) - API used to send SMS messages
* [Heroku](https://dashboard.heroku.com/) - Used to automatically execute Python code every morning.
