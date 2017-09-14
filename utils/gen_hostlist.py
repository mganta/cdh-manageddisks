import json
from pprint import pprint
json_file='hosts.json'
hosts_file = open('hosts.txt', 'w')
json_data=open(json_file)
data = json.load(json_data)
for x in data['items']:
    print(x['ipAddress'] + "  " + x['hostname'].split(".")[0] +".cdh-worker.internal " + x['hostname'].split(".")[0])
    hosts_file.write(x['ipAddress'] + "  " + x['hostname'].split(".")[0] +".cdh-worker.internal " + x['hostname'].split(".")[0] +"\n")

json_data.close()
hosts_file.close()
