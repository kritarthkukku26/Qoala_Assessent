This Python script allows you to perform rolling updates for an Auto Scaling Group in AWS. It increases the desired capacity of the Auto Scaling Group by one, waits for the new instances to become healthy in the load balancer target group, and then updates the desired capacity back to its original value to complete the rolling update.

Prerequisites
Before running the script, ensure that you have the following:

Python installed on your machine.
Boto3 library installed (pip install boto3).
AWS credentials with permissions to manage the Auto Scaling Group and access the load balancer target group.

Usage
Clone the Repository: Clone or download the repository containing the script to your local machine.
Set Up AWS Credentials:
Ensure that your AWS credentials are configured either through environment variables or in the AWS credentials file (~/.aws/credentials).
The credentials should have the necessary permissions to manage Auto Scaling Groups and access load balancer target groups.
Specify Auto Scaling Group and Target Group:
Set the autoscaling_group_name variable to the name of your Auto Scaling Group.
Set the 'your-target-group-arn' string to the ARN of your target group.