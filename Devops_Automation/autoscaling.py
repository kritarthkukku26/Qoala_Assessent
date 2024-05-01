import boto3
import time

# Initialize the boto3 client for Auto Scaling
autoscaling_client = boto3.client('autoscaling')

# Define the name of your Auto Scaling Group
autoscaling_group_name = 'your-autoscaling-group-name'

# Get the current desired capacity of the Auto Scaling Group
response = autoscaling_client.describe_auto_scaling_groups(AutoScalingGroupNames=[autoscaling_group_name])
current_capacity = response['AutoScalingGroups'][0]['DesiredCapacity']

# Update the desired capacity to trigger rolling updates
new_capacity = current_capacity + 1  # Increase desired capacity by 1
response = autoscaling_client.update_auto_scaling_group(
    AutoScalingGroupName=autoscaling_group_name,
    DesiredCapacity=new_capacity
)

# Wait for the instances to be healthy in the load balancer before proceeding
elbv2_client = boto3.client('elbv2')

while True:
    response = elbv2_client.describe_target_health(TargetGroupArn='your-target-group-arn')
    healthy_instance_count = sum(1 for target in response['TargetHealthDescriptions'] if target['TargetHealth']['State'] == 'healthy')

    if healthy_instance_count >= new_capacity:
        print("All instances are healthy in the target group.")
        break
    else:
        print("Waiting for instances to become healthy...")
        time.sleep(10)  # Wait for 10 seconds before checking again

# Update the desired capacity back to the original value to complete the rolling update
response = autoscaling_client.update_auto_scaling_group(
    AutoScalingGroupName=autoscaling_group_name,
    DesiredCapacity=current_capacity
)
