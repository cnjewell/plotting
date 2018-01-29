import datetime


with open('testdata.csv', 'r', buffering=1) as infile:
    for line_buffer in infile:
        print(line_buffer)