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

import datetime

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
    loc_dt = datetime.datetime.today() 
    time_del = datetime.timedelta(hours=8) 
    new_dt = loc_dt + time_del 
    datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
    loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
 #  message2="裝置1\n更新時間:\n溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)"
    yourID = 'Uc2c240ca992c30a49afa0a29288ee53d'
    if re.match('我想選擇裝置',message):
        carousel_template_message = TemplateSendMessage(
            alt_text='多樣版組合按鈕',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1875/1875043.png',
                        title='裝置1',
                        text='請點選你想查看的資訊',
                        actions=[
                             MessageTemplateAction(
                               label='環境資料1',
                               text='環境資料1'
                             ),
                             MessageTemplateAction(
                               label='裝置位置1',
                               text='裝置位置1'
                             ),
                             MessageTemplateAction(
                               label='環境影像1',
                               text='環境影像1'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1874/1874965.png',
                        title='裝置2',
                        text='請點選你想查看的資訊',
                        actions=[
                             MessageTemplateAction(
                               label='環境資料2',
                               text='環境資料2'
                             ),
                             MessageTemplateAction(
                               label='裝置位置2',
                               text='裝置位置2'
                             ),
                             MessageTemplateAction(
                               label='環境影像2',
                               text='環境影像2'
                            )
                        ]
                    ),
                     CarouselColumn(
                        thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1875/1875078.png',
                        title='裝置3',
                        text='請點選你想查看的資訊',
                        actions=[
                             MessageTemplateAction(
                               label='環境資料3',
                               text='環境資料3'
                             ),
                             MessageTemplateAction(
                               label='裝置位置3',
                               text='裝置位置3'
                             ),
                             MessageTemplateAction(
                               label='環境影像3',
                               text='環境影像3'
                            )
                        ]
                    ),
                     CarouselColumn(
                        thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1874/1874996.png',
                        title='裝置4',
                        text='請點選你想查看的資訊',
                        actions=[
                             MessageTemplateAction(
                               label='環境資料4',
                               text='環境資料4'
                             ),
                             MessageTemplateAction(
                               label='裝置位置4',
                               text='裝置位置4'
                             ),
                             MessageTemplateAction(
                               label='環境影像4',
                               text='環境影像4'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1875/1875006.png',
                        title='裝置5',
                        text='請點選你想查看的資訊',
                        actions=[
                            MessageTemplateAction(
                               label='環境資料5',
                               text='環境資料5'
                             ),
                             MessageTemplateAction(
                               label='裝置位置5',
                               text='裝置位置5'
                             ),
                             MessageTemplateAction(
                               label='環境影像5',
                               text='環境影像5'
                            )
                        ]
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    elif re.match('環境資料1',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(str(datetime_format)))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(text='溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)'))
    elif re.match('環境資料2',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(str(datetime_format)))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(text='溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)'))
    elif re.match('環境資料3',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(str(datetime_format)))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(text='溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)'))
    elif re.match('環境資料4',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(str(datetime_format)))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(text='溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)'))
    elif re.match('環境資料5',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(str(datetime_format)))
        line_bot_api.push_message(yourID, 
                          TextSendMessage(text='溫度:\n濕度:\n懸浮粒子(ug/m3)\nPM1:\nPM2.5:\nPM10:\n氣體感測\nMQ3:(ug/L)\nMQ7:(ppm)\nMQ135:(ppm)'))
    elif re.match('裝置位置1',message):
        location_message = LocationSendMessage(
            title='裝置1目前的所在位置',
            address='總統府',
            latitude=25.040213810016002,
            longitude=121.51238385108306
        )
        line_bot_api.reply_message(event.reply_token,location_message)
    elif re.match('裝置位置2',message):
        location_message = LocationSendMessage(
            title='裝置2目前的所在位置',
            address='總統府',
            latitude=25.040213810016002,
            longitude=121.51238385108306
        )
        line_bot_api.reply_message(event.reply_token,location_message)
    elif re.match('裝置位置3',message):
        location_message = LocationSendMessage(
            title='裝置3目前的所在位置',
            address='總統府',
            latitude=25.040213810016002,
            longitude=121.51238385108306
        )
        line_bot_api.reply_message(event.reply_token,location_message)
    elif re.match('裝置位置4',message):
        location_message = LocationSendMessage(
            title='裝置4目前的所在位置',
            address='總統府',
            latitude=25.040213810016002,
            longitude=121.51238385108306
        )
        line_bot_api.reply_message(event.reply_token,location_message)
    elif re.match('裝置位置5',message):
        location_message = LocationSendMessage(
            title='裝置5目前的所在位置',
            address='總統府',
            latitude=25.040213810016002,
            longitude=121.51238385108306
        )
        line_bot_api.reply_message(event.reply_token,location_message)
    elif re.match('環境影像1',message):
        image_message = ImageSendMessage(
        original_content_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA=',
        preview_image_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA='
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('環境影像2',message):
        image_message = ImageSendMessage(
        original_content_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA=',
        preview_image_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA='
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('環境影像3',message):
        image_message = ImageSendMessage(
        original_content_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA=',
        preview_image_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA='
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('環境影像4',message):
        image_message = ImageSendMessage(
        original_content_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA=',
        preview_image_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA='
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif re.match('環境影像5',message):
        image_message = ImageSendMessage(
        original_content_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA=',
        preview_image_url='https://media.istockphoto.com/illustrations/tapir-illustration-id1128835465?k=20&m=1128835465&s=612x612&w=0&h=o5rGp2t8zFGLj_BrSqWes-d1DqeWtM3Z-_rQU73jfzA='
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
