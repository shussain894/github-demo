import json
from re import sub
import boto3
from ftp import ftplib
import requests
import os
from ftp import send_ftp
from api import send_api
from sendem import send_emails
from dotenv import load_dotenv
load_dotenv()


client = boto3.client('dynamodb', region_name='eu-west-1')

# function to get customer info from Dynamo DB

def get_submission_parameters(Customer_ID, App_ID):
        client = boto3.client('dynamodb', region_name='eu-west-1')
        table = os.getenv('Dynamo_Main_Table') # AWS Dynamo DB table name stored in an environment variable

        # get item by Customer ID, this will return how a customer prefers to be contacted

        response = client.get_item( 
            TableName = table,
            Key={                                           
                    'PK' : {'S':f'submission-event-{Customer_ID}'}, # search by {Customer_ID} 4 digit number
                    'SK' :{'S':f'{App_ID}'} # for eg buying/reorder
                        
            }
        )

        print('response',response)
        
        return response['Item']

def lambda_handler(event, context):
        
        sub = get_submission_parameters('submission-event-1234','BUYING')        # Customer_ID, App_ID
        type = sub['type']

        if(type == "email"):
            send_emails(sub)

        elif(type == "ftp"):
            send_ftp(sub)
        
        else:
            (type == "api")
            send_api(sub)

lambda_handler('','')
