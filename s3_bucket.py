
import boto3
from botocore.exceptions import ClientError

class S3Bucket:
    def __init__(self, bucket_name):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def create_bucket(self):
        try:
            self.s3.create_bucket(Bucket=self.bucket_name)
            print(f"S3 bucket {self.bucket_name} created.")
        except ClientError as e:
            print(f"Error creating S3 bucket: {e}")

    def delete_bucket(self):
        try:
            bucket = boto3.resource('s3').Bucket(self.bucket_name)
            bucket.objects.all().delete()
            bucket.delete()
            print(f"S3 bucket {self.bucket_name} deleted.")
        except ClientError as e:
            print(f"Error deleting S3 bucket: {e}")
    