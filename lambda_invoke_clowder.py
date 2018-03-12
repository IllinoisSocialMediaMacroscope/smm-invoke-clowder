import requests
import json

def lambda_handler(event, context):
    # basic fields
    auth = (event['username'],event['password'])
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
        
    # create dataset
    title = event['payload']['title']
    data = {'name':title, 'access':'PRIVATE'}
    
    if 'collection' in event['payload'].keys():
        data['collection'] = event['payload']['collection']
    if 'space' in event['payload'].keys():
        data['space'] = event['payload']['space']
    if 'descriptions' in event['payload'].keys():
        data['description'] = event['payload']['descriptions']
   
    r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/createempty',
                     data=json.dumps(data),
                     headers=headers,
                     auth=auth)
    if r.status_code != 200:
        return {'info': r.text, 'id': 'null' }
        exit()
    else:
        dataset_id = r.json()['id']
    
    
    # if metadata exist, add metada
    if 'metadata' in event['payload'].keys():
        metadata = event['payload']['metadata']
        r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/metadata',
                         data=json.dumps(metadata),
                         headers=headers,
                         auth=auth)
        # if fail, return fail info and dataset id 
        if r.status_code != 200:
            return {'info': r.text, 'id': dataset_id}
            exit()
            
    # if tag exist, add tags
    if 'tags' in event['payload'].keys():
        tags = {'tags': event['payload']['tags']}
        r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/tags',
                         data=json.dumps(tags),
                         headers=headers,
                         auth=auth)
        # if fail, return fail info and dataset id 
        if r.status_code != 200:
            return {'info': r.text, 'id': dataset_id}
            exit()
    
    return {'info':'successfully created the new dataset!', 'id':dataset_id}
    
