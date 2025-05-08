import boto3
db = boto3.resource('dynamodb')
table = db.create_table(
    TableName='Lebron',
    KeySchema=[{'AttributeName':'id','KeyType':'HASH'}],
    AttributeDefinitions=[{'AttributeName':'id','AttributeType':'N'}],
    BillingMode='PAY_PER_REQUEST'
)
table.wait_until_exists()
table.put_item(Item={'id':1,'title':'Test'})
print(table.get_item(Key={'id':1})['Item'])
