# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:30:24 2019

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib2 import Path


Base_Dir=Path(__file__).resolve().parent
inputfile = Base_Dir.joinpath('output\Crime2Census.csv')
df=pd.read_csv(inputfile)

# plt1=plt.scatter(x=df['Median Age'],y=df['Total Violent Crime'],c='red', marker='v')
# plt1=plt.scatter(x=df['Median Age'],y=df['Total Non-Violent Crime'],c='blue', marker='o',alpha=.5)
# plt1=plt.ylim(0,15000)

plt2=plt.scatter(x=df['Population'],y=df['Total Violent Crime']/df['Population'],c='red',alpha=.7,edgecolors='black',s=df['Total Workforce'])

plt2=plt.scatter(x=df['Population'],y=df['Total Non-Violent Crime']/df['Population'],c='blue',alpha=.4,edgecolors='black',s=df['Total Workforce'])
# plt2=plt.scatter(x=df['Median Age'],y=df['Total Non-Violent Crime'],c='blue',s=df['Population']/10000)
# plt2=plt.ylim(0,15000)
plt.autofit()

