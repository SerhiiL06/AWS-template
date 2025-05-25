from types_boto3_s3 import S3Client as S3
from types_boto3_ec2 import EC2Client as EC2
import boto3

s3_client: S3 = boto3.client("s3")
ec2_client: EC2 = boto3.client("ec2")
