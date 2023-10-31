from pykafka import KafkaClient

class EventBroker:
    def __init__(self, addr: str, topic: str):
        client = KafkaClient(hosts=addr)
        topic = client.topics[topic]

        self.producer = topic.get_sync_producer()
        self.consumer = topic.get_simple_consumer()

    def produce(self, message: str):
        self.producer.produce(bytes(message, encoding='utf8'))

    def subscribe(self):
        try:
            # Extra simple consumer (also reading last messages)
            for message in self.consumer:
                if message is not None:
                    print(message.value.decode('utf-8'))
        except Exception as ex:
            print("Kafka Exception : {}", ex)
