import requests
import json

def lambda_handler(event, context):
    # basic fields
    auth = (event['username'],event['password'])
    headers = {'Content-type': 'application/json', 'accept': 'application/json'}
    
    # private method add user to space
    def _addUser(sp_id, usr_id, role):
        data = {'rolesandusers':{role:usr_id}}
        r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces/' + sp_id +'/updateUsers',
                 data=json.dumps(data),
                 headers=headers,
                 auth=auth)
        if r.status_code != 200:
            print('addUser')
            print(r.text)
            return None
        else:
            return r.text
            
    # private method to identify myself
    def _findMyself(username):
        r = requests.get('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/me', 
            auth=auth)
        
        if r.status_code != 200:
            print('findMyself')
            print(r.text)
            return None
        else:
            return r.json()['id']
    
    # create collection
    name = event['payload']['name']
    data = {'name':name}
    
    if 'descriptions' in event['payload'].keys():
        data['description'] = event['payload']['descriptions']
    else:
        # important: description seems to be an required parameter
        data['description'] = ''
        
    r = requests.post('https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces',
                 data=json.dumps(data),
                 headers=headers,
                 auth=auth)
       
    if r.status_code != 200:
        print('create collection')
        return {'info': r.text, 'id': 'null' }
        exit()
    
    else:
        # identify myself
        my_id = _findMyself(event['username'])
        if my_id == None:
            return {'info': 'cannot add yourself/person to this space, please to go clowder to add', 'id': 'null' }
            exit()
        
        # add myself as Admin
        if _addUser(r.json()['id'], my_id, 'Admin') == None:
            return {'info': 'cannot add yourself/person to this space, please to go clowder to add', 'id': 'null' }
            exit()
            
        # add other people as Editor
        if 'usr_ids' in event['payload'].keys():
            if _addUser(r.json()['id'], event['payload']['usr_ids'], 'Editor') == None:
                return {'info': 'cannot add yourself/person to this space, please to go clowder to add', 'id': 'null' }
                exit()

        # success!!!   
        return {'info':'successfully created the new space!', 'id':r.json()['id']}
