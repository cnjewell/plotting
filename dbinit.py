import sqlite3
import datetime

db = sqlite3.connect("test.db")
# db = sqlite3.connect(":memory:")
db.execute("create table records(timestamp, year, month, day, hour, levels)")

with open('testdata.csv', 'r', buffering=1) as infile:
    for line_buffer in infile:
        record = line_buffer.split(sep=',')
        time_format = "%Y-%m-%dT%H"
        d_obj = datetime.datetime.strptime(record[0], time_format)
        record[1] = record[1].strip()
        new_record = [record[0], d_obj.year, d_obj.month, d_obj.day, d_obj.hour, record[1]]
        db.execute("insert into records(timestamp, year, month, day, hour, levels) values (?, ?, ?, ?, ?, ?)", new_record)
        db.commit()

# for row in db.execute("select timestamp, levels from records"):
#     # print(type(row[0]))
#     print(row[0])

db.close()

