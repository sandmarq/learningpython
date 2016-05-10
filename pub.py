from random import randint
import time
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 1883, 60)

while True:
    value1 = randint(0,99)
    print("1 :", value1)
    client.publish('/leds/esp8266_1', value1)

    value2 = randint(0,99)
    print("2 :", value2)
    client.publish('/leds/esp8266_2', value2)

    time.sleep(1)
