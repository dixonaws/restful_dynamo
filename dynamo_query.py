import boto3
from boto3.dynamodb.conditions import Key
import json

def main():
	dynamodb_resource = boto3.resource('dynamodb')

	strDynamoTable = "employees"
	table = dynamodb_resource.Table(strDynamoTable)

	intEmployeeId=8675309

	response = table.query(KeyConditionExpression=Key('employee_id').eq(intEmployeeId))

	print(response)

	print("Loading into a Python dict...")
	dictItem = json.loads(response['Items'][0]['data'])

	print('dictItem: ' + json.dumps(dictItem, indent=4, separators=(',', ': ')))


main()
