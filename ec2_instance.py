
import boto3
from botocore.exceptions import ClientError

class EC2Instance:
    def __init__(self, instance_type, key_name, security_group, ami_id="ami-0c55b159cbfafe1f0"):
        self.ec2 = boto3.resource("ec2")
        self.instance_type = instance_type
        self.key_name = key_name
        self.security_group = security_group
        self.ami_id = ami_id
        self.instance = None

    def launch_instance(self):
        try:
            self.instance = self.ec2.create_instances(
                ImageId=self.ami_id,
                InstanceType=self.instance_type,
                KeyName=self.key_name,
                SecurityGroups=[self.security_group],
                MinCount=1,
                MaxCount=1
            )[0]
            print(f"EC2 instance {self.instance.id} launched.")
            return self.instance
        except ClientError as e:
            print(f"Error launching EC2 instance: {e}")

    def terminate_instance(self):
        try:
            if self.instance:
                self.instance.terminate()
                self.instance.wait_until_terminated()
                print(f"EC2 instance {self.instance.id} terminated.")
            else:
                print("No EC2 instance to terminate.")
        except ClientError as e:
            print(f"Error terminating EC2 instance: {e}")
    