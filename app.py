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
import os
import datetime
import pymysql

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('0ZtGtrSOwbENt1n2Z0cehZ610JCO8aaojjiqtyOJlpt1/M85m3UpKTWiEpfmx+2vhLTgSLwnFe8DRpUQBsWjTWNUhG5O9KnlAbF7IIYWbPYKh+CLZ9E0c9H4FG0bCfGdpcbajZ42KRQgmexjrNbQzQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('01bbcb3ed094f619ac3be5b6fe352942')

line_bot_api.push_message('Uc2c240ca992c30a49afa0a29288ee53d', TextSendMessage(text='HI'))


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

#資料庫連線設定
db = pymysql.connect(host='us-cdbr-east-05.cleardb.net', port='', user='b27ce87b980a11', passwd='167961db', database = "heroku_5ce6e6298fde0f2")

cursor1 = db.cursor()
cursor1.execute("SELECT * FROM device_1 ORDER BY time DESC LIMIT 1")
result1 = cursor1.fetchone()
result11=result1[1]
result21=result1[2]
result31=result1[3]
result41=result1[4]
result51=result1[5]
result61=result1[6]
result71=result1[7]
result81=result1[8]
result91=result1[9]
result101=result1[10]
result111=result1[11]

cursor2 = db.cursor()
cursor2.execute("SELECT * FROM device_2 ORDER BY time DESC LIMIT 1")
result2 = cursor2.fetchone()
result12=result2[1]
result22=result2[2]
result32=result2[3]
result42=result2[4]
result52=result2[5]
result62=result2[6]
result72=result2[7]
result82=result2[8]
result92=result2[9]
result102=result2[10]
result112=result2[11]

cursor3 = db.cursor()
cursor3.execute("SELECT * FROM device_3 ORDER BY time DESC LIMIT 1")
result3 = cursor3.fetchone()
result13=result3[1]
result23=result3[2]
result33=result3[3]
result43=result3[4]
result53=result3[5]
result63=result3[6]
result73=result3[7]
result83=result3[8]
result93=result3[9]
result103=result3[10]
result113=result3[11]

cursor4 = db.cursor()
cursor4.execute("SELECT * FROM device_4 ORDER BY time DESC LIMIT 1")
result4 = cursor4.fetchone()
result14=result4[1]
result24=result4[2]
result34=result4[3]
result44=result4[4]
result54=result4[5]
result64=result4[6]
result74=result4[7]
result84=result4[8]
result94=result4[9]
result104=result4[10]
result114=result4[11]

cursor5 = db.cursor()
cursor5.execute("SELECT * FROM device_5 ORDER BY time DESC LIMIT 1")
result5 = cursor5.fetchone()
result15=result5[1]
result25=result5[2]
result35=result5[3]
result45=result5[4]
result55=result5[5]
result65=result5[6]
result75=result5[7]
result85=result5[8]
result95=result5[9]
result105=result5[10]
result115=result5[11]

db.close()

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
                             URITemplateAction(
                               label='動態影像1',
                               uri='http://192.168.0.4:9601/stream'
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
                               URITemplateAction(
                               label='動態影像2',
                               uri='http://192.168.0.6:9601/stream'
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
                             URITemplateAction(
                               label='動態影像3',
                               uri='http://192.168.0.8:9601/stream'
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
                             URITemplateAction(
                               label='動態影像4',
                               uri='http://192.168.0.10:9601/stream'
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
                             URITemplateAction(
                               label='動態影像5',
                               uri='http://192.168.0.12:9601/stream'
                             )
                        ]
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    elif re.match('環境資料1',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result11)+'\n'+'溫度: '+str(result21)+'˚C'+'\n'+'濕度: '+str(result31)+'RH'+'\n'+'PM1: '+str(result41)+'μg/m3'+'\n'+'PM25: '+str(result51)+'μg/m3'+'\n'+'PM10: '+str(result61)+'μg/m3'+'\n'+'MQ3: '+str(result71)+'μg/L'+'\n'+'MQ10: '+str(result81)+'μg/L'+'\n'+'MQ135: '+str(result91)+'μg/L')) 
    elif re.match('環境資料2',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result12)+'\n'+'溫度: '+str(result22)+'˚C'+'\n'+'濕度: '+str(result32)+'RH'+'\n'+'PM1: '+str(result42)+'μg/m3'+'\n'+'PM25: '+str(result52)+'μg/m3'+'\n'+'PM10: '+str(result62)+'μg/m3'+'\n'+'MQ3: '+str(result72)+'μg/L'+'\n'+'MQ10: '+str(result82)+'μg/L'+'\n'+'MQ135: '+str(result92)+'μg/L'))
    elif re.match('環境資料3',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result13)+'\n'+'溫度: '+str(result23)+'˚C'+'\n'+'濕度: '+str(result33)+'RH'+'\n'+'PM1: '+str(result43)+'μg/m3'+'\n'+'PM25: '+str(result53)+'μg/m3'+'\n'+'PM10: '+str(result63)+'μg/m3'+'\n'+'MQ3: '+str(result73)+'μg/L'+'\n'+'MQ10: '+str(result83)+'μg/L'+'\n'+'MQ135: '+str(result93)+'μg/L'))
    elif re.match('環境資料4',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result14)+'\n'+'溫度: '+str(result24)+'˚C'+'\n'+'濕度: '+str(result34)+'RH'+'\n'+'PM1: '+str(result44)+'μg/m3'+'\n'+'PM25: '+str(result54)+'μg/m3'+'\n'+'PM10: '+str(result64)+'μg/m3'+'\n'+'MQ3: '+str(result74)+'μg/L'+'\n'+'MQ10: '+str(result84)+'μg/L'+'\n'+'MQ135: '+str(result94)+'μg/L'))
    elif re.match('環境資料5',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result15)+'\n'+'溫度: '+str(result25)+'˚C'+'\n'+'濕度: '+str(result35)+'RH'+'\n'+'PM1: '+str(result45)+'μg/m3'+'\n'+'PM25: '+str(result55)+'μg/m3'+'\n'+'PM10: '+str(result65)+'μg/m3'+'\n'+'MQ3: '+str(result75)+'μg/L'+'\n'+'MQ10: '+str(result85)+'μg/L'+'\n'+'MQ135: '+str(result95)+'μg/L'))
     
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
            latitude=float(result10),
            longitude=float(result12)
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
