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

### Modify the code to query a DynamoDB table
The app.py program in your Chalice project folder is the Lambda function behind your API. Use 
dynamo_query.py and dynamo_scan.py as a reference to modify app.py to get 
information from a DynamoDB table.

