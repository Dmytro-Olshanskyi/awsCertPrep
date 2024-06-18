import boto3
import json

def lambda_handler(event, content):
    print("Recived event: {event}")
    
    #Setting boto3 client
    ec2 = boto3.client('ec2')
    
    #Grabbing instance ID from event
    instance_id = event['detail']['instance_id']
    
    #Restarting instance
    responce = ec2.start_instance(InstanceIds=[instance_id])
    print('Started instance: ' + instance_id)
    return {
        'statusCode': 200,
        'body' : json.dumps('Started instance: ' + instance_id)
    }
    