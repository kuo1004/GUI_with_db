import mysql.connector as myconn
import hashlib

db=myconn.connect(
        host="localhost",
        user="Kuo",
        password="D1146229",
        database="kuo",
    )
my_cursor = db.cursor()

sql = '''CREATE TABLE selectPhone (
  id INT PRIMARY KEY AUTO_INCREMENT,
  article VARCHAR(255) NOT NULL,
  number VARCHAR(255) NOT NULL
  );'''
my_cursor.execute(sql)

my_cursor.execute('SHOW TABLES')
for table in my_cursor:
    print(table[0])

#m = hashlib.sha256()
#name = "KUO"
#pw = '1146229'
#m.update(pw.encode('utf-8'))
#pw_h = m.hexdigest()


#insert_query = "INSERT INTO `users2` (username, password) VALUES (%s, %s)"
#my_cursor.execute(insert_query, (name,pw_h))

#db.commit()