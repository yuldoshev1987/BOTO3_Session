import boto3
session=boto3.Session(profile_name='lambdaDeveloper')
s3_client=session.client('s3')
response = s3_client.list_buckets()
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(bucket["Name"])