#Python Drill Page 103
#Author: David A Simar

import sqlite3

fList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
tList = [file for file in fList if file.endswith('.txt')]


#Create the db
conn = sqlite3.connect('test1.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()
conn.close()

#Fill the db
conn = sqlite3.connect('test1.db')

with conn:
    cur = conn.cursor()
    cur.execute\
    ("INSERT INTO tbl_persons(col_fName) VALUES (?)",\
     (tList[0],))
    
    cur.execute\
    ("INSERT INTO tbl_persons(col_fName) VALUES (?)",\
     (tList[1],))
    conn.commit()
conn.close()

#Making it nice to the user
conn = sqlite3.connect('test1.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT ID, col_fName FROM tbl_persons WHERE col_fName = 'txt'")
    varPerson = cur.fetchall()
    for item in varPerson:
        tList = "File Names: {},".format(item[0],item[1])
print(tList)
                

    

