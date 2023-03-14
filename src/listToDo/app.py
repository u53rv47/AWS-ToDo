import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan()

    # create a response

    response = {
        "statusCode": 200,
        "headers": event['headers'],
        "body": json.dumps(result['Items']),
        "isBase64Encoded": True
    }
    return response
