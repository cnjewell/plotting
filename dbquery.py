import sqlite3
import datetime
import numpy as np
import matplotlib.pyplot as plt

db = sqlite3.connect("test.db")

# for row in db.execute("select timestamp, levels from records"):
    # np.datetime64(row[0])

mydtype = np.dtype([('f0', "datetime64[h]"),('f1','<i8')])

data = db.execute("select timestamp, levels from records")
npdata = np.asarray(data, dtype=mydtype)
plt.plot(data['f0'], data['f1'])
plt.show()

