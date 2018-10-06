import boto3

def main():
	dynamodb_resource = boto3.resource('dynamodb')

	strDynamoTable = "employees"
	table = dynamodb_resource.Table(strDynamoTable)

	response = table.scan()

	print(response)

main()
