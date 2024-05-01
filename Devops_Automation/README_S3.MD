S3 Bucket Backup Script

This Python script allows you to backup an AWS S3 bucket to a local folder. It uses the Boto3 library to interact with AWS services.

Prerequisites
Before running the script, ensure that you have the following:

Python installed on your machine.
Boto3 library installed (pip install boto3).
AWS credentials with permissions to access the specified S3 bucket.


Usage
Clone the Repository: Clone or download the repository containing the script to your local machine.
Set Up AWS Credentials:
Specify your AWS access key ID and secret access key in the script.
Alternatively, you can set these credentials as environment variables.
Specify S3 Bucket and Backup Folder:
Set the BUCKET_NAME variable to the name of the S3 bucket you want to backup.
Set the BACKUP_FOLDER variable to the local folder path where the backup will be saved.
