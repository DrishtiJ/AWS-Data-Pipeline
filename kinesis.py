import boto3

kinesis = boto3.client('kinesis')

response = kinesis.create_stream(
    StreamName='new-stream',
    ShardCount=1
)

putData = kinesis.put_record(
    StreamName='new-stream',
    Data='Hello world',
    PartitionKey='partitionKey'
)