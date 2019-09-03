# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:38:16 2019

@author: Phiremouse
"""


import pandas as pd
from pathlib2 import Path

def CleanStepFinal():

    Base_Dir=Path(__file__).resolve().parent
    myfile=Base_Dir.joinpath('output\FullCrimeStats.csv')
    mychecker =Base_Dir.joinpath('Resources\CrimeListing.csv')
    df= pd.read_csv(myfile)
    df2 = pd.read_csv(mychecker)
    df2.insert(1,column='tmp',value='Crime Cleared Count ' + df2['Crime'])
    df2.insert(2,column='tmp2',value='Total Crime Count ' + df2['Crime'])
    
    
    df2v=df2[df2['Type']=='Violent']
    df2n=df2[df2['Type']=='Non-Violent']
    
    Cleared = df.filter(regex='Cleared ')
    Crime = df.filter(regex='Crime Count ')
    
    Cleared['Total Violent Cleared']=Cleared[df2v['tmp']].sum(axis =1 )
    Cleared['Total Non-Violent Cleared']=Cleared[df2n['tmp']].sum(axis =1 )
    
    Crime['Total Violent Crime']=Crime[df2v['tmp2']].sum(axis =1 )
    Crime['Total Non-Violent Crime']=Crime[df2n['tmp2']].sum(axis =1 )
    
    Cleared=Cleared.filter(['Total Violent Cleared','Total Non-Violent Cleared'])
    Crime=Crime.filter(['Total Violent Crime','Total Non-Violent Crime'])
    Merge1 = pd.concat([Cleared, Crime],join='inner', axis=1, sort=False)
    
    Result=pd.concat([df,Merge1],axis=1,join='inner', sort=False)
    outputfile = Base_Dir.joinpath('output/FullCrimeStatsFinal.csv')

    Result.to_csv(outputfile)