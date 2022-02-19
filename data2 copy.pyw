import sqlite3

conn = sqlite3.connect('overtimeTEST.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS overtime")

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
