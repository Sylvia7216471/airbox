import pymysql

#資料庫連線設定
#可縮寫db = pymysql.connect("localhost","root","root","30days" )
db = pymysql.connect(host='120.119.157.238', port=1801, user='LiRu', passwd='', database = "iot")
#建立操作游標
cursor = db.cursor()

# Read
cursor.execute("SELECT * FROM device_5")
result = cursor.fetchall()
for row in result:
    print(row)

#關閉連線
db.close()
