import boto3
import os

ses_client = boto3.client('ses')

def lambda_handler(event, context):
    # Get your email address from environment variables
    recipient_email = os.environ['RECIPIENT_EMAIL']
    
    # Send email using SES
    response = ses_client.send_email(
        Source=recipient_email,
        Destination={
            'ToAddresses': [recipient_email],
        },
        Message={
            'Subject': {
                'Data': 'CV Download Notification',
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': 'Your CV was downloaded by someone on your website.',
                    'Charset': 'UTF-8'
                }
            }
        }
    )

    return {
        'statusCode': 200,
        'body': 'Email sent successfully!'
    }
