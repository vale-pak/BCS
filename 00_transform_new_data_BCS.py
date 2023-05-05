import os
import sys
import nibabel as nib
import pandas as pd
from pandas import DataFrame
import numpy as np
import umap
import pickle

#reopen the space
loaded_reducer = pickle.load((open('/BCS_3D.sav DIRECTORY/00_BCS_3D.sav', 'rb')))

#read the csv of the new maps parcellation matrix
mycsvfile = "/CSV_DIRECTORY/PARCELLED_MAPS.csv"
data_csv = pd.read_csv(mycsvfile, header = None, sep=',')
df = np.matrix(data_csv).T #to transpose
df.shape
data_csv_arr = np.array(data_csv)

#coordinates output file
output = "coordinates_new.csv"

#projection of each new map in the BCS
dist = np.zeros(((len(data_csv)),3))
for col in range(df.shape[1]):
    d =loaded_reducer.transform((df[:, col]).T)
    dist[col] = d
np.savetxt(output, dist)

