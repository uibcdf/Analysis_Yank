
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
        topology=traj.topology.residues
        print (traj)
        print (topology)
        return
    
    if not traj_nc:
    	print('yo have to set a .nc file from yank')
    	return

    if not replica:
    	print ('replica no defined, loading replica 0')
    	return

def residues ():
    print ('List of residues in this experiment:',[residue for residue in traj.topology.residues])
    return

def atoms ():
    print ('list of atoms in this experiment:', [atoms for residue in traj.topology.residues])
    return

def index (resid=0):
    index = str(resid)
    selection=traj.topology.select ('('resid', index)')
    return

def def_cluster (resid=0):
    index=str(resid)
    selection=md.load (load, atom_indices=[index])
    distances = np.empty ((selection.n_frames, selection.n_frames))
        for i in range(selection.n_frames):
            distances[i] = md.rmsd(selection,selection, i)
            print('Max pairwise rmsd: %f nm' % np.max(distances))
    reduced_distances = squareform(distances, checks=False)
    linkage = scipy.cluster.hierarchy.linkage(reduced_distances, method='average')
    return













