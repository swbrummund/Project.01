# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:11:35 2019
Main Run

@author: Phiremouse
"""

# Module Section
import os
from pathlib2 import Path
from ORI_Translate import ORI_Transform
from GROUP_V2_CrimeRate import SumCrime
from GROUP_V2_Employment import Agg_Employment
from GROUP_V2_cleaner import clean_cr_e
from VvsNV import CleanStepFinal
from Crime2Census import c2c

# Declared Vairbles
sampleFile = os.path.join('..','Census_API','sample.csv')
oriFile = os.path.join('.','Resources','ORI_Dataset.csv')
Base_Dir=Path(__file__).resolve().parent
FBISampleFile=Base_Dir.joinpath('output\FBI_Sample_List.csv')
C_File =Base_Dir.joinpath('output\FullCrimeStatsFinal.csv')
CrimeFile = os.path.join('.','output','cr_breakdown.csv')
EmploymentFile = os.path.join('.','output','E_Breakdown.csv')


# Pulls in census sample, reduces it to needed columns, creates bridge file b/w census & crime data.
ORI_Transform(sampleFile,oriFile,FBISampleFile)

# based on the bridge file requests are made to pull in crime and cleared stats for a given agency
SumCrime(FBISampleFile,2016)

# based on the bridge file requests are made to pull in employment information for a given agency
Agg_Employment(FBISampleFile,2016)

# groups agency employment and crime states data and merge them. Renames columns and creates calculated columns.
clean_cr_e(CrimeFile,EmploymentFile,'County')

# creates total columns on the crime and cleared columns based on nonviolent and violent offenses
CleanStepFinal()

# merges the FBI API data to the census sample.
c2c(sampleFile,C_File)
