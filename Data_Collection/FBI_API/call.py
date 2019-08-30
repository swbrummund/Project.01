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
from GROUP_V2_cleaner import clean_cr_e

sampleFile = os.path.join('..','Census_API','sample.csv')
oriFile = os.path.join('.','Resources','ORI_Dataset.csv')
FBISampleFile = os.path.join('Output','FBI_Sample_List.csv')

# logic to desconstruct and transform sample from Census to line up to the FBI API
# ORI_Transform(sampleFile,oriFile,FBISampleFile)

# # 'Logic to create the crime rate csv'
# SumCrime(FBISampleFile,2016)

# # 'Logic to create the  Police Agency Employement (PAE) csv'
# Agg_Employment(FBISampleFile,2016)

# CLEAN UP CRIME RATE AND EMPLOYMNENT FILES
CrimeFile = os.path.join('.','output','cr_breakdown.csv')
EmploymentFile = os.path.join('.','output','E_Breakdown.csv')
clean_cr_e(CrimeFile,EmploymentFile,'County')


# 'Bring it back to the central dataframe from census api'