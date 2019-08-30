# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:44:59 2019

@author: PHIREMOUSE
"""


import pandas as pd
import numpy as np

def clean_cr_e(cr_file,e_file,level):
    cr_df = pd.read_csv(cr_file)
    e_df = pd.read_csv(e_file)

    if level=='County':
        cr_df=cr_df.groupby(['STATENAME','COUNTYNAME','offense']).aggregate({'actual':'sum','cleared':'sum'}).reset_index()
        e_df=e_df.groupby(['STATENAME','COUNTYNAME']).aggregate({'female_civilian_ct':'sum','female_officer_ct':'sum','male_civilian_ct':'sum','male_officer_ct':'sum'}).reset_index()

        cr_df= cr_df.rename(columns={
                 'STATENAME':'State',
                 'COUNTYNAME':'County',
                 'offense':'Offense',
                 'actual':'Total Crime Count',
                 'cleared':'Crime Cleared Count'
                 })

        e_df= e_df.rename(columns={
                 'STATENAME':'State',
                 'COUNTYNAME':'County',
                 'female_civilian_ct':'Female Civilians',
                 'female_officer_ct':'Female Officers',
                 'male_civilian_ct':'Male Civilians',
                 'male_officer_ct':'Male Officers'
                 })

        #shift crime rate data to join with the data better
        table = pd.pivot_table(cr_df,values=['Total Crime Count','Crime Cleared Count'], index=['State','County'],columns=['Offense'],aggfunc={'Total Crime Count':np.sum,'Crime Cleared Count':np.sum},fill_value=0)
        table.reset_index(inplace=True)
        table.columns = [' '.join(col).strip() for col in table.columns.values]
        table2 = e_df.merge(table, left_on=['State','County'], right_on=['State','County'])
        table2['Total Cleared']= table2['Crime Cleared Count aggravated-assault'] + table2['Crime Cleared Count arson'] + table2['Crime Cleared Count burglary'] + table2['Crime Cleared Count homicide'] + table2['Crime Cleared Count larceny'] + table2['Crime Cleared Count motor-vehicle-theft'] + table2['Crime Cleared Count property-crime'] + table2['Crime Cleared Count rape'] + table2['Crime Cleared Count rape-legacy'] + table2['Crime Cleared Count robbery'] + table2['Crime Cleared Count violent-crime']
        table2['Total Crime']= table2['Total Crime Count aggravated-assault'] + table2['Total Crime Count arson'] + table2['Total Crime Count burglary'] + table2['Total Crime Count homicide'] + table2['Total Crime Count larceny'] + table2['Total Crime Count motor-vehicle-theft'] + table2['Total Crime Count property-crime'] + table2['Total Crime Count rape'] + table2['Total Crime Count rape-legacy'] + table2['Total Crime Count robbery'] + table2['Total Crime Count violent-crime']
        table2['Total Clear Rate']=table2['Total Cleared']/table2['Total Crime']
        table2['Total Female Workforce']=table2['Female Civilians']+table2['Female Officers']
        table2['Total Male Workforce']=table2['Male Civilians']+table2['Male Officers']
        table2['Total Workforce']=table2['Total Male Workforce']+table2['Total Female Workforce']
        table2['Total Officers']=table2['Female Officers']+table2['Male Officers']
        table2.to_csv('output/FullCrimeStats.csv')


    elif level=='city':
        print('dont use this option!!!!!!')
        # cr_df=cr_df.groupby(['STATENAME','COUNTYNAME','ADDRESS_CITY','offense']).aggregate({'actual':'sum','cleared':'sum'})
        # e_df=e_df.groupby(['STATENAME','COUNTYNAME','ADDRESS_CITY']).aggregate({'female_civilian_ct':'sum','female_officer_ct':'sum','male_civilian_ct':'sum','female_civilian_ct':'sum'})
        # cr_df.to_csv('output/CITY_crdf.csv')
        # e_df.to_csv('output/CITY_edf.csv')
