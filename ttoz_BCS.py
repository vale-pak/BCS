import os
import sys
from scipy.stats import norm
from scipy.stats import t
import nibabel as nib
import numpy as np

#set the input image and the output image names on the terminal
inTfile = sys.argv[1]
outZfile = sys.argv[2]
#degrees of freedom of the map to be transformed
dof = n
sided = 2  # 1 for one-sided, 2 for two-sided t-test

#compute zmaps
tmap_im = nib.load(inTfile)
in_dtype = tmap_im.get_data_dtype()
tmap = tmap_im.get_fdata(dtype=in_dtype)

pmap = t.sf(np.abs(tmap), df=dof) * sided
zmap = np.nan_to_num(-norm.ppf(pmap)) * np.sign(tmap)

zmap_I = nib.Nifti1Image(zmap.astype(in_dtype), tmap_im.affine)
nib.save(zmap_I, outZfile)
