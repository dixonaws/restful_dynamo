from chalice import Chalice
import boto3
from boto3.dynamodb.conditions import Key
import json

app = Chalice(app_name='restful_dynamo_api')


@app.route('/')
def index():
	dynamodb_resource = boto3.resource('dynamodb')

	strDynamoTable = "employees"
	table = dynamodb_resource.Table(strDynamoTable)

	intEmployeeId = 8675309

	response = table.query(KeyConditionExpression=Key('employee_id').eq(intEmployeeId))

	print("Loading into a Python dict...")
	dictItem = json.loads(response['Items'][0]['data'])

	# we're allowed to return a Python dict object here, no encoding to JSON needed
	return(dictItem)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
