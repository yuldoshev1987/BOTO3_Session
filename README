============Creating of boto3 Session object====================
Session :
	store configuration information (primarily credentials of AWS root account or AWS IAM user account and selected region)
	
There are two type os sessions:
	Custom Session
	Default Session

aws configure --profile p-name
	import boto3
	session=boto3.Session(profile_name='lambdaDeveloper')
	s3_client=session.client('s3')
	response = s3_client.list_buckets()
	# Output the bucket names
	print('Existing buckets:')
	for bucket in response['Buckets']:
		print(bucket["Name"])
		
NOTE: If you do not declare your profile , it will take your default profile 
if you have multiple IAM user with different IAM role , you can mention in your code		
