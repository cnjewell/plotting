import numpy as np
import matplotlib.pyplot as plt

mydtype = np.dtype([('f0', "datetime64[h]"),('f1','<i8')])
data = np.genfromtxt("testdata.csv", delimiter=',', dtype=mydtype)

plt.plot(data['f0'], data['f1'])

plt.show()
