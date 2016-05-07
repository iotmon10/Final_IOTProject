# *********************************************************************************************
# All S3 related helper function
# *********************************************************************************************
import time,sys,json

import boto3

from botocore.exceptions import ClientError 

import aws

class S3(object):
	S3 = None
	S3_BUCKET_NAME = 'finalBaochan'
	S3Bucket = None
	trainingData = None


	def __init__(self,trainingData):
		self.S3 = aws.getResource('s3','us-east-1')
		self.trainingData = trainingData


	def uploadData(self):

		if self.bucketExists():	
			self.S3Bucket = self.S3.Bucket(self.S3_BUCKET_NAME)
		else:
			self.S3Bucket = self.S3.create_bucket(Bucket=self.S3_BUCKET_NAME)

		# Upload data to S3
		self.uploadToS3()		

	def uploadToS3(self):
	 	with open(self.trainingData,'rU') as data:
			# uploading data
			self.S3Bucket.Object(self.trainingData).put(Body=data)

	def bucketExists(self):
	    try:
	    	# Get S3 bucket related details
	        self.S3.meta.client.head_bucket(Bucket=self.S3_BUCKET_NAME)
	        return True

	    except ClientError:
	        return False



    	

	
