import boto3
s3 = boto3.client('s3')
for b in s3.list_buckets()['Buckets']:
    print(b['Name'])
    for obj in s3.list_objects_v2(Bucket=b['Name']).get('Contents', []):
        print('  ', obj['Key'])

