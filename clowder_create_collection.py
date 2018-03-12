import requests
import json

def lambda_handler(event, context):
    # basic fields
    auth = (event['username'],event['password'])
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
        
    # create collection
    name = event['payload']['name']
    data = {'name':name}
    
    if 'descriptions' in event['payload'].keys():
        data['description'] = event['payload']['descriptions']
    if 'space' in event['payload'].keys():
        data['space'] = event['payload']['space']
   
    r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/collections',
                 data=json.dumps(data),
                 headers=headers,
                 auth=auth)
   
    print(r.status_code)
    print(r.text)
    
    if r.status_code != 200:
        return {'info': r.text, 'id': 'null' }
        exit()
    else:
        return {'info':'successfully created the new collection!', 'id':r.json()['id']}
    
