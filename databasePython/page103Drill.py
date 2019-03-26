#
#   Python:     3.6.6
#
#   Author:     Jordan Richter
#
#   Purpose:    Drill Description:
#               For this drill, you will need to write a script that creates
#               a database and adds new data into that database.


import sqlite3

conn = sqlite3.connect('files.db')


with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fileName TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("information.docx",))
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("Hello.txt",))
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("myImage.png",))
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("myMovie.mpg",))
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("World.txt",))
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("data.pdf",))
    cur.execute("INSERT INTO tbl_files(col_fileName) \
        VALUES (?)", ("myPhoto.jpg",))
    conn.commit()
conn.close()


conn = sqlite3.connect('files.db')

with conn:
    cur = conn.cursor()
    for items in cur.execute("SELECT col_fileName FROM tbl_files WHERE col_fileName LIKE '%txt'"):
        print(items)

