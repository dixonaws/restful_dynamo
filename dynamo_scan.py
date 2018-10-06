import boto3
from boto3 import Key

def main():
	dynamodb=boto3.client('dynamodb')

	strEmployeeId='8675309'

	table = dynamodb.Table('employees')


	response = table.query(KeyConditionExpression=Key('employee_id').eq(strEmployeeId))

	# todo: this will need to be adjusted
	print(response['Items'][0]['name'])


main()