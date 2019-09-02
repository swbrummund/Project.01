# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:34:46 2019

@author: PHIREMOUSE
"""

import pandas as pd
# import os


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
    
    # Super Amazing fun time of creating MORE columns
    Mdf['Overal Crime Rate']=Mdf['Total Crime']/Mdf['Population']
    Mdf['Overal Clear Rate']=Mdf['Total Cleared']/Mdf['Population']
    Mdf['Workforce 2 Pop']=Mdf['Total Workforce']/Mdf['Population']
    Mdf['Leo 2 Pop']=Mdf['Total Officers']/Mdf['Population']
    
    
    

    Mdf.to_csv('Output/Crime2Census.csv')