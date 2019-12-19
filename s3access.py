import boto3
from botocore.exceptions import ClientError

from bucket_operations import *



s3 = boto3.client('s3')

#file to upload
file_path = r"Statement_SES_2010-11-Teacher.csv"
#retrive all s3 bucket names
response = s3.list_buckets()

for eachbucket in response["Buckets"]:
    print("Bucket Name:", eachbucket["Name"])

#Load csv file in bucket
try:
    #open File object
    file_obj = open(file_path,"rb")
    mybucket = S3Bucket("bucketname")
    #mybucket.load_bucket(file_name, mybucket.name,s3)
    mybucket.load_obj_bucket(file_obj,mybucket.name,s3, "school_teacher.csv")
    print("File Load successful\n", response)
except ClientError as e:
    print(e)

