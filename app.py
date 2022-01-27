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
line_bot_api = LineBotApi('TGI+fp/W9YityaQpiRF9OhrAqbP9EZT/GocLhKD11XEuHoiCTmlvDZA6EhTh+mUlhLTgSLwnFe8DRpUQBsWjTWNUhG5O9KnlAbF7IIYWbPbwDgkmm3WJj2iBYyogfmepv6aAB4mlDSw4LEx22zh4WwdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('01bbcb3ed094f619ac3be5b6fe352942')

line_bot_api.push_message('Uc2c240ca992c30a49afa0a29288ee53d', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def handle_message(event):
     message = text=event.message.text
     if re.match('告訴我秘密',message):
         carousel_template_message = TemplateSendMessage(
             alt_text='免費教學影片',
             template=CarouselTemplate(
                 columns=[
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                         title='Python基礎教學',
                         text='萬丈高樓平地起',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='拆解步驟詳細介紹安裝並使用Anaconda、Python、Spyder、VScode…'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=270'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                         title='Line Bot聊天機器人',
                         text='台灣最廣泛使用的通訊軟體',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Line Bot申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2532'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                         title='Telegram Bot聊天機器人',
                         text='唯有真正的方便，能帶來意想不到的價值',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Telegrame申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2648'
                             )
                         ]
                     )
                 ]
             )
         )
         line_bot_api.reply_message(event.reply_token, carousel_template_message)
     else:
         line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
 # 主程式
 import os
 if name == "main":
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port)
