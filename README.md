# invokeClowder
scripts to interact with Clowder 

### Endpoint used:
1. create spaces
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces/' + sp_id +'/updateUsers'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/me'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces'
    
2. create collections
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/collections'

3. upload files to dataset
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/tags'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/updateDescription'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/metadata'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/urls'

4. create dataset (lambda_invoke_clowder.py)
*TODO: Bad script name, change it later*
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/createempty'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/metadata'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/tags'
    
5. list spaces, collections, datasets, people
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/collections/allCollections'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces/canEdit'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/users?key=Globalkey'
