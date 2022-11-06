from scipy.stats import norm
from scipy.stats import t
import nibabel as nib
import numpy as np


inTfile = "YOUR_PATHNAME/YOUR_NIFTI.nii.gz"
outZfile = "YOUR_PATHNAME/YOUR_NIFTI_OUTPUT.nii.gz"
dof = #n degrees of freedom of the study
sided = 2  # 1 for one-sided, 2 for two-sided t-test

tmap_im = nib.load(inTfile)
in_dtype = tmap_im.get_data_dtype()
tmap = tmap_im.get_fdata(dtype=in_dtype)

pmap = t.sf(np.abs(tmap), df=dof) * sided
zmap = np.nan_to_num(-norm.ppf(pmap)) * np.sign(tmap)

zmap_I = nib.Nifti1Image(zmap.astype(in_dtype), tmap_im.affine)
nib.save(zmap_I, outZfile)
