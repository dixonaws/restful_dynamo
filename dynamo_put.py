import boto3
from boto3.dynamodb.conditions import Key
import sys
from boto3 import resource
import json

dynamodb_resource = resource('dynamodb')


def main():
	strDynamoTable = "employees"
	table = dynamodb_resource.Table(strDynamoTable)

	sys.stdout.write('Inserting data into Dynamo table ' + strDynamoTable + '... ')
	dictRow = {}
	dictRow['employee_id'] = 8675309

	dictRow['data'] = '{ ' \
					  '"firstName": "John",' \
					  '"lastName": "Dixon",' \
					  '"phone": "+12482192900",' \
					  '"email": "dixonaws@amazon.com",' \
					  '"addressLine1": "150 W Jefferson",' \
					  '"addressLine2": "2nd Floor",' \
					  '"city": "Detroit", ' \
					  '"state": "MI", ' \
					  '"zipcode": "48988", ' \
					  '"company": "AWS", ' \
					  '"userid": "dixonaws",' \
					  '"employeeType": "employee",' \
					  '"manager": "Bezos, Jeff",' \
					  '"managerEmail": "jeff@amazon.com"}'

	response = table.put_item(Item=dictRow)

	if (response['ResponseMetadata']['HTTPStatusCode']) == 200:
		print("Insert successful, (RequestId: " + response['ResponseMetadata']['RequestId'] + ")")
	else:
		print(
			"Something went wrong: response code " + response['ResponseMetadata']['HTTPStatusCode'] + " from DynamoDB")

	print('Getting item from Dynamo table...')

	response = table.get_item(Key={'employee_id': 8675309})

	# print(json.dumps(response['Item']['data'], indent=4, separators=(',', ': ')))

	print("Loading into a Python dict...")
	dictItem = json.loads(response['Item']['data'])

	print('dictItem: ' + json.dumps(dictItem, indent=4, separators=(',', ': ')))


main()
