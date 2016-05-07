# Creating aws machine learning model
# This program uploads the finalData.csv file to S3, and used it as a data source to train a binary 
# classification model
import time,sys,random

import boto3

import S3

sys.path.append('utils')
import aws

client = aws.getClient('machinelearning','us-east-1')
TIMESTAMP  =  time.strftime('%Y-%m-%d-%H-%M-%S')
S3_BUCKET_NAME = "finalBaochan"
S3_FILE_NAME = 'training1.csv'
S3_URI = "s3://{0}/{1}".format(S3_BUCKET_NAME, S3_FILE_NAME)
DATA_SCHEMA =open("training1.csv.schema").read()

DATA_SOURCE_ID = 'finaldata2'
ML_MODEL_ID = 'finalmodel2'

testvariable = S3.S3(S3_FILE_NAME)
testvariable.uploadData()

response = client.create_data_source_from_s3(
    DataSourceId=DATA_SOURCE_ID,
    DataSourceName='finaldata',
    DataSpec={
        'DataLocationS3': S3_URI,
	'DataSchema': DATA_SCHEMA
    },
    ComputeStatistics=True
)
response1 = client.create_ml_model(
    MLModelId= ML_MODEL_ID,
    MLModelName='finalmodel',
    MLModelType='REGRESSION',
    TrainingDataSourceId= DATA_SOURCE_ID
)








