# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:26:10 2019

@author: Phiremouse
"""

# def newkey(x):
#     df=pd.DataFrame(x)
#     df = df.reset_index()
#     df['MyID']=df.index
#     df=df.set_index('MyID', inplace= True)
#     return df

import pandas as pd
import os
def ORI_Transform(S_File,O_File, Output):
    x= os.getcwd()
    DFs=pd.read_csv(S_File)
    DFo=pd.read_csv(O_File)

    # format columns to get census sample to match the format of ORI files fields
    DFs['STATENAME']=DFs['State'].str.upper()
    DFs['STATENAME']=DFs['STATENAME'].str.strip()
    DFs['COUNTYNAME']=DFs['County'].str.replace(' County','')
    DFs['COUNTYNAME']=DFs['COUNTYNAME'].str.upper()
    DFs['COUNTYNAME']=DFs['COUNTYNAME'].str.strip()

    #reduce the sample list to needed columns
    DFs_cleaned= pd.DataFrame(data=DFs, columns=['STATENAME','COUNTYNAME'])

    
    #reduce ORI file to needed columns
    DFo_Cleaned=pd.DataFrame(DFo,columns=['STATENAME','COUNTYNAME','ADDRESS_CITY','ORI9'])
    
    # merge the list
    DFm = DFs_cleaned.merge(DFo_Cleaned,left_on=['STATENAME','COUNTYNAME'], right_on=['STATENAME','COUNTYNAME'])
    DFm.to_csv(Output)
    
    #Cleaning up to reduce memory. just in case when i run this as a module
    DFs=''
    DFo=''
    DFs_cleaned=''
    DFo_Cleaned=''
    DFm=''
    
