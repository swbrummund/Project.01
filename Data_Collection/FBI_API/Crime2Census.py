# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:34:46 2019

@author: PHIREMOUSE
"""

import pandas as pd



def c2c(S_File,C_File):
    #census table
    # S_File =os.path.join('..','Census_API','sample.csv')
    #fbi table
    # C_File =os.path.join('Output','FullCrimeStats.csv')
    Sdf= pd.read_csv(S_File)
    Cdf = pd.read_csv(C_File)
    Sdf['State']=Sdf['State'].str.strip()
    Sdf['County']=Sdf['County'].str.strip()
    Sdf['County']=Sdf['County'].str.replace(' County','')
    Sdf['State']=Sdf['State'].str.upper()
    Sdf['County']=Sdf['County'].str.upper()
    Mdf=Sdf.merge(Cdf, left_on = ['State','County'], right_on = ['State','County'])

    Mdf.to_csv('Output/Crime2Census.csv')