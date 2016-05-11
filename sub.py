import paho.mqtt.client as mqtt
import mysql.connector as mariadb
import datetime
import time
from decimal import Decimal


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print(
        "Connected with result code " + str(rc))  # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe([("/home/room/esp8266_1", 0), ("/home/room/esp8266_2", 2), ("/home/room/esp8266_3", 2),
                      ("/home/room/esp8266_4", 2), ("/home/room/esp8266_5",
                                                    2)])  # The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    f = open('myfile.csv', 'a')
    datenow = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print(datenow + "," + msg.topic + "," + str(
        msg.payload.decode("UTF-8")))
    f.write(datenow + "," + msg.topic + "," + str(
        msg.payload.decode("UTF-8")) + "\n")
    f.close()

    datas = msg.payload.decode("UTF-8").split(",")
    topic = msg.topic
    value1 = datas[0]
    value2 = datas[1]

    mariadb_connection = mariadb.connect(user='domocontrolsm_user', password='domocontrolsm_password',
                                         database='domocontrolsm_database')
    cursor = mariadb_connection.cursor()
    cursor.execute("INSERT INTO tempsensors(date,topic,temp,humidity) VALUES(%s,%s,%s,%s)",
                   (datenow, topic, Decimal(value1), Decimal(value2)))
    mariadb_connection.commit()
    mariadb_connection.close()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
