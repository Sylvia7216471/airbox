# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:16:35 2021

@author: Ivan
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Line Bot聊天機器人
第四章 選單功能
多樣版組合按鈕CarouselTemplate
"""
#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('0ZtGtrSOwbENt1n2Z0cehZ610JCO8aaojjiqtyOJlpt1/M85m3UpKTWiEpfmx+2vhLTgSLwnFe8DRpUQBsWjTWNUhG5O9KnlAbF7IIYWbPYKh+CLZ9E0c9H4FG0bCfGdpcbajZ42KRQgmexjrNbQzQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('01bbcb3ed094f619ac3be5b6fe352942')

line_bot_api.push_message('Uc2c240ca992c30a49afa0a29288ee53d', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    message2="裝置1\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)"
    yourID = 'Uc2c240ca992c30a49afa0a29288ee53d'
    if re.match('我想選擇裝置',message):
        carousel_template_message = TemplateSendMessage(
            alt_text='多樣版組合按鈕',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='裝置1',
                        text='請點選你想查看的資訊',
                        actions=[
                            PostbackAction(
                              label='環境資料',
                              display_text='環境資料',
                              data='裝置1\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm) '
                            ),
                            URIAction(
                                label='環境影像',
                                uri='https://marketingliveincode.com/?page_id=270'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                        title='裝置2',
                        text='請點選你想查看的資訊',
                        actions=[
                             PostbackAction(
                              label='環境資料',
                              display_text='環境資料',
                             data='裝置2\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm) '
                            ),
                            URIAction(
                                label='環境影像',
                                uri='https://marketingliveincode.com/?page_id=2532'
                            )
                        ]
                    ),
                     CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='裝置3',
                        text='請點選你想查看的資訊',
                        actions=[
                             PostbackAction(
                              label='環境資料',
                              display_text='環境資料',
                              data='裝置3\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm) '
                            ),
                            URIAction(
                                label='環境影像',
                                uri='https://marketingliveincode.com/?page_id=270'
                            )
                        ]
                    ),
                     CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                        title='裝置4',
                        text='請點選你想查看的資訊',
                        actions=[
                             PostbackAction(
                              label='環境資料',
                              display_text='環境資料',
                             data='裝置4\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm) '
                            ),
                            URIAction(
                                label='環境影像',
                                uri='https://marketingliveincode.com/?page_id=270'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                        title='裝置5',
                        text='請點選你想查看的資訊',
                        actions=[
                             PostbackAction(
                              label='環境資料',
                              display_text='環境資料',
                             data='裝置5\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm) '
                            ),
                            URIAction(
                                label='環境影像',
                                uri='https://marketingliveincode.com/?page_id=2648'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.push_message(yourID, 
                          TextSendMessage(text='裝置3\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)'))
        
    elif re.match('環境資料',message):
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)