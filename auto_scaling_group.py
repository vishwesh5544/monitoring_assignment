
import boto3
from botocore.exceptions import ClientError

class AutoScalingGroup:
    def __init__(self, group_name, launch_config, subnets):
        self.autoscaling = boto3.client("autoscaling")
        self.group_name = group_name
        self.launch_config = launch_config
        self.subnets = subnets

    def create_auto_scaling_group(self, min_size, max_size):
        try:
            self.autoscaling.create_auto_scaling_group(
                AutoScalingGroupName=self.group_name,
                LaunchConfigurationName=self.launch_config,
                MinSize=min_size,
                MaxSize=max_size,
                VPCZoneIdentifier=",".join(self.subnets)
            )
            print(f"Auto Scaling Group {self.group_name} created.")
        except ClientError as e:
            print(f"Error creating Auto Scaling Group: {e}")

    def delete_auto_scaling_group(self):
        try:
            self.autoscaling.delete_auto_scaling_group(
                AutoScalingGroupName=self.group_name,
                ForceDelete=True
            )
            print(f"Auto Scaling Group {self.group_name} deleted.")
        except ClientError as e:
            print(f"Error deleting Auto Scaling Group: {e}")
    