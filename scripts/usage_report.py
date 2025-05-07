#!/usr/bin/env python3
import boto3
from datetime import datetime, timedelta

cw = boto3.client('cloudwatch', region_name='us-east-1')
instance_id = 'i-0d6c82a1c1f16d80b'

metrics = cw.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
    StartTime=datetime.utcnow() - timedelta(hours=1),
    EndTime=datetime.utcnow(),
    Period=300,
    Statistics=['Average']
)

print(f"CPU data for {instance_id}:")
for point in metrics['Datapoints']:
    ts = point['Timestamp']
    avg = point['Average']
    print(f" - {ts}: {avg:.2f}%")
