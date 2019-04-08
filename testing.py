import requests

url = "http://localhost:5000/add"
expression = {'expression': "3+2"}

res = requests.post(url, data=expression)

# verify correct expression
from sqlalchemy import create_engine

engine = create_engine('postgresql://cs162_user:cs162_password@db:5432/cs162', echo=True)


connection = engine.connect()
try:
	result = connection.execute("SELECT value FROM Expression WHERE text='3+2'")
	print(result == 5)
except:
	print("something went wrong")
# incorrect expression 
incorrect = {"expression": "Hello xDD"}

res = requests.post(url, data=incorrect)

try: 
	result = connection.execute("SELECT * FROM Expression")
	print(result)
except:
	print("something went wrong")

connection.close()
