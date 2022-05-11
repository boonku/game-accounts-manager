import sqlite3
import config

db_name = config.database['name']
db_script = config.script['name']

conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# create tables and inserts platforms into table
with open(db_script) as sql_file:
    sql_script = sql_file.read()
    cursor.executescript(sql_script)
    conn.commit()
    print(f'created database \'{db_name}\' and tables inside')
conn.close()
