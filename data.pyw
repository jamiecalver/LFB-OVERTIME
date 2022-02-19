import sqlite3

conn = sqlite3.connect('overtimeTEST.db')
cursor = conn.cursor()
#cursor.execute("DROP TABLE IF EXISTS overtime")
#only uncomment line 5 if starting with a fresh .db file with no tables in

sql = """ CREATE TABLE overtime (
    id integer PRIMARY KEY,
    paynum text,
    rank text,
    actup text,
    name text,
    station text,
    skills text,
    watch text,
    pref text,
    number text,
    hours int,
    lastper int,
    nightOne text,
    dayTwo text,
    nightTwo text,
    dayThree text,
    nightThree text,
    dayFour text
    ); """

cursor.execute(sql)
conn.commit()
conn.close()
