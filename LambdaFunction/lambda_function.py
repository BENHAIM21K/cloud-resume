import json
import boto3

def lambda_handler(event, context):
    try:
        # Check if the HTTP method is POST
        if event.get('httpMethod') == 'POST':
            # Load the body of the event
            body = json.loads(event.get('body', '{}'))
            
            # Check if the event body contains the success key and its value is True
            if body.get('success') == True:
                sns_client = boto3.client('sns')
                
                # Define the SNS topic ARN
                topic_arn = 'arn:aws:sns:il-central-1:381492296048:CVDownloadEmail'
                
                # Define the message you want to send
                message = 'Someone has successfully downloaded your CV!'
                
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
            else:
                return {
                    'statusCode': 400,
                    'body': json.dumps('Download not successful, no email sent.')
                }
        else:
            return {
                'statusCode': 405,
                'body': json.dumps('Only POST method is allowed.')
            }
    except KeyError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"KeyError: {str(e)}")
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f"An unexpected error occurred: {str(e)}")
        }
