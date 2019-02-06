import os
import boto3


def endpoint(event, context):
    fileName = 'input.jpg'
    bucket = os.environ['BUCKET']

    client = boto3.client('rekognition')

    # ラベル取得
    response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': fileName}})

    # テキスト認識(English only)
    # response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': fileName}})

    # 不適切な画像のラベルを取得
    # response = client.detect_moderation_labels(Image={'S3Object': {'Bucket': bucket, 'Name': fileName}})

    print('Detected labels for ' + fileName)
    return response
