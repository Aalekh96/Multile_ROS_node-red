import json 
import time 
import paho.mqtt.client as mqtt 


########################################################
payload=open("pose.json")
read_content=payload.read()
x=json.loads(read_content)
y=(x['pose']['position'])
#print(y)
########################################################
for i in y.keys():
    #print(i)
    y[i]=input("enter x , y and z coordinate")

#########################################################
paylaod_1={
    "header": {
      "seq": 0,
      "stamp": {
        "secs": 0,
        "nsecs": 0
      },
      "frame_id": "map"
    },
    "pose":{
      "position":
        y
      ,

      "orientation": {
        "x": 0,
        "y": 0,
        "z": 0,
        "w": 1
      }
    }
}
###########################################
#print(paylaod_1)  
jsonString=json.dumps(paylaod_1,indent=4)
jsonFile=open("update_json.json","w")
jsonFile.write(jsonString)
#print((jsonString))
###########################################