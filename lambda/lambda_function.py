import json

def lambda_handler(event, context):
 return {
     'statusCode': 200,
     'body': json.dumps('Hello lambda from vs code this is Ans 2nd ')
    }
