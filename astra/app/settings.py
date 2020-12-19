import os

#DB_URL = 'mysql://root:@localhost/zakupki'
DB_URL = os.getenv('DB_URL', 'postgres://admin:secret@localhost/postgres')
DOCKER_LIST = [
    'http://gosparcer:8000/feed'

]
DB_UPDATE_SCHEMA = True
