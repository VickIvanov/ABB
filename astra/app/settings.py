import os

#DB_URL = 'mysql://root:@localhost/zakupki'
DB_URL = os.getenv('DB_URL', 'postgres://admin:secret@localhost/postgres')

DOCKER_LIST = [
    'http://gosparser:8000/'

]
DB_UPDATE_SCHEMA = True
