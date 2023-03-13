import paho.mqtt.client as mqtt
import json

mqtt_broker_host='54.210.208.75'
mqtt_broker_port =1883
mqtt_alive_inerval=60
topic1="return/R1"
#topic2="return/R2"


def on_connect(client,userdata,flags,rc):
    print("connected with the result code" + str(rc))
    client.subscribe("return/R1")

def on_message(client,userdata,msg):
    x=msg.payload.decode()
    x=json.loads(x)
    my_position=x['pose']['pose']['position']
    print(my_position)

client=mqtt.Client()
client.connect(mqtt_broker_host,mqtt_broker_port,mqtt_alive_inerval)
client.on_connect=on_connect
client.on_message=on_message
client.loop_forever()