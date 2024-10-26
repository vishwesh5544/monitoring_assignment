
from s3_bucket import S3Bucket
from ec2_instance import EC2Instance
from load_balancer import LoadBalancer
from auto_scaling_group import AutoScalingGroup
from sns_notifier import SNSNotifier

def deploy_infrastructure():
    s3_bucket = S3Bucket("my-web-app-bucket")
    s3_bucket.create_bucket()

    ec2_instance = EC2Instance("t2.micro", "my-key-pair", "my-security-group")
    instance = ec2_instance.launch_instance()

    load_balancer = LoadBalancer("my-load-balancer", "my-security-group", ["subnet-xxxx", "subnet-yyyy"])
    load_balancer_arn = load_balancer.create_load_balancer()

    asg = AutoScalingGroup("my-auto-scaling-group", "my-launch-configuration", ["subnet-xxxx", "subnet-yyyy"])
    asg.create_auto_scaling_group(min_size=1, max_size=3)

    sns_notifier = SNSNotifier()
    topic_arn = sns_notifier.create_topic("infrastructure-alerts")
    sns_notifier.subscribe_email(topic_arn, "admin@example.com")

def teardown_infrastructure():
    sns_notifier = SNSNotifier()
    sns_notifier.delete_topic("infrastructure-alerts-topic-arn")

    asg = AutoScalingGroup("my-auto-scaling-group", "my-launch-configuration", ["subnet-xxxx", "subnet-yyyy"])
    asg.delete_auto_scaling_group()

    load_balancer = LoadBalancer("my-load-balancer", "my-security-group", ["subnet-xxxx", "subnet-yyyy"])
    load_balancer.delete_load_balancer()

    ec2_instance = EC2Instance("t2.micro", "my-key-pair", "my-security-group")
    ec2_instance.terminate_instance()

    s3_bucket = S3Bucket("my-web-app-bucket")
    s3_bucket.delete_bucket()

if __name__ == "__main__":
    action = input("Enter 'deploy' to create infrastructure or 'teardown' to delete it: ").strip().lower()
    if action == "deploy":
        deploy_infrastructure()
    elif action == "teardown":
        teardown_infrastructure()
    else:
        print("Invalid action. Please enter 'deploy' or 'teardown'.")
    