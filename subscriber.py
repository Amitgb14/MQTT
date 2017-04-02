
import paho.mqtt.client as mqtt
import time

host="172.17.0.2"
port=1883
user="amitg"
password="amitg14"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection
    # and
    # reconnect then subscriptions will be renewed.
    client.subscribe("owntracks/temp", qos=1)

# The callback for when a PUBLISH message is received from
# the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("S2", clean_session=False)
client.username_pw_set(username=user, password=password)

client.on_connect = on_connect
client.on_message = on_message


client.connect(host, port, 60)


client.loop_forever()

