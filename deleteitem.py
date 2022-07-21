import boto3
import requests
import os
from dotenv import load_dotenv
load_dotenv()

client = boto3.client('dynamodb', region_name='eu-west-1')

table = os.getenv('Dynamo_Main_Table')

# this will delete items from the Dynamo DB table
 
response = client.delete_item(
    TableName= table,
    Key={
        'PK': {
            'S': 'submission-event-{Customer_ID}' # insert customer id here
        },
        'SK': {
            'S': '{App_ID}' # app id, i.e buying/reorder
        }
    }
)