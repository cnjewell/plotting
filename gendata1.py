import numpy as np

date_range = np.arange("2017-12", "2018-02", dtype="datetime64[h]")

with open("testdata.csv", "a+") as f:
    for a_date in date_range:
        rand_level = np.random.randint(1,10)+40
        f.write(str(a_date) + ", " + str(rand_level)+"\n")
    
