# euclidean distance
import os
# os for interaction with the system
import sys
# sys to script arguments (argv) this is for you to be able to run in your terminal
import numpy as np
# numpy to do basic maths renamed np
import pandas as pd
# Panda to manipulate csv matrices

mycsvfile = "/Users/valentinapacella/Dropbox (GIN)/MSCA/4valentina/Fabric/001_Original_funMAPS/UMAPped/00_2017coordinates_parcelled_eucli.csv"

data_csv = pd.read_csv(mycsvfile, header=None, sep=';')

#transform data as array
data_csv_arr = np.array(data_csv)
#renamed
coords = np.array(data_csv)

# select the n items
grid_coords = coords[-0:]

#dist = []
for i, (x1, y1) in enumerate(grid_coords):
    d = []
    #name_i = 'coord_' + str(i) + '.txt'
    name_i = f'coord_{i+1}.txt'
    print(i)
    for e, (x2, y2) in enumerate(grid_coords):
        if e != i:
            d.append(np.sqrt((x1-x2)**2 + (y1-y2)**2))
    np.savetxt(name_i, d)
