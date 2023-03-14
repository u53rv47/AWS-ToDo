import boto3
import json
import requests
import datetime
from pprint import pprint

print('Time:', datetime.datetime.now())


dynamodb_client = boto3.client('dynamodb')
response = dynamodb_client.scan(
    TableName='ToDo',
    AttributesToGet=['id']
)
ids = []
for item in response['Items']:
    ids.append(int(item['id']['S']))

print('Id:', ids)


def get_id():
    if len(ids) == 0:
        return str(0)
    for id in range(max(ids)):
        if id not in ids:
            ids.append(id)
            return str(id)
    return str(max(ids) + 1)


headers = {
    'authorizationToken': 'FA2S1G4FTY2HJNDFG3D'
}

# vijaysingh88086@gmail.com
# url = 'https://t78ebyp3ve.execute-api.ap-south-1.amazonaws.com/test/'

# vijaysingh997022@gmail.com
url = 'https://da0ou7ll4g.execute-api.ap-south-1.amazonaws.com/Prod/'


######################################  CREATE  #####################################
# body = {
#     'id': get_id(),
#     'todo': 'This is my first Python ToDo.',
#     'checked': 'no'
# }
# create_url = url + 'create-todo'
# post_response = requests.post(create_url, json=body).json()
# pprint(post_response)


# #######################################  GET  #######################################
# params = {
#     "id": "1"
# }
# get_url = url + 'get-todo'
# response = requests.get(get_url, params=params).json()
# pprint(response)


# #######################################  DELETE  #####################################
# params = {
#     "id": "1"
# }
# delete_url = url + 'delete-todo'
# response = requests.delete(
#     delete_url, params=params).json()
# pprint(response)


#######################################  UPDATE  #######################################
params = {
    "id": "0"
}
body = {
    'todo': 'This is my new updated Python ToDo.',
    'checked': 'no'
}
update_url = url + 'update-todo'
update_response = requests.patch(update_url, params=params, json=body).json()
pprint(update_response)


# #######################################  LIST  #######################################
# get_url = url + 'list-todo'
# response = requests.get(get_url).json()
# pprint(response)


#######################################  TEMP  #######################################

# url = 'https://sw7nkioh75.execute-api.ap-south-1.amazonaws.com/Prod/hello'
# response = requests.get(url).json()
# pprint(response)
