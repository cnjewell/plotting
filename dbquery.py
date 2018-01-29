import sqlite3
import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')
time_format = "%Y-%m-%dT%H"

db = sqlite3.connect("test.db")


timestamps = []
levels = []
# my_query = db.execute("select timestamp, levels from records")
my_query = db.execute("select timestamp, levels from records where year=2018 and month=1 and day between 1 and 5")

for record in my_query:
    timestamps.append(datetime.datetime.strptime(record[0], time_format))
    levels.append(record[1])

timestamps = np.asarray(timestamps)
levels = np.asarray(levels)

fig, ax = plt.subplots()
ax.plot(timestamps, levels)

ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

# datemin = datetime.date(timestamps.min().year, 1, 1)
# datemax = datetime.date(timestamps.max().year + 1, 1, 1)
# ax.set_xlim(datemin, datemax)

fig.autofmt_xdate()

plt.show()

# plt.plot(timestamps, levels)