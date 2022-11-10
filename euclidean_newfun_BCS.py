#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:02:10 2022

@author: valentinapacella
"""

import numpy as np
import os
import pandas as pd

# The csv does not contain header. The first 506 raws are the BCS maps' coordinates. The last ones are your new map coordinates.
mycsvfile = "YOURPATHNAME/NEWFUNCTIONSCOORDINATES.csv"

data_csv = pd.read_csv(mycsvfile, header=None, sep=',')
coords = np.array(data_csv)

#select the last n (according to the number of new map, e.g. 2 maps) items
grid_coords = coords[-2:]
original_coords = coords[:-2]
#dist = []
for i, (x1, y1) in enumerate(grid_coords):
    d = []
    #name_i = 'coord_' + str(i) + '.txt'
    name_i = f'coord_{i+1}.txt'
    print(i)
    for x2, y2 in original_coords:
        d.append(np.sqrt((x1-x2)**2 + (y1-y2)**2))
    #dist.append(d)
    np.savetxt(name_i, d)

data_csv.shape
