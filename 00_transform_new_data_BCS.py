## !! Note that python v 3.8, umap.learn v 0.5.1, numba v 0.53.1, and pickle v 0.7.5 are needed !!

#libraries we will be working with
import os
import sys
import pandas as pd
from pandas import DataFrame
import numpy as np
import umap
import pickle

#reopen the space
loaded_reducer = pickle.load((open('/YOURPATHNAME/00_2017space_parcelledpickle.sav', 'rb')))

mycsvfile = "YOURPATHNAME/YOURPARCELLEDANDTHR_DATA.csv"
data_csv = pd.read_csv(mycsvfile, header=None,sep=',')
df = np.matrix(data_csv) #.T to transpose if needed


#X = datamatrix
X1 = (df [:,[0]])
X2 = (df [:,[1]])

#reduce and project
test_embedding1=loaded_reducer.transform(X1.T)
test_embedding2=loaded_reducer.transform(X2.T)

all_test=np.concatenate([test_embedding1,test_embedding2])
all=np.array(all_test)

#save the coordinates of the new data
np.savetxt("my_file.csv", all , delimiter=",")
