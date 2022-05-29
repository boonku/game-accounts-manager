from cryptography.fernet import Fernet
import os.path
import sqlite3
import config

root_dir = config.app['root_dir']


def create_db():
    db_name = config.database['name']
    db_script = config.script['name']
    # run sql script if database doesnt exist
    if not os.path.exists(root_dir + db_name):
        # create tables and inserts platforms into table
        with open(root_dir + db_script) as sql_file:
            conn = sqlite3.connect(root_dir + db_name)
            cursor = conn.cursor()
            sql_script = sql_file.read()
            cursor.executescript(sql_script)
            conn.commit()
            conn.close()


# generate key for symmetric encryption
def create_key():
    key_file = config.encryption['file']
    if not os.path.exists(root_dir + key_file):
        with open(root_dir + key_file, 'wb') as file:
            key = Fernet.generate_key()
            file.write(key)

