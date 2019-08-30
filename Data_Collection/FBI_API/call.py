# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:11:35 2019
Main Run
@author: Phiremouse
"""
import os
from ORI_Translate import ORI_Transform
from GROUP_V2_CrimeRate import SumCrime
from GROUP_V2_Employment import Agg_Employment
from GROUP_V2_Joindata import combine_CR_E

sampleFile = os.path.join('..','Census_API','sample.csv')
oriFile = os.path.join('.','Resources','ORI_Dataset.csv')
FBISampleFile = os.path.join('Output','FBI_Sample_List.csv')
CrimeFile = os.path.join()
EmploymentFile = os.path.join()

# logic to desconstruct and transform sample from Census to line up to the FBI API
ORI_Transform(sampleFile,oriFile,FBISampleFile)

# 'Logic to create the crime rate csv'
SumCrime(FBISampleFile,2016)

# 'Logic to create the  Police Agency Employement (PAE) csv'
Agg_Employment(FBISampleFile,2016)

# 'logic to join the PAE and Crime Rate data'
combine_CR_E()
combine_CR_E


# 'Bring it back to the central dataframe from census api'