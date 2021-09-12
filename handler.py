import json
import boto3
import uuid

def initiator(event, context):
    response = {"statusCode": 200, 'headers':{
            'Access-Control-Allow-Origin': '*'
        }}

    try:
        body = json.loads(event['body'])
        file_name, file_type = body['name'], body['type']
        file_extension = file_name.split('.')[-1]
        file_name = "".join(file_name.split('.')[:-1])

        key = f'{file_name}-{str(uuid.uuid4())}.{file_extension}'
        url = boto3.client('s3').generate_presigned_url(
            ClientMethod='put_object', 
            Params={
                'Bucket': 'utils-s3-uploader', 
                'Key': key,
                'ContentType': file_type,
            },
            ExpiresIn=3600)
        response['body'] = json.dumps({'url': url, 'key': key})
    except Exception as e:
        response['statusCode'] = 500
        response['body'] = json.dumps({'error': 'Presigned URL could not be generated'})

    return response