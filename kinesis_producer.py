import boto3
import json
import random
import time

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def generate_transaction():
    transaction = {
        "transaction_id": str(random.randint(100000, 999999)),
        "user_id": random.randint(1, 1000),
        "amount": round(random.uniform(5, 5000), 2),
        "location": random.choice(["New York", "Los Angeles", "Chicago"]),
        "transaction_type": random.choice(["Online", "Offline"]),
        "fraud_probability": round(random.uniform(0, 1), 2)
    }
    return transaction

while True:
    data = generate_transaction()
    kinesis_client.put_record(
        StreamName="fraud-detection-stream",
        Data=json.dumps(data),
        PartitionKey=str(data["user_id"])
    )
    print(f"Sent: {data}")
    time.sleep(2)
