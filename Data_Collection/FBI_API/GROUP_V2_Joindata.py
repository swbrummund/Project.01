# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:44:59 2019

@author: PHIREMOUSE
"""


import pandas as pd


def combine_CR_E(cr_file,e_file,level):
    cr_df = pd.read_csv(cr_file)
    e_df = pd.read_csv(e_file)
    full_df = e_df.merge(cr_df, on =['STATENAME','COUNTYNAME','ADDRESS_CITY'])
    full_df=full_df.rename(columns={'STATENAME':'State','COUNTYNAME':'County','ADDRESS_CITY':'City','total_pe_ct':'Peace Officer Count','actual':'Total Crimes','cleared':'Crimes Cleared'})

    if level=='County':
        agg_df=full_df.groupby(['Statename',])
        full_df=full_df.rename(columns={'STATENAME':'State','COUNTYNAME':'County','ADDRESS_CITY':'City','total_pe_ct':'Peace Officer Count','actual':'Total Crimes','cleared':'Crimes Cleared'})
        
        full_df.to_csv('full_df.csv')
    elif level=='city':

        
        
        full_df = e_df.merge(cr_df, on =['STATENAME','COUNTYNAME','ADDRESS_CITY'])
        full_df=full_df.rename(columns={'STATENAME':'State','COUNTYNAME':'County','ADDRESS_CITY':'City','total_pe_ct':'Peace Officer Count','actual':'Total Crimes','cleared':'Crimes Cleared'})
        
        full_df.to_csv('full_df.csv')
    elif level == 'full':


    elif level=='type':