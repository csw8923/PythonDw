import MySQLdb
db = MySQLdb.connect(user='root', db='test', passwd='19890823', host='localhost')
cursor = db.cursor()
cursor.execute('SELECT username FROM user ORDER BY id')
value = [1,"inserted"]
cursor.execute("insert into user values(%s,%s)",value)
names = [row[0] for row in cursor.fetchall()]
#print names
#print len(names)
#for name in names:
#    print name
#else:
#    print 'this is over'
db.close()