import MySQLdb
db = MySQLdb.connect(user='root', db='test', passwd='19890823', host='localhost')
cursor = db.cursor()
value = ["inserted","cswandzxm"]
cursor.execute("insert into user(username,love) values(%s,%s)",value)
db.close()