from confluent_kafka import Producer

def acked(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

p = Producer({'bootstrap.servers': 'localhost:9092'})

for i in range(10):
    p.produce('test_topic', key=str(i), value=f'test message {i}', callback=acked)

p.flush()