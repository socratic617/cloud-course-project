import boto3

BUCKET_NAME = "cloud-course-bucket-erik"

s3_client = boto3.client("s3")

# write a file to the s3 bucket with the contents "Hello, World!"
s3_client.put_object(Bucket=BUCKET_NAME, Key="folder/hello.txt", Body="Hello, World!")
