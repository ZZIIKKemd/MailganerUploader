import os
import sqlite3

import requests
import yaml

current_path = os.getcwd() + '/'

# getting config
with open(current_path+'config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)

# opening db
db = sqlite3.connect(current_path+'data.sqlite')
data_cursor = db.cursor()

# getting unsent user
data_cursor.execute('select * from users where processed = \'\'')
user = data_cursor.fetchone()

# preparing request data
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'CodeRequest ' + config['api_key']
}
post_data = {
    'email': user[0],
    'name': user[1],
    'patronymic': user[2],
    'surname': user[3],
    'source': config['source']
}

# performing request
mailganer = requests.post('https://mailganer.com/api/v2/emails/',
                          json=post_data, headers=headers)
returned = mailganer.json()

# setting user as processed
if returned.get('id'):
    query = 'update users set processed = \'Y\' where email = \'{}\''
    data_cursor.execute(query.format(user[0]))
db.commit()

# closing db
db.close()
