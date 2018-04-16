
#Importing libraries to use with Anlisys_Yank

import yank.analyze as yk
import matplotlib as mt
from matplotlib import pyplot as plt
from matplotlib import pylab
from mpl_toolkits.mplot3d import Axes3D
import scipy.cluster.hierarchy
from scipy.spatial.distance import squareform
from __future__ import print_function
from numpy import dot, sqrt
from numpy.linalg import eigvalsh
import pandas as pnd
import mdtraj as md
import nglview as nv
import seaborn as sb
import numpy as np
import os as os

def version():
    print("version: 0.0")

def load_replica (traj_nc=None, nc_checkpoint_file=None, replica=0):
	print ('now loading ...')
    index=str(replica)
    traj= yk.extract_trajectory ('traj_nc',nc_checkpoint_file='nc_checkpoint_file', replica_index='replica', start_frame=0, end_frame=-1, keep_solvent=True)
    load_traj=md.load (traj)
    return
    
    if not traj_nc:
    	print('yo have to set a .nc file from yank')
    	return

    if not nc_checkpoint_file:
		print ('now loading ...')
    	index=str(replica)
    	traj= yk.extract_trajectory ('traj_nc',nc_checkpoint_file=None, replica_index='replica', start_frame=0, end_frame=-1, keep_solvent=True)
    	load_traj=md.load (traj)
    	return

    if not replica:
    	print ('replica no defined, loading replica 0')
    	return
