import boto3

def hello(event, context):
    print("Second Update.")
    client = boto3.client('lambda')
    response = client.list_functions()
    return response
