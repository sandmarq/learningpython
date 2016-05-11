from random import randint
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 1883, 60)

while True:
    value1 = str(randint(-40, 40)) + "." + str(randint(0, 99)) + "," + str(randint(0, 100)) + "." + str(randint(0, 100))
    print("1 :", value1)
    client.publish('/home/room/esp8266_1', value1)

    value2 = str(randint(-40, 40)) + "." + str(randint(0, 99)) + "," + str(randint(0, 100)) + "." + str(randint(0, 100))
    print("2 :", value2)
    client.publish('/home/room/esp8266_2', value2)

    value3 = str(randint(-40, 40)) + "." + str(randint(0, 99)) + "," + str(randint(0, 100)) + "." + str(randint(0, 100))
    print("3 :", value3)
    client.publish('/home/room/esp8266_3', value3)

    value4 = str(randint(-40, 40)) + "." + str(randint(0, 99)) + "," + str(randint(0, 100)) + "." + str(randint(0, 100))
    print("4 :", value4)
    client.publish('/home/room/esp8266_4', value4)

    value5 = str(randint(-40, 40)) + "." + str(randint(0, 99)) + "," + str(randint(0, 100)) + "." + str(randint(0, 100))
    print("5 :", value5)
    client.publish('/home/room/esp8266_5', value5)

    time.sleep(60)
