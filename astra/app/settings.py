import os

#DB_URL = 'mysql://root:@localhost/zakupki'
DB_URL = os.getenv('DB_URL', 'postgres://admin:secret@localhost/postgres')
DB_UPDATE_SCHEMA = True
