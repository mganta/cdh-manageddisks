# Pass in the URL for the Cloudera Manager server
echo 'Getting Hosts from: '$1
curl -u 'admin' 'http://'$1':7180/api/v14/hosts' > hosts.json
python gen_hostlist.py
