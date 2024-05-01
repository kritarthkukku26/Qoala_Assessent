import boto3
import datetime
import os

def backup_s3_bucket(bucket_name, backup_folder):
    """
    Function to backup an AWS S3 bucket to a local folder.

    Args:
    - bucket_name: Name of the S3 bucket to backup.
    - backup_folder: Local folder where the backup will be saved.
    """
    # Initialize Boto3 S3 client
    s3 = boto3.client('s3')

    # Create a timestamped folder for backup
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_path = os.path.join(backup_folder, f'backup_{timestamp}')
    os.makedirs(backup_path)

    try:
        # List objects in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']

        # Download each object to the backup folder
        for obj in objects:
            key = obj['Key']
            local_file_path = os.path.join(backup_path, key)
            s3.download_file(bucket_name, key, local_file_path)
            print(f'Downloaded: {key}')

        print(f'Backup completed successfully. Files saved to: {backup_path}')
    except Exception as e:
        print(f'Backup failed: {str(e)}')

if __name__ == '__main__':
    # Specify your AWS credentials and S3 bucket name
    AWS_ACCESS_KEY_ID = 'YOUR_ACCESS_KEY_ID'
    AWS_SECRET_ACCESS_KEY = 'YOUR_SECRET_ACCESS_KEY'
    BUCKET_NAME = 'YOUR_S3_BUCKET_NAME'

    # Specify the local backup folder path
    BACKUP_FOLDER = '/path/to/backup/folder'

    # Set AWS credentials
    os.environ['AWS_ACCESS_KEY_ID'] = AWS_ACCESS_KEY_ID
    os.environ['AWS_SECRET_ACCESS_KEY'] = AWS_SECRET_ACCESS_KEY

    # Perform the backup
    backup_s3_bucket(BUCKET_NAME, BACKUP_FOLDER)
