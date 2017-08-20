
import pymysql
db = pymysql.connect('localhost', 'root', '', 'test')

cursor = db.cursor()

cursor.execute('select * from python')
data = cursor.fetchall()

# print('Databases version %s' % data)

for name in data:
    print(name)

db.close()