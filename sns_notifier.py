
import boto3
from botocore.exceptions import ClientError

class SNSNotifier:
    def __init__(self):
        self.sns = boto3.client("sns")

    def create_topic(self, name):
        try:
            response = self.sns.create_topic(Name=name)
            print(f"SNS topic {name} created.")
            return response["TopicArn"]
        except ClientError as e:
            print(f"Error creating SNS topic: {e}")

    def subscribe_email(self, topic_arn, email):
        try:
            self.sns.subscribe(TopicArn=topic_arn, Protocol="email", Endpoint=email)
            print(f"Subscribed {email} to SNS topic {topic_arn}.")
        except ClientError as e:
            print(f"Error subscribing email to SNS topic: {e}")

    def delete_topic(self, topic_arn):
        try:
            self.sns.delete_topic(TopicArn=topic_arn)
            print(f"SNS topic {topic_arn} deleted.")
        except ClientError as e:
            print(f"Error deleting SNS topic: {e}")
    