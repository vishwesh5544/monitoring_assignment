
# AWS Infrastructure Management System

This project provides an automated infrastructure management system on AWS, using Python and `boto3` in an OOP style. The system deploys a web application hosted on EC2 instances, sets up load balancing, configures auto-scaling, and sends SNS notifications for monitoring and scaling events.

## Project Structure

The project consists of the following modules, each responsible for a different AWS component:

- `s3_bucket.py`: Manages an S3 bucket for static file storage.
- `ec2_instance.py`: Launches and manages an EC2 instance to host the web application.
- `load_balancer.py`: Sets up and manages an Application Load Balancer (ALB) to distribute traffic.
- `auto_scaling_group.py`: Configures an Auto Scaling Group (ASG) for scaling EC2 instances based on demand.
- `sns_notifier.py`: Sets up SNS notifications for monitoring infrastructure events.
- `main.py`: The main orchestrator file that deploys or tears down the entire infrastructure.

## Requirements

Ensure you have the following installed:

- Python 3.6+
- `boto3` library: Install it using `pip install boto3`.
- AWS CLI configured with appropriate credentials (`aws configure`). The IAM user should have permissions for EC2, S3, ELB, Auto Scaling, and SNS.

## Usage

The `main.py` script can deploy or tear down the infrastructure based on user input.

### Deploy Infrastructure

To deploy the infrastructure:

```bash
python main.py
```

When prompted, enter `deploy` to initiate the deployment.

### Tear Down Infrastructure

To tear down the infrastructure:

```bash
python main.py
```

When prompted, enter `teardown` to delete all created resources.

## Module Details

### S3 Bucket

- `create_bucket()`: Creates an S3 bucket for storing static files.
- `delete_bucket()`: Deletes the S3 bucket along with all objects.

### EC2 Instance

- `launch_instance()`: Launches an EC2 instance and configures it as a web server.
- `terminate_instance()`: Terminates the EC2 instance.

### Load Balancer

- `create_load_balancer()`: Creates an ALB and registers EC2 instances.
- `delete_load_balancer()`: Deletes the load balancer.

### Auto Scaling Group

- `create_auto_scaling_group(min_size, max_size)`: Creates an ASG with specified scaling limits.
- `delete_auto_scaling_group()`: Deletes the ASG.

### SNS Notifier

- `create_topic(name)`: Creates an SNS topic for alerts.
- `subscribe_email(topic_arn, email)`: Subscribes an email address for notifications.
- `delete_topic(topic_arn)`: Deletes the SNS topic.

## Notes

This project automates the infrastructure lifecycle but does not include an actual web application. You may add your application files and deployment steps as needed.
