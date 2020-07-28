import requests
import json

limit = 500
path = "https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limat=%d"
path = path % limit
data = requests.get(path).text # data
dict = json.loads(data)
youbikes = dict.get('result').get('records')  # list型態

print(type(data),type(dict),type(youbikes))