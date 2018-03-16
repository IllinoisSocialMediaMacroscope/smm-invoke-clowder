import requests
import json

def lambda_handler(event, context):
    
    # basic fields
    auth = (event['username'],event['password'])
    
    if event['item'] == 'dataset':
        r = requests.get('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets', 
                     auth=auth)
        print('dataset')
        print(r.status_code)
        print(r.text)
        
    elif event['item'] == 'collection':
        r = requests.get('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/collections/allCollections',
                        auth=auth)
        print('collection')
        print(r.status_code)
        print(r.text)
        
    elif event['item'] == 'space':
        r = requests.get('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces/canEdit',
                    auth=auth)
        print('space')
        print(r.status_code)
        print(r.text)
    
    # use a global key here be careful of this information!!
    elif event['item'] == 'user':
        r = requests.get('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/users?key=Globalkey')
        print('user')
        print(r.status_code)
        print(r.text)
            
    else:
        return {'info':'cannot list ' + event['item'], 'data':['error']}
        exit()
        
    if r.status_code != 200:
        return {'info':r.text, 'data':['error']}
    else:
        return {'info':'successfully fetched list of dataset', 'data':r.json()}
