import sqlite3

conn=sqlite3.connect('orgdbdb.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('CREATE TABLE counts(org TEXT,count INTEGER)')
fname=input("enter the text file?")
fopen=open(fname,'r',encoding='utf-8-sig')
for line in fopen:
    if  not line.startswith('From'):continue
    domain=line.split("@")[1]
    cur.execute('SELECT count FROM counts WHERE org=?',(domain,))
    db_response=cur.fetchone()
    if db_response is None:
        cur.execute('INSERT INTO counts (org,count) VALUES (?,1)',(domain,))
    else:
        cur.execute('UPDATE counts SET count=count+1 WHERE org=?',(domain,))
    conn.commit()
# sqlstr='SELECT email,count FROM counts ORDER BY count DESC LIMIT 10'
# print("here is the most frequent emails our ogr interact:\n")
# for dbresponse in cur.execute(sqlstr):
#     print(str(dbresponse[0]),dbresponse[1])
# cur.close()