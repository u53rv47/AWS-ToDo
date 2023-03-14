import os
import json

import boto3
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    data = event['queryStringParameters']
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # delete the todo from the database
    table.delete_item(
        Key={
            'id': data['id']
        }
    )

    # create a response
    response = {
        "statusCode": 200,
        "headers": event['headers'],
        "body": json.dumps({"Result": "Deleted"}),
        "isBase64Encoded": True
    }

    return response
