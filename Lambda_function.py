import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

table = dynamodb.Table("ContactMessages")

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"


def lambda_handler(event, context):

    try:

        body = json.loads(event.get("body", "{}"))

        name = body.get("name")
        email = body.get("email")
        message = body.get("message")

        if not name or not email or not message:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps({
                    "message": "Name, email and message are required"
                })
            }

        message_id = str(uuid.uuid4())

        table.put_item(
            Item={
                "id": message_id,
                "name": name,
                "email": email,
                "message": message,
                "createdAt": datetime.utcnow().isoformat()
            }
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="New Contact Form Submission",
            Message=f"""
New contact form submission

Name: {name}
Email: {email}

Message:
{message}
"""
        )

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Message submitted successfully"
            })
        }

    except Exception as e:

        print(str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Internal server error"
            })
        }
