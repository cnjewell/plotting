import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
#data = np.random.randn(2,100)
start_date = "2017-12"
levels = np.random.randint(1, 10, size=212)+40
dates = np.arange(start_date, np.datetime64(start_date)+7, dtype="datetime64[D]")




#fig, axs = plt.subplots(2, 2, figsize=(5,5))
#axs[0, 0].hist(data[0])
#axs[1, 0].scatter(data[0], data[1])
#axs[0, 1].plot(data[0], data[1])
#axs[1, 1].hist2d(data[0], data[1])
plt.plot(dates, levels)
plt.show()
