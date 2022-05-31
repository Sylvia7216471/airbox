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

def aqi(num):
    if(num <=50): aqi1 ='良好'
    elif(num > 50 and num <= 100):aqi1 ='普通'
    elif(num >100 and num <= 150):aqi1='不良'
    elif(num >150 and num <= 200):aqi1 ='不健康'
    elif(num >200 ):aqi1 ='危害'
    return aqi1

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

point11=aqi(result1[4])
point12=aqi(result1[5])
point13=aqi(result1[6])
point14=aqi(result1[7])
point15=aqi(result1[8])
point16=aqi(result1[9])

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

point21=aqi(result2[4])
point22=aqi(result2[5])
point23=aqi(result2[6])
point24=aqi(result2[7])
point25=aqi(result2[8])
point26=aqi(result2[9])


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

point31=aqi(result3[4])
point32=aqi(result3[5])
point33=aqi(result3[6])
point34=aqi(result3[7])
point35=aqi(result3[8])
point36=aqi(result3[9])

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

point41=aqi(result4[4])
point42=aqi(result4[5])
point43=aqi(result4[6])
point44=aqi(result4[7])
point45=aqi(result4[8])
point46=aqi(result4[9])

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

point51=aqi(result5[4])
point52=aqi(result5[5])
point53=aqi(result5[6])
point54=aqi(result5[7])
point55=aqi(result5[8])
point56=aqi(result5[9])

############################################歷史資料第1筆###############################################
cursor11 = db.cursor()
cursor11.execute("SELECT * FROM device_1 ORDER BY time DESC LIMIT 1,1")
frist1 = cursor11.fetchone()
frist11=frist1[1]
frist21=frist1[2]
frist31=frist1[3]
frist41=frist1[4]
frist51=frist1[5]
frist61=frist1[6]
frist71=frist1[7]
frist81=frist1[8]
frist91=frist1[9]
frist101=frist1[10]
frist111=frist1[11]


cursor12 = db.cursor()
cursor12.execute("SELECT * FROM device_2 ORDER BY time DESC LIMIT 1,1")
frist2 = cursor12.fetchone()
frist12=frist2[1]
frist22=frist2[2]
frist32=frist2[3]
frist42=frist2[4]
frist52=frist2[5]
frist62=frist2[6]
frist72=frist2[7]
frist82=frist2[8]
frist92=frist2[9]
frist102=frist2[10]
frist112=frist2[11]

cursor13 = db.cursor()
cursor13.execute("SELECT * FROM device_3 ORDER BY time DESC LIMIT 1,1")
frist3 = cursor13.fetchone()
frist13=frist3[1]
frist23=frist3[2]
frist33=frist3[3]
frist43=frist3[4]
frist53=frist3[5]
frist63=frist3[6]
frist73=frist3[7]
frist83=frist3[8]
frist93=frist3[9]
frist103=frist3[10]
frist113=frist3[11]

cursor14 = db.cursor()
cursor14.execute("SELECT * FROM device_4 ORDER BY _AI DESC LIMIT 1,1")
frist4 = cursor14.fetchone()
frist14=frist4[1]
frist24=frist4[2]
frist34=frist4[3]
frist44=frist4[4]
frist54=frist4[5]
frist64=frist4[6]
frist74=frist4[7]
frist84=frist4[8]
frist94=frist4[9]
frist104=frist4[10]
frist114=frist4[11]

cursor15 = db.cursor()
cursor15.execute("SELECT * FROM device_5 ORDER BY time DESC LIMIT 1,1")
frist5 = cursor15.fetchone()
frist15=frist5[1]
frist25=frist5[2]
frist35=frist5[3]
frist45=frist5[4]
frist55=frist5[5]
frist65=frist5[6]
frist75=frist5[7]
frist85=frist5[8]
frist95=frist5[9]
frist105=frist5[10]
frist115=frist5[11]


 ############################################歷史資料第2筆###############################################


