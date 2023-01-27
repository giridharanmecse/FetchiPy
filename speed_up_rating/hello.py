import requests
import static
import json

query = static.solved_count_query

variables = {'username': 'RIHANABANU'}

url = 'https://leetcode.com/graphql/'
r = requests.post(url, json={'query': query, 'variables': variables})

json_data_count = json.loads(r.text)
print(json_data_count)
usernameHandle = json_data_count['data']['matchedUser']['username']
total = json_data_count['data']['matchedUser']['submitStats']['acSubmissionNum'][0]['count']
easy = json_data_count['data']['matchedUser']['submitStats']['acSubmissionNum'][1]['count']
med = json_data_count['data']['matchedUser']['submitStats']['acSubmissionNum'][2]['count']
hard = json_data_count['data']['matchedUser']['submitStats']['acSubmissionNum'][3]['count']

print(total)