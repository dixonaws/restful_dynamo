# restful_dynamo
Create a RESTful API that accesses a DynamoDB database through API Gateway and
Lambda.

### Create a virtualenv with Python 3.6 and activate it
```virtualenv `which python3` venv```

### Install dependencies
```pip install -r requirements.txt```

### Create a new Chalice project
```chalice new-project restful_dynamo_api```

### Test the API
Deploy locally with ```chalice local```
Does the API in its basic form work properly?

Deploy to AWS with ```chalice deploy```
Does the API in its basic form work properly?

### Create a DynamoDB table
Create a table called ```employees``` with employee_id as the primary key (an integer)

> Spelling and case are critical: employee_ID or Employee_id are not the same as <b>employee_id</b>

### Add a sample record to your DynamoDB table
Use the dynamo_put.py program to put an item into your table.

### Get a record from your DynamoDB table
use dynamo_scan.py and dynamo_query.py programs to retrieve items from your DynamoDB table.
 
> Username/password credentials are not used in DynamoDB. Authenticaiotn and aurthoeization is 
> handled by AWS IAM
> You may have to modify the IAM role that your Lambda function uses to query Dynamo

### Modify the code to query a DynamoDB table
The app.py program in your Chalice project folder is the Lambda function behind your API. Use 
dynamo_query.py and dynamo_scan.py as a reference to modify app.py to get 
information from a DynamoDB table.