cursor21 = db.cursor()
cursor21.execute("SELECT * FROM device_1 ORDER BY time DESC LIMIT 2,1")
second1 = cursor21.fetchone()
second11=second1[1]
second21=second1[2]
second31=second1[3]
second41=second1[4]
second51=second1[5]
second61=second1[6]
second71=second1[7]
second81=second1[8]
second91=second1[9]
second101=second1[10]
second111=second1[11]


cursor22 = db.cursor()
cursor22.execute("SELECT * FROM device_2 ORDER BY time DESC LIMIT 2,1")
second2 = cursor22.fetchone()
second12=second2[1]
second22=second2[2]
second32=second2[3]
second42=second2[4]
second52=second2[5]
second62=second2[6]
second72=second2[7]
second82=second2[8]
second92=second2[9]
second102=second2[10]
second112=second2[11]

cursor23 = db.cursor()
cursor23.execute("SELECT * FROM device_3 ORDER BY time DESC LIMIT 2,1")
second3 = cursor23.fetchone()
second13=second3[1]
second23=second3[2]
second33=second3[3]
second43=second3[4]
second53=second3[5]
second63=second3[6]
second73=second3[7]
second83=second3[8]
second93=second3[9]
second103=second3[10]
second113=second3[11]

cursor24 = db.cursor()
cursor24.execute("SELECT * FROM device_4 ORDER BY time DESC LIMIT 2,1")
second4 = cursor24.fetchone()
second14=second4[1]
second24=second4[2]
second34=second4[3]
second44=second4[4]
second54=second4[5]
second64=second4[6]
second74=second4[7]
second84=second4[8]
second94=second4[9]
second104=second4[10]
second114=second4[11]

cursor25 = db.cursor()
cursor25.execute("SELECT * FROM device_5 ORDER BY time DESC LIMIT 2,1")
second5 = cursor25.fetchone()
second15=second5[1]
second25=second5[2]
second35=second5[3]
second45=second5[4]
second55=second5[5]
second65=second5[6]
second75=second5[7]
second85=second5[8]
second95=second5[9]
second105=second5[10]
second115=second5[11]

############################################歷史資料第3筆###############################################


cursor31 = db.cursor()
cursor31.execute("SELECT * FROM device_1 ORDER BY time DESC LIMIT 3,1")
third1 = cursor31.fetchone()
third11=third1[1]
third21=third1[2]
third31=third1[3]
third41=third1[4]
third51=third1[5]
third61=third1[6]
third71=third1[7]
third81=third1[8]
third91=third1[9]
third101=third1[10]
third111=third1[11]


cursor32 = db.cursor()
cursor32.execute("SELECT * FROM device_2 ORDER BY time DESC LIMIT 3,1")
third2 = cursor32.fetchone()
third12=third2[1]
third22=third2[2]
third32=third2[3]
third42=third2[4]
third52=third2[5]
third62=third2[6]
third72=third2[7]
third82=third2[8]
third92=third2[9]
third102=third2[10]
third112=third2[11]

cursor33 = db.cursor()
cursor33.execute("SELECT * FROM device_3 ORDER BY time DESC LIMIT 3,1")
third3 = cursor33.fetchone()
third13=third3[1]
third23=third3[2]
third33=third3[3]
third43=third3[4]
third53=third3[5]
third63=third3[6]
third73=third3[7]
third83=third3[8]
third93=third3[9]
third103=third3[10]
third113=third3[11]

cursor34 = db.cursor()
cursor34.execute("SELECT * FROM device_4 ORDER BY time DESC LIMIT 3,1")
third4 = cursor34.fetchone()
third14=third4[1]
third24=third4[2]
third34=third4[3]
third44=third4[4]
third54=third4[5]
third64=third4[6]
third74=third4[7]
third84=third4[8]
third94=third4[9]
third104=third4[10]
third114=third4[11]

