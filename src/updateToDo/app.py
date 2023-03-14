import os
import json
import datetime
import logging

# from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    data = json.loads(event['body'])
    if 'todo' not in data or 'checked' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")

    updateTime = str(datetime.datetime.now())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the todo in the database
    result = table.update_item(
        Key={
            'id': event['queryStringParameters']['id']
        },

        ExpressionAttributeValues={
            ':var0': data['todo'],
            ':var1': data['checked'],
            ':var2': updateTime
        },

        UpdateExpression="set todo = :var0, checked = :var1, updatedAt = :var2",

        ReturnValues='ALL_NEW'
    )

    # create a response
    response = {
        "statusCode": 200,
        "headers": event['headers'],
        "body": json.dumps(result['Attributes']),
        "isBase64Encoded": True
    }

    return response
