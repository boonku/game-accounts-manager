from cryptography.fernet import Fernet
import os.path
import sqlite3
import config

db_name = config.database['name']
db_script = config.script['name']
root_dir = config.app['root_dir']

# run sql script if database doesnt exist
if not os.path.exists(root_dir + db_name):
    conn = sqlite3.connect(root_dir + db_name)
    cursor = conn.cursor()

    # create tables and inserts platforms into table
    with open(db_script) as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)
        conn.commit()
        print(f'created database \'{db_name}\' and tables inside')
    conn.close()
else:
    print('error: database already exists')

# generate key for symmetric encryption
key_file = config.encryption['file']

if not os.path.exists(root_dir + key_file):
    with open(root_dir + key_file, 'wb') as file:
        key = Fernet.generate_key()
        file.write(key)
        print('created new encryption key')
else:
    print('error: secret already exists')
