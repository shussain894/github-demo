import boto3
import json

# verify email address on AWS SES
client = boto3.client('ses', region_name='eu-west-1')
response = client.verify_email_identity(
    EmailAddress='shah@gmail.com'
)

# function to send email

def send_emails(sub):

    ToAddresses=sub['ToAddresses']

    ses = boto3.client('ses')

    body = """
        Hello X,
    
        Kind Regards,
        Shah
    """

    ses.send_email(
        Source = 'shah@gmail.com',
        Destination = {
            'ToAddresses': ToAddresses
        },
        Message = {
            'Subject': {
                'Data': 'SES Demo',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text':{
                    'Data': body,
                    'Charset': 'UTF-8'
                }
            }
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent email from Lambda using Amazon SES')
    }