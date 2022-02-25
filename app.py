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
result_1 = cursor1.fetchone()
result1_1=result_1[1]
result2_1=result_1[2]
result3_1=result_1[3]
result4_1=result_1[4]
result5_1=result_1[5]
result6_1=result_1[6]
result7_1=result_1[7]
result8_1=result_1[8]
result9_1=result_1[9]
result10_1=result_1[10]
result11_1=result_1[11]

cursor2 = db.cursor()
cursor2.execute("SELECT * FROM device_2 ORDER BY time DESC LIMIT 1")
result_2 = cursor2.fetchone()
result1_2=result_2[1]
result2_2=result_2[2]
result3_2=result_2[3]
result4_2=result_2[4]
result5_2=result_2[5]
result6_2=result_2[6]
result7_2=result_2[7]
result8_2=result_2[8]
result9_2=result_2[9]
result10_2=result_2[10]
result11_2=result_2[11]

cursor3 = db.cursor()
cursor3.execute("SELECT * FROM device_3 ORDER BY time DESC LIMIT 1")
result_3 = cursor3.fetchone()
result1_3=result_3[1]
result2_3=result_3[2]
result3_3=result_3[3]
result4_3=result_3[4]
result5_3=result_3[5]
result6_3=result_3[6]
result7_3=result_3[7]
result8_3=result_3[8]
result9_3=result_3[9]
result10_3=result_3[10]
result11_3=result_3[11]

cursor4 = db.cursor()
cursor4.execute("SELECT * FROM device_4 ORDER BY time DESC LIMIT 1")
result_4 = cursor4.fetchone()
result1_4=result_4[1]
result2_4=result_4[2]
result3_4=result_4[3]
result4_4=result_4[4]
result5_4=result_4[5]
result6_4=result_4[6]
result7_4=result_4[7]
result8_4=result_4[8]
result9_4=result_4[9]
result10_4=result_4[10]
result11_4=result_4[11]

cursor5 = db.cursor()
cursor5.execute("SELECT * FROM device_5 ORDER BY time DESC LIMIT 1")
result_5 = cursor5.fetchone()
result1_5=result_5[1]
result2_5=result_5[2]
result3_5=result_5[3]
result4_5=result_[4]
result5_5=result_5[5]
result6_5=result_5[6]
result7_5=result_5[7]
result8_5=result_5[8]
result9_5=result_5[9]
result10_5=result_5[10]
result11_5=result_5[11]

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
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result1_1)+'\n'+'溫度: '+str(result2_1)+'˚C'+'\n'+'濕度: '+str(result3_1)+'RH'+'\n'+'PM1: '+str(result4_1)+'μg/m3'+'\n'+'PM25: '+str(result5_1)+'μg/m3'+'\n'+'PM10: '+str(result6_1)+'μg/m3'+'\n'+'MQ3: '+str(result7_1)+'μg/L'+'\n'+'MQ10: '+str(result8_1)+'μg/L'+'\n'+'MQ135: '+str(result9_1)+'μg/L')) 
    elif re.match('環境資料2',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result1_2)+'\n'+'溫度: '+str(result2_3)+'˚C'+'\n'+'濕度: '+str(result3_2)+'RH'+'\n'+'PM1: '+str(result4_2)+'μg/m3'+'\n'+'PM25: '+str(result5_2)+'μg/m3'+'\n'+'PM10: '+str(result6_2)+'μg/m3'+'\n'+'MQ3: '+str(result7_2)+'μg/L'+'\n'+'MQ10: '+str(result8_2)+'μg/L'+'\n'+'MQ135: '+str(result9_2)+'μg/L'))
    elif re.match('環境資料3',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result1_3)+'\n'+'溫度: '+str(result2_3)+'˚C'+'\n'+'濕度: '+str(result3_3)+'RH'+'\n'+'PM1: '+str(result4_3)+'μg/m3'+'\n'+'PM25: '+str(result5_3)+'μg/m3'+'\n'+'PM10: '+str(result6_3)+'μg/m3'+'\n'+'MQ3: '+str(result7_3)+'μg/L'+'\n'+'MQ10: '+str(result8_3)+'μg/L'+'\n'+'MQ135: '+str(result9_3)+'μg/L'))
    elif re.match('環境資料4',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result1_4)+'\n'+'溫度: '+str(result2_4)+'˚C'+'\n'+'濕度: '+str(result3_4)+'RH'+'\n'+'PM1: '+str(result4_4)+'μg/m3'+'\n'+'PM25: '+str(result5_4)+'μg/m3'+'\n'+'PM10: '+str(result6_4)+'μg/m3'+'\n'+'MQ3: '+str(result7_4)+'μg/L'+'\n'+'MQ10: '+str(result8_4)+'μg/L'+'\n'+'MQ135: '+str(result9_4)+'μg/L'))
    elif re.match('環境資料5',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result1_5)+'\n'+'溫度: '+str(result2_5)+'˚C'+'\n'+'濕度: '+str(result3_5)+'RH'+'\n'+'PM1: '+str(result4_5)+'μg/m3'+'\n'+'PM25: '+str(result5_5)+'μg/m3'+'\n'+'PM10: '+str(result6_5)+'μg/m3'+'\n'+'MQ3: '+str(result7_5)+'μg/L'+'\n'+'MQ10: '+str(result8_5)+'μg/L'+'\n'+'MQ135: '+str(result9_5)+'μg/L'))
     
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
