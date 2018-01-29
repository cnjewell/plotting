import sqlite3
import datetime

db = sqlite3.connect("test.db")
# db = sqlite3.connect(":memory:")
db.execute("create table records(timestamp, levels)")

with open('testdata.csv', 'r', buffering=1) as infile:
    for line_buffer in infile:
        record = line_buffer.split(sep=',')
        record[1] = record[1].strip()
        db.execute("insert into records(timestamp, levels) values (?, ?)", record)

for row in db.execute("select timestamp, levels from records"):
    print(row)

db.commit()
db.close()

