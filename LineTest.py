# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:47:20 2021

@author: iambe
"""

import requests

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
        

bot = LINENotifyBot(access_token='Write your token.')

bot.send(
    message='Write Your Message',
    image='Test.png',  # png or jpg
    sticker_package_id=1,
    sticker_id=13,
    )

