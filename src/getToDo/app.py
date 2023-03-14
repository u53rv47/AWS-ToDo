import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    data = event['queryStringParameters']
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id': data['id']
        }
    )

    # create a response

    response = {
        "statusCode": 200,
        "headers": event['headers'],
        "body": json.dumps(result['Item']),
        "isBase64Encoded": True
    }
    return response
