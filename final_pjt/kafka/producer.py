from confluent_kafka import Producer
import requests
import json
import time
from datetime import datetime

def try_api(url):
    response = requests.get(url)
    now_time = datetime.now().strftime('%Y%m%d_%H%M')

    if(response.status_code) == 200:
        res = response.json()
        data = res['rentBikeStatus']['row']
        for obj in data:
           obj['datetime']=now_time
        return data
    else:
        print("Failed")
        return None


def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed:', err)
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


bootstrap_servers = 'localhost:9092'
topic = 'bike-topic'
#group_id='bike'

producer_config ={
   'bootstrap.servers':bootstrap_servers,
   # 'group.id':group_id
}

producer = Producer(producer_config)



user_key = "664c747774656f6e3130384667614e49"
api_url = "http://openapi.seoul.go.kr:8088/"+user_key+"/json/bikeList/1/999/"

while True:
     data=try_api(api_url)
     #print(data)
     byte_data =json.dumps(data).encode('utf-8')
     producer.produce(topic,key=None,value=byte_data,callback = delivery_report)
     producer.flush()
     time.sleep(300)
