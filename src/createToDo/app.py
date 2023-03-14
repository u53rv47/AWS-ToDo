import logging
import os
import json
import datetime
import boto3

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the todo item.")

    timestamp = str(datetime.datetime.now())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': data['id'],
        'text': data['text'],
        'checked': False,
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # write the todo to the database
    table.put_item(Item=item)

    # # create a response

    response = {
        "statusCode": 200,
        "headers": event['headers'],
        "body": json.dumps(item),
        "isBase64Encoded": True
    }

    return response
