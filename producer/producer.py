from kafka import KafkaProducer
import json
import random
import time
import uuid

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Producer started... sending to topic: bank-transactions")

while True:

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "account_id": f"ACC{random.randint(100, 999)}",
        "amount": random.randint(100, 100000),
        "currency": "INR",
        "merchant": random.choice([
            "Amazon",
            "Flipkart",
            "Myntra",
            "BigBasket"
        ]),
        "location": random.choice([
            "Hyderabad",
            "Bangalore",
            "Mumbai",
            "Delhi"
        ]),
        "status": "SUCCESS"
    }

    producer.send(
        "bank-transactions",
        value=transaction
    )

    print("Produced:", transaction)

    time.sleep(2)
