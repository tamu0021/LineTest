# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:47:20 2021

@author: iambe
"""

import requests
from bs4 import BeautifulSoup
import urllib.request

class Forecast:
    FORECAST_URL = "https://tenki.jp/forecast/6/30/6200/27100/"
    response = urllib.request.urlopen(FORECAST_URL)
    soup = BeautifulSoup(response, 'html.parser')
    # 天気
    weather = soup.find_all("p", class_="weather_telop")
    # 最高気温
    high_temp = soup.find_all("dd", class_="high-temp temp")
    # 最低気温
    low_temp = soup.find_all("dd", class_="low-temp temp")
    # 降水確率
    rainy_percent = soup.select("tr.rain-probability td")
    # 日にち
    date = soup.find_all("h3", class_="left-style")
    def today_weather(self):
        today_weather = self.date[0].getText() + "\n\n" + self.weather[0].getText()
        today_high_temp = "\n最高" + self.high_temp[0].getText()
        today_low_temp = "\n最低" + self.low_temp[0].getText()
        today_rain_00_06 = "\n\n降水確率\n00-06時" + self.rainy_percent[0].getText()
        today_rain_06_12 = "\n06-12時" + self.rainy_percent[1].getText()
        today_rain_12_18 = "\n12-18時" + self.rainy_percent[2].getText()
        today_rain_18_24 = "\n18-24時" + self.rainy_percent[3].getText()
        
        return (today_weather + today_high_temp + today_low_temp + today_rain_00_06 + today_rain_06_12 + today_rain_12_18 + today_rain_18_24)

class LINENotifyBot:
    API_URL = 'https://notify-api.line.me/api/notify'
    def __init__(self, access_token):
        self.__headers = {'Authorization': 'Bearer ' + access_token}

    def send(
            self, message,
            image=None, sticker_package_id=None, sticker_id=None,
            ):
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
            }
        files = {}
        if image != None:
            files = {'imageFile': open(image, 'rb')}
        r = requests.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
            )
        

forecast = Forecast()
print(forecast.today_weather)

bot = LINENotifyBot(access_token='Write your token.')

bot.send(
    message='Write Your Message',
    image='Test.jpg',  # png or jpg
    sticker_package_id=1,
    sticker_id=13,
    )

