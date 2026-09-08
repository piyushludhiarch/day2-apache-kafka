from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "bank-transactions",
    bootstrap_servers="localhost:9092",
    group_id="bank-monitoring",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("Consumer started...")

for message in consumer:

    transaction = message.value

    print("Received:", transaction)
