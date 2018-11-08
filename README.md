# smm-invoke-clowder
![](https://clowder.ncsa.illinois.edu/img/logo.png)

**This repository hosts scripts to interact with <a href="https://clowder.ncsa.illinois.edu/" target="_blank">NCSA Clowder</a>.**  

Clowder is a research data management system designed to support any data format and multiple research domains. 
When new data is added to the system, whether it is via the web front-end or through its Web service API, 
a cluster of extraction services process the data to extract interesting metadata and create web based data 
visualizations.

**Each script is designed to be deployed on <a href="https://aws.amazon.com/lambda" target="_blank">AWS Lambda</a>.**

### Endpoint used:
1. **create spaces** (clowder_create_space.py)
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces/' + sp_id +'/updateUsers'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/me'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces'
    
2. **create collections** (clowder_create_collection.py)
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/collections'

3. **upload files to dataset** (clowder_upload_file.py)
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/tags'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/updateDescription'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/files/' + fileID +'/metadata'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/urls'

4. **create dataset** (clowder_create_dataset.py)
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/createempty'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/metadata'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets/' + dataset_id +'/tags'
    
5. **list spaces, collections, datasets, and people** (clowder_list.py)
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/datasets'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/collections/allCollections'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/spaces/canEdit'
    * 'https://socialmediamacroscope.ncsa.illinois.edu/clowder/api/users?key=Globalkey'
