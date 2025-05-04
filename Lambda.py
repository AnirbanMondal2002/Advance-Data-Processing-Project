import json
import boto3
import base64

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fraud-transactions')

def lambda_handler(event, context):
    records = []
    
    for record in event['Records']:
        try:
            # Decode and parse the Kinesis data
            payload = json.loads(base64.b64decode(record['kinesis']['data']))
            records.append(payload)

            # Store in DynamoDB
            table.put_item(Item=payload)
        
        except Exception as e:
            print(f"Error processing record: {e}")
            continue

    # Save the full batch to S3
    if records:
        try:
            s3_client.put_object(
                Bucket="fraud-detection-buckets",
                Key=f"raw-transactions/{records[0]['transaction_id']}.json",
                Body=json.dumps(records),
                ContentType='application/json'
            )
        except Exception as e:
            print(f"Error writing to S3: {e}")

    return {
        "statusCode": 200,
        "body": "Data processed successfully"
    }
