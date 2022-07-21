import boto3
import requests
import os
from dotenv import load_dotenv
load_dotenv()

client = boto3.client('dynamodb', region_name='eu-west-1')

table = os.getenv('Dynamo_Main_Table')

# add items to Dynamo DB table, this can be used to update existing items too

response = client.put_item(
    TableName= table,
    Item={
        'PK': {
            'S': 'submission-event-2022'
        },
        'SK': {
            'S': 'BUYING'
        },
        'type': {
            'S': 'api'
        }
    }
)
