import random
import time
import test_request as pollo

from mqtt import client as mqtt_client


#broker = 'broker.emqx.io'
broker = 'localhost'
#broker = "148.213.116.247"
port = 1883
topic = "food/apple"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'hilario'
password = 'pollo123'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    while True:
        time.sleep(1)
        #msg = pollo.get_temp()
        #volts = int(msg)*(5/1023)
        #millivolts = volts*1000
        #degreesC = round(millivolts/100, 3)
        #result = client.publish(topic, degreesC)
        result = client.publish(topic, "alvmevake")


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

