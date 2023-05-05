#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:02:10 2022

@author: valentinapacella
"""

import numpy as np
import os
import pandas as pd

#merging the BCS coordinates and the new maps coordinates. The first 506 raws are the BCS maps' coordinates. The last ones are your new map coordinates.
mycsvfile1 = "/YOURPATHNAME/BCS_3D.csv"
data_csv1 = pd.read_csv(mycsvfile1, header=None, sep=',')
mycsvfile2 = "YOURPATHNAME/NEW_MAPS_COORDINATES.csv"
data_csv2 = pd.read_csv(mycsvfile2, header=None, sep=' ')
data_csv = pd.concat([data_csv1,data_csv2], ignore_index=True)
coords = np.array(data_csv)

#select the last n (according to the number of new map, e.g. 2 maps) items
grid_coords = coords[-(len(data_csv2)):]
#select the first n items (506 BCS maps)
original_coords = coords[:-(len(data_csv2))]

#compute euclidean distances and save txt file for each new map
for i, (x1, y1, z1) in enumerate(grid_coords):
    d = []
    #name_i = 'coord_' + str(i) + '.txt'
    name_i = f'coord_{i+1}.txt'
    #print(i)
    for x2, y2, z2 in original_coords:
        d.append(np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2))
    #dist.append(d)
    np.savetxt(name_i, d)

