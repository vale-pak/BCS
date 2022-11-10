# BCS
#  
# Here you will find the datasets and the code used in the validation of the BCS as predictive framework.
# IMPORTANT: Note that python v 3.8, umap.learn v 0.5.1, numba v 0.53.1, and pickle v 0.7.5 are needed to open the BCS and project your data onto it.
#
# If you want to import new fMRI data onto the BCS to see where it colocalises, transform your data in z maps, the code is provided in ttoz_BCS.py. 
# Before running the parcellation onto your z-map, don't forget to threshold it at z 3.4. An easy way to do it is via fslmaths (https://open.win.ox.ac.uk/pages/fslcourse/practicals/intro3/index.html) 
# Now you are ready to reduce the dimensionality of your data and project it onto the BCS via the transform_new_data_BCS.py code.
