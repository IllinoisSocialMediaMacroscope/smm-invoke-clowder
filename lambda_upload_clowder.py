import requests
import json

# global
headers = {'Content-type': 'application/json', 'accept': 'application/json'}

def add_tags(fileID, auth, tags):
    payload = json.dumps({'tags':tags})
    r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/tags',
                 data=payload,
                 headers=headers,
                 auth=auth)
    print(r.status_code)
    print(r.text)
    
def add_descriptions(fileID, auth, descriptions):
    payload = json.dumps({'description':descriptions})
    r = requests.put('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/updateDescription',
                     data=payload,
                     headers=headers,
                     auth=auth)
    print(r.status_code)
    print(r.text)
    
def add_metadata(fileID, auth, metadata):
    payload = json.dumps(metadata)
    r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/metadata',
                 data=payload,
                 headers=headers,
                 auth=auth)
    print(r.status_code)
    print(r.text)
    
def lambda_handler(event, context):
  
    # basic fields
    auth = (event['username'],event['password'])
    dataset_id = event['payload']['dataset_id']
   
    # loop through URL list
    file_id = []
    
    for url in event['payload'].keys():
        if url != 'dataset_id':
            r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/urls',
                     data=json.dumps({'url':url}),
                     headers=headers,
                     auth=auth)    
            if r.status_code != 200:
                return {'info': r.text, 'ids': [] }
                exit()
            else:
                file_id.append(r.json()['id'])
                
                if 'tags' in event['payload'][url].keys():
                    try:
                        add_tags(r.json()['id'], auth, event['payload'][url]['tags'])
                    except:
                        print('cannot add tags to this file: ', r.json()['id'])
                      
                if 'metadata' in event ['payload'][url].keys():
                    try:
                        add_metadata(r.json()['id'], auth, event['payload'][url]['metadata'])
                    except:
                        print('cannot add metadata to this file: ', r.json()['id'])
                        
                if 'descriptions' in event['payload'][url].keys():
                    try:
                        add_descriptions(r.json()['id'], auth, event['payload'][url]['descriptions'])
                    except:
                        print('cannot add tags to this file: ', r.json()['id'])

    return {'info': 'You have successfully uploaded all the files to your specified dataset!',
            'ids': file_id }
    
    

    
    
