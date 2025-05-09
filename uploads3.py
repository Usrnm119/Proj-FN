import boto3
import os

# CONFIGURE THIS:
bucket_name = 'finale-artifacts-734c12a9'
local_folder = '/home/ec2-user/environment/Proj-FN/'

# Initialize S3 client
s3 = boto3.client('s3')

# Walk through local directory and upload each file
for root, dirs, files in os.walk(local_folder):
    for file in files:
        full_path = os.path.join(root, file)
        s3_key = os.path.relpath(full_path, local_folder)  # keeps folder structure
        print(f"Uploading {full_path} to s3://{bucket_name}/{s3_key}")
        s3.upload_file(full_path, bucket_name, s3_key)

print("Upload complete.")

