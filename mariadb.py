#!/usr/bin/python
import mysql.connector as mariadb
import datetime
import time
from random import randint
from decimal import Decimal

date1 = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
topic = '/home/room/esp8266_1'
value1 = str(randint(-40, 40)) + "." + str(randint(0, 99))
value2 = str(randint(0, 100)) + "." + str(randint(0, 100))

print(date1)
print(topic)
print(value1)
print(value2)

mariadb_connection = mariadb.connect(user='domocontrolsm_user', password='domocontrolsm_password', database='domocontrolsm_database')
cursor = mariadb_connection.cursor()
cursor.execute("INSERT INTO tempsensors(date,topic,temp,humidity) VALUES(%s,%s,%s,%s)", (date1, topic, Decimal(value1), Decimal(value2)))
mariadb_connection.commit()


cursor2 = mariadb_connection.cursor()
cursor2.execute("SELECT * FROM tempsensors")
rows = cursor2.fetchall()

for row in rows:
    id = row[0]
    date2 = row[1]
    topic2 = row[2]
    temp = row[3]
    humi = row[4]
    print("id = %s, date = %s, topic = %s, temp = %s, humi = %s" % (id, date2, topic2, temp, humi))

mariadb_connection.commit()
mariadb_connection.close()
