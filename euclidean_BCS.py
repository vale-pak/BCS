# euclidean distance
import os
# os for interaction with the system
import sys
# sys to script arguments (argv) this is for you to be able to run in your terminal
import numpy as np
# numpy to do basic maths renamed np
import pandas as pd
# Panda to manipulate csv matrices

#read the BCS coordinates file.csv
mycsvfile = "/YOUR_DIRECTORY/00_BCS_3D.csv"
data_csv = pd.read_csv(mycsvfile, header=None, sep=' ')
data_csv_arr = np.array(data_csv)
data_csv_arr.shape

#create output file
output = "euclidean_distances.csv"

#compute the euclidean distances between each and other maps in the BCS
dist = np.zeros((len(data_csv), len(data_csv)))
for i in range(len(data_csv)):
    for j in range(len(data_csv)):
        if j < i:
            x1 = data_csv_arr[i, 0]
            x2 = data_csv_arr[j, 0]
            y1 = data_csv_arr[i, 1]
            y2 = data_csv_arr[j, 1]
            z1 = data_csv_arr[i, 2]
            z2 = data_csv_arr[j, 2]
            d = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
            dist[i, j] = d
np.savetxt(output, dist)
