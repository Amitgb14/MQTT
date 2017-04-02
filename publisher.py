
import paho.mqtt.client as mqtt
import time

host="172.17.0.2"
port=1883
user="amitg"
password="amitg14"
# The callback for when the client receives a CONNACK response from the server.
def on_publish(client, userdata, result):
    print("Published done")

# The callback for when a PUBLISH message is received from
# the server.
def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

client = mqtt.Client("P1", clean_session=True)
client.username_pw_set(username=user, password=password)

client.on_publish = on_publish
client.on_message = on_message

client.connect(host, port, 60)


client.loop_start()
loop_flag = 1
counter = 0
while loop_flag==1:
    print("Sending Temp:", counter)
    client.publish("owntracks/temp", counter, qos=1)
    time.sleep(2)
    counter += 1

