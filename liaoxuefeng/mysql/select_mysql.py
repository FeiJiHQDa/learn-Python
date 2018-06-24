import mysql.connector

conn = mysql.connector.connect(user='root', password='', database='test')
cursor = conn.cursor()
# cursor.execute('select * from user where id = %s', ('1',))


cursor.execute('select * from user')
values = cursor.fetchall()

# conn.start_transaction()
# conn.rollback()
# conn.commit()

print(values)

cursor.close()
