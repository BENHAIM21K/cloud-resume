import json
import boto3

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    
    # Define the SNS topic ARN
    topic_arn = 'your arn'
    
    # Define the message you want to send
    message = 'Someone has downloaded your CV!'
    
    # Publish the message to the SNS topic
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='CV Download'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email sent successfully!')
    }
