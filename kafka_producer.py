from kafka import KafkaProducer
def sender(input_data):
    producer = KafkaProducer(bootstrap_servers='localhost:9092') 
    producer.send('input', input_data.encode('utf-8'))
    producer.flush()

