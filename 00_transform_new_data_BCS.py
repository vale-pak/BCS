#libraries we will be working with
import os
import sys
import nibabel as nib
import pandas as pd
from pandas import DataFrame
import numpy as np
import umap
import pickle

#reopen the space
loaded_reducer = pickle.load((open('/Users/valentinapacella/Dropbox (GIN)/MSCA/4valentina/002_New_funMAPS/UMAPped_newfun/00_2017space_parcelledpickle.sav', 'rb')))

mycsvfile = "MY_PATH/csv_parcelled_and_thresholded_data.csv"
data_csv = pd.read_csv(mycsvfile, header=None,sep=',')
df = np.matrix(data_csv) #.T to transpose


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
