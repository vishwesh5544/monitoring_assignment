
import boto3
from botocore.exceptions import ClientError

class LoadBalancer:
    def __init__(self, name, security_group, subnets):
        self.elb = boto3.client("elbv2")
        self.name = name
        self.security_group = security_group
        self.subnets = subnets
        self.arn = None

    def create_load_balancer(self):
        try:
            response = self.elb.create_load_balancer(
                Name=self.name,
                Subnets=self.subnets,
                SecurityGroups=[self.security_group],
                Scheme="internet-facing",
                Type="application"
            )
            self.arn = response['LoadBalancers'][0]['LoadBalancerArn']
            print(f"Load balancer {self.name} created.")
            return self.arn
        except ClientError as e:
            print(f"Error creating Load Balancer: {e}")

    def delete_load_balancer(self):
        try:
            if self.arn:
                self.elb.delete_load_balancer(LoadBalancerArn=self.arn)
                print(f"Load balancer {self.name} deleted.")
            else:
                print("No load balancer to delete.")
        except ClientError as e:
            print(f"Error deleting Load Balancer: {e}")
    