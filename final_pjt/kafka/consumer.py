from confluent_kafka import Consumer, KafkaError
import json
import csv

# Kafka 설정
bootstrap_servers = 'localhost:9092'
topic = 'bike-topic'
group_id ='bike'

# Kafka Consumer 설정
consumer_config = {
    'bootstrap.servers': bootstrap_servers,
    'group.id':group_id,
    'auto.offset.reset': 'earliest'  # Consumer가 시작할 때 가장 이른 오프셋부터 메시지를 읽도록 설정
}

# Kafka Consumer 인스턴스 생성
consumer = Consumer(consumer_config)

# 토픽 구독
consumer.subscribe([topic])

# 메시지 소비 루프
try:
    while True:
        msg = consumer.poll(timeout=1.0)  # 1초마다 메시지 폴링
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # 토픽의 파티션의 마지막 오프셋에 도달하여 더 이상 읽을 메시지가 없음
                continue
            else:
                # 다른 에러가 발생한 경우
                print(msg.error())
                break
        else:
            # 메시지 소비
            #print('Received message: {}'.format(msg.value().decode('utf-8')))
            res=format(msg.value().decode('utf-8'))
            data =json.loads(res) 
            now_time = data[0]['datetime']
            csv_file = str(now_time)+'.csv'

            with open(csv_file,'w',newline='') as f:
                  writer=csv.writer(f)
                  headers=list(data[0].keys())

                  for row in data:
                     row_value=list(row.values())
                     writer.writerow(row_value)

except KeyboardInterrupt:
    pass
finally:
    # Consumer 종료
    consumer.close()
