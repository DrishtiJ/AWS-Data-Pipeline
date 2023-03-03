import boto3

glue = boto3.client('glue')

response = glue.create_job(
    Name='new-job',
    Role='arn:aws:iam::ACCOUNT_ID:role/GlueServiceRole',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://my-bucket/scripts/my-script.py'
    }
)