cursor35 = db.cursor()
cursor35.execute("SELECT * FROM device_5 ORDER BY time DESC LIMIT 3,1")
third5 = cursor35.fetchone()
third15=third5[1]
third25=third5[2]
third35=third5[3]
third45=third5[4]
third55=third5[5]
third65=third5[6]
third75=third5[7]
third85=third5[8]
third95=third5[9]
third105=third5[10]
third115=third5[11]

 
db.close()

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    loc_dt = datetime.datetime.today() 
    time_del = datetime.timedelta(hours=8) 
    new_dt = loc_dt 
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
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result11)+'\n'+'溫度: '+str(result21)+'˚C'+'\n'+'濕度: '+str(result31)+'RH'+'\n'+'PM1: '+str(result41)+'μg/m3'+str(point11)+'\n'+'MQ3: '+str(result51)+'μg/L'+str(point12)+'\n'+'MQ7: '+str(result61)+'μg/L'+str(point13)+'\n'+'MQ135: '+str(result71)+'μg/L'+str(point14)+'\n'+'PM25: '+str(result81)+'μg/m3'+str(point15)+'\n'+'PM10: '+str(result91)+'μg/m3'+str(point16))) 
    elif re.match('環境資料2',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result12)+'\n'+'溫度: '+str(result22)+'˚C'+'\n'+'濕度: '+str(result32)+'RH'+'\n'+'PM1: '+str(result42)+'μg/m3'+str(point21)+'\n'+'MQ3: '+str(result52)+'μg/L'+str(point22)+'\n'+'MQ7: '+str(result62)+'μg/L'+str(point23)+'\n'+'MQ135: '+str(result72)+'μg/L'+str(point24)+'\n'+'PM25: '+str(result82)+'μg/L'+str(point25)+'\n'+'PM10: '+str(result92)+'μg/m3'+str(point26)))
    elif re.match('環境資料3',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result13)+'\n'+'溫度: '+str(result23)+'˚C'+'\n'+'濕度: '+str(result33)+'RH'+'\n'+'PM1: '+str(result43)+'μg/m3'+str(point31)+'\n'+'MQ3: '+str(result53)+'μg/L'+str(point32)+'\n'+'MQ7: '+str(result63)+'μg/L'+str(point33)+'\n'+'MQ135: '+str(result73)+'μg/L'+str(point34)+'\n'+'PM25: '+str(result83)+'μg/L'+str(point35)+'\n'+'PM10: '+str(result93)+'μg/m3'+str(point36)))
    elif re.match('環境資料4',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result14)+'\n'+'溫度: '+str(result24)+'˚C'+'\n'+'濕度: '+str(result34)+'RH'+'\n'+'PM1: '+str(result44)+'μg/m3'+str(point41)+'\n'+'MQ3: '+str(result54)+'μg/L'+str(point42)+'\n'+'MQ7: '+str(result64)+'μg/L'+str(point43)+'\n'+'MQ135: '+str(result74)+'μg/L'+str(point44)+'\n'+'PM25: '+str(result84)+'μg/L'+str(point45)+'\n'+'PM10: '+str(result94)+'μg/m3'+str(point46)))
    elif re.match('環境資料5',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(result15)+'\n'+'溫度: '+str(result25)+'˚C'+'\n'+'濕度: '+str(result35)+'RH'+'\n'+'PM1: '+str(result45)+'μg/m3'+str(point51)+'\n'+'MQ3: '+str(result55)+'μg/L'+str(point52)+'\n'+'MQ7: '+str(result65)+'μg/L'+str(point53)+'\n'+'MQ135: '+str(result75)+'μg/L'+str(point54)+'\n'+'PM25: '+str(result85)+'μg/L'+str(point55)+'\n'+'PM10: '+str(result95)+'μg/m3'+str(point56)))
     
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
##########################################################歷史資料########################################################################

    elif re.match('我想看歷史資料',message):
         flex_message = TextSendMessage(text='請選擇要觀看裝置幾的歷史資料',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(label="裝置一", text="裝置一歷史資料")),
                                    QuickReplyButton(action=MessageAction(label="裝置二", text="裝置二歷史資料")),
                                    QuickReplyButton(action=MessageAction(label="裝置三", text="裝置三歷史資料")),
                                    QuickReplyButton(action=MessageAction(label="裝置四", text="裝置四歷史資料")),
                                    QuickReplyButton(action=MessageAction(label="裝置五", text="裝置五歷史資料")),
                                ]))
         line_bot_api.reply_message(event.reply_token, flex_message)

    elif re.match('裝置一歷史資料',message):
         buttons_template_message = TemplateSendMessage(
         alt_text='這個看不到',
         template=ButtonsTemplate(
             thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1875/1875043.png',
             title='裝置一的歷史資料',
             text='請選擇你想看哪筆資料',
             actions=[
                 MessageAction(
                     label='前第一筆資料',
                     text='裝置一前第一筆資料'
                 ),
                 MessageAction(
                     label='前第二筆資料',
                     text='裝置一前第二筆資料'
                 ),
                 MessageAction(
                     label='前第三筆資料',
                     text='裝置一前第三筆資料'
                 ),
             ]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('裝置二歷史資料',message):
         buttons_template_message = TemplateSendMessage(
         alt_text='這個看不到',
         template=ButtonsTemplate(
             thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1874/1874965.png',
             title='裝置二的歷史資料',
             text='請選擇你想看哪筆資料',
             actions=[
                 MessageAction(
                     label='前第一筆資料',
                     text='裝置二前第一筆資料'
                 ),
                 MessageAction(
                     label='前第二筆資料',
                     text='裝置二前第二筆資料'
                 ),
                 MessageAction(
                     label='前第三筆資料',
                     text='裝置二前第三筆資料'
                 ),
             ]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('裝置三歷史資料',message):
         buttons_template_message = TemplateSendMessage(
         alt_text='這個看不到',
         template=ButtonsTemplate(
             thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1875/1875078.png',
             title='裝置三的歷史資料',
             text='請選擇你想看哪筆資料',
             actions=[
                 MessageAction(
                     label='前第一筆資料',
                     text='裝置三前第一筆資料'
                 ),
                 MessageAction(
                     label='前第二筆資料',
                     text='裝置三前第二筆資料'
                 ),
                 MessageAction(
                     label='前第三筆資料',
                     text='裝置三前第三筆資料'
                 ),
             ]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('裝置四歷史資料',message):
         buttons_template_message = TemplateSendMessage(
         alt_text='這個看不到',
         template=ButtonsTemplate(
             thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1874/1874996.png',
             title='裝置四的歷史資料',
             text='請選擇你想看哪筆資料',
             actions=[
                 MessageAction(
                     label='前第一筆資料',
                     text='裝置四前第一筆資料'
                 ),
                 MessageAction(
                     label='前第二筆資料',
                     text='裝置四前第二筆資料'
                 ),
                 MessageAction(
                     label='前第三筆資料',
                     text='裝置四前第三筆資料'
                 ),
             ]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)
    elif re.match('裝置五歷史資料',message):
         buttons_template_message = TemplateSendMessage(
         alt_text='這個看不到',
         template=ButtonsTemplate(
             thumbnail_image_url='https://cdn-icons-png.flaticon.com/512/1875/1875006.png',
             title='裝置五的歷史資料',
             text='請選擇你想看哪筆資料',
             actions=[
                 MessageAction(
                     label='前第一筆資料',
                     text='裝置五前第一筆資料'
                 ),
                 MessageAction(
                     label='前第二筆資料',
                     text='裝置五前第二筆資料'
                 ),
                 MessageAction(
                     label='前第三筆資料',
                     text='裝置五前第三筆資料'
                 ),
             ]
         )
     )
         line_bot_api.reply_message(event.reply_token, buttons_template_message)

    elif re.match('裝置一前第一筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(frist11)+'\n'+'溫度: '+str(frist21)+'˚C'+'\n'+'濕度: '+str(frist31)+'RH'+'\n'+'PM1: '+str(frist41)+'μg/m3'+'\n'+'MQ3: '+str(frist51)+'μg/L'+'\n'+'MQ7: '+str(frist61)+'μg/L'+'\n'+'MQ135: '+str(frist71)+'μg/L'+'\n'+'PM25: '+str(frist81)+'μg/m3'+'\n'+'PM10: '+str(frist91)+'μg/m3')) 
    elif re.match('裝置一前第二筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(second11)+'\n'+'溫度: '+str(second21)+'˚C'+'\n'+'濕度: '+str(second31)+'RH'+'\n'+'PM1: '+str(second41)+'μg/m3'+'\n'+'MQ3: '+str(second51)+'μg/L'+'\n'+'MQ7: '+str(second61)+'μg/L'+'\n'+'MQ135: '+str(second71)+'μg/L'+'\n'+'PM25: '+str(second81)+'μg/m3'+'\n'+'PM10: '+str(second91)+'μg/m3'))
    elif re.match('裝置一前第三筆資料',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(third11)+'\n'+'溫度: '+str(third21)+'˚C'+'\n'+'濕度: '+str(third31)+'RH'+'\n'+'PM1: '+str(third41)+'μg/m3'+'\n'+'MQ3: '+str(third51)+'μg/L'+'\n'+'MQ7: '+str(third61)+'μg/L'+'\n'+'MQ135: '+str(third71)+'μg/L'+'\n'+'PM25: '+str(third81)+'μg/m3'+'\n'+'PM10: '+str(third91)+'μg/m3'))
    elif re.match('裝置二前第一筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(frist12)+'\n'+'溫度: '+str(frist22)+'˚C'+'\n'+'濕度: '+str(frist32)+'RH'+'\n'+'PM1: '+str(frist42)+'μg/m3'+'\n'+'MQ3: '+str(frist52)+'μg/L'+'\n'+'MQ7: '+str(frist62)+'μg/L'+'\n'+'MQ135: '+str(frist72)+'μg/L'+'\n'+'PM25: '+str(frist82)+'μg/m3'+'\n'+'PM10: '+str(frist92)+'μg/m3')) 
    elif re.match('裝置二前第二筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(second12)+'\n'+'溫度: '+str(second22)+'˚C'+'\n'+'濕度: '+str(second32)+'RH'+'\n'+'PM1: '+str(second42)+'μg/m3'+'\n'+'MQ3: '+str(second52)+'μg/L'+'\n'+'MQ7: '+str(second62)+'μg/L'+'\n'+'MQ135: '+str(second72)+'μg/L'+'\n'+'PM25: '+str(second82)+'μg/m3'+'\n'+'PM10: '+str(second92)+'μg/m3'))
    elif re.match('裝置二前第三筆資料',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(third12)+'\n'+'溫度: '+str(third22)+'˚C'+'\n'+'濕度: '+str(third32)+'RH'+'\n'+'PM1: '+str(third42)+'μg/m3'+'\n'+'MQ3: '+str(third52)+'μg/L'+'\n'+'MQ7: '+str(third62)+'μg/L'+'\n'+'MQ135: '+str(third72)+'μg/L'+'\n'+'PM25: '+str(third82)+'μg/m3'+'\n'+'PM10: '+str(third92)+'μg/m3'))
    elif re.match('裝置三前第一筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(frist13)+'\n'+'溫度: '+str(frist23)+'˚C'+'\n'+'濕度: '+str(frist33)+'RH'+'\n'+'PM1: '+str(frist43)+'μg/m3'+'\n'+'MQ3: '+str(frist53)+'μg/L'+'\n'+'MQ7: '+str(frist63)+'μg/L'+'\n'+'MQ135: '+str(frist73)+'μg/L'+'\n'+'PM25: '+str(frist83)+'μg/m3'+'\n'+'PM10: '+str(frist93)+'μg/m3')) 
    elif re.match('裝置三前第二筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(second13)+'\n'+'溫度: '+str(second23)+'˚C'+'\n'+'濕度: '+str(second33)+'RH'+'\n'+'PM1: '+str(second43)+'μg/m3'+'\n'+'MQ3: '+str(second53)+'μg/L'+'\n'+'MQ7: '+str(second63)+'μg/L'+'\n'+'MQ135: '+str(second73)+'μg/L'+'\n'+'PM25: '+str(second83)+'μg/m3'+'\n'+'PM10: '+str(second93)+'μg/m3'))
    elif re.match('裝置三前第三筆資料',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(third13)+'\n'+'溫度: '+str(third23)+'˚C'+'\n'+'濕度: '+str(third33)+'RH'+'\n'+'PM1: '+str(third43)+'μg/m3'+'\n'+'PM25: '+str(third53)+'μg/m3'+'\n'+'PM10: '+str(third63)+'μg/m3'+'\n'+'MQ3: '+str(third73)+'μg/L'+'\n'+'MQ10: '+str(third83)+'μg/L'+'\n'+'MQ135: '+str(third93)+'μg/L'))
    elif re.match('裝置四前第一筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(frist14)+'\n'+'溫度: '+str(frist24)+'˚C'+'\n'+'濕度: '+str(frist34)+'RH'+'\n'+'PM1: '+str(frist44)+'μg/m3'+'\n'+'PM25: '+str(frist54)+'μg/m3'+'\n'+'PM10: '+str(frist64)+'μg/m3'+'\n'+'MQ3: '+str(frist74)+'μg/L'+'\n'+'MQ10: '+str(frist84)+'μg/L'+'\n'+'MQ135: '+str(frist94)+'μg/L')) 
    elif re.match('裝置四前第二筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(second14)+'\n'+'溫度: '+str(second24)+'˚C'+'\n'+'濕度: '+str(second34)+'RH'+'\n'+'PM1: '+str(second44)+'μg/m3'+'\n'+'PM25: '+str(second54)+'μg/m3'+'\n'+'PM10: '+str(second64)+'μg/m3'+'\n'+'MQ3: '+str(second74)+'μg/L'+'\n'+'MQ10: '+str(second84)+'μg/L'+'\n'+'MQ135: '+str(second94)+'μg/L'))
    elif re.match('裝置四前第三筆資料',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(third14)+'\n'+'溫度: '+str(third24)+'˚C'+'\n'+'濕度: '+str(third34)+'RH'+'\n'+'PM1: '+str(third44)+'μg/m3'+'\n'+'PM25: '+str(third54)+'μg/m3'+'\n'+'PM10: '+str(third64)+'μg/m3'+'\n'+'MQ3: '+str(third74)+'μg/L'+'\n'+'MQ10: '+str(third84)+'μg/L'+'\n'+'MQ135: '+str(third94)+'μg/L'))
    elif re.match('裝置五前第一筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(frist15)+'\n'+'溫度: '+str(frist25)+'˚C'+'\n'+'濕度: '+str(frist35)+'RH'+'\n'+'PM1: '+str(frist45)+'μg/m3'+'\n'+'PM25: '+str(frist55)+'μg/m3'+'\n'+'PM10: '+str(frist65)+'μg/m3'+'\n'+'MQ3: '+str(frist75)+'μg/L'+'\n'+'MQ10: '+str(frist85)+'μg/L'+'\n'+'MQ135: '+str(frist95)+'μg/L')) 
    elif re.match('裝置五前第二筆資料',message):
        line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(second15)+'\n'+'溫度: '+str(second25)+'˚C'+'\n'+'濕度: '+str(second35)+'RH'+'\n'+'PM1: '+str(second45)+'μg/m3'+'\n'+'PM25: '+str(second55)+'μg/m3'+'\n'+'PM10: '+str(second65)+'μg/m3'+'\n'+'MQ3: '+str(second75)+'μg/L'+'\n'+'MQ10: '+str(second85)+'μg/L'+'\n'+'MQ135: '+str(second95)+'μg/L'))
    elif re.match('裝置五前第三筆資料',message):
          line_bot_api.push_message(yourID, 
                         TextSendMessage(text='更新時間:'+str(datetime_format)+'\n'+'測量時間:'+str(third15)+'\n'+'溫度: '+str(third25)+'˚C'+'\n'+'濕度: '+str(third35)+'RH'+'\n'+'PM1: '+str(third45)+'μg/m3'+'\n'+'PM25: '+str(third55)+'μg/m3'+'\n'+'PM10: '+str(third65)+'μg/m3'+'\n'+'MQ3: '+str(third75)+'μg/L'+'\n'+'MQ10: '+str(third85)+'μg/L'+'\n'+'MQ135: '+str(third95)+'μg/L'))
        
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
