import MySQLdb
db = MySQLdb.connect(user='root', db='test', passwd='19890823', host='localhost')
cursor = db.cursor()
value = ["Leo Tolstoy","1"]
cursor.execute("update user set username = %s where id = %s",value)
db.close()