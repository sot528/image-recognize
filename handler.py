import os
import json
import boto3


def endpoint(event, context):
    fileName = 'input.jpg'
    bucket = os.environ['BUCKET']

    client = boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': fileName}})

    print('Detected labels for ' + fileName)
    return response

    # for label in response['Labels']:
    #     print(label['Name'] + ' : ' + str(label['Confidence']))
