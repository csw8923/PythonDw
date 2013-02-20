import MySQLdb
db = MySQLdb.connect(user='root', db='test', passwd='19890823', host='localhost')
cursor = db.cursor()
value = "25"
cursor.execute("delete from user where id = %s",value)
db.close()