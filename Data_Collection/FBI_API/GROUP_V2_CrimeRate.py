# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:03:45 2019
Updating the group crime API Code
@author: PHIREMOUSE
"""
import requests
import pandas as pd
import time

def SumCrime( inputfile, year):

    row_count=0
    load_count=0
    since=year
    until=year
    cityfile = pd.read_csv(inputfile)

    #police-employment-controller : Endpoints pertaining to UCR Police Employment data
    #/api/police-employment/agencies/{ori}/{since}/{until} Agency level UCR Police Employment Endpoint
    #base_url_e = f'https://api.usa.gov/crime/fbi/sapi/api/police-employment/agencies/{ori}/{since}/{until}'
    
    #summarized-data-controller : Endpoints pertaining to Agency SRS Level Crime Data
    #/api/summarized/agencies/{ori}/offenses/{since}/{until} Agency level SRS Crime Data Endpoint
    #base_url_c=f'https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{ori}/offenses/{since}/{until}'
    
    p={
        'api_key':'fByj7VuEfeNrsAI7MxVeiltb3Y0kULdT0XzfTbDf'
        }
    
    df = pd.DataFrame(cityfile,columns=['STATENAME','COUNTYNAME','ADDRESS_CITY','ORI9'])
    
    for index, row in df.iterrows():
        ori = row['ORI9']
        base_url_e = f'https://api.usa.gov/crime/fbi/sapi/api/summarized/agencies/{ori}/offenses/{since}/{until}'

        try:
            j = requests.get(base_url_e, p).json()
            print(f'Processing CrimeRate Record {row_count} in load count of {load_count} | State: {row.STATENAME} , County: {row.COUNTYNAME}, CITY {row.ADDRESS_CITY}, ORI: {row.ORI9} ')

            #print(requests.get(base_url_e, p).url)
            if row_count==1:
                ded= pd.DataFrame(pd.DataFrame(j['results']))
            else:
                ded=ded.append(pd.DataFrame(j['results']), ignore_index=True)
        except:
            print(f"Error with city data. Skipping {row.ADDRESS_CITY} - {row.ORI9}......")
            df.drop(labels=index, inplace=True)
        
        time.sleep(1) #60 seconds / limit request of 60
        row_count+=1
      

    CR_Join = df.merge(ded, left_on = 'ORI9', right_on = 'ori')
    CR_agg = CR_Join.groupby(['STATENAME','COUNTYNAME','ADDRESS_CITY']).aggregate({'actual':'sum','cleared':'sum'})
    CR_agg.to_csv('output/CR_Agg.csv')
    CR_Join.to_csv('output/cr_breakdown.csv')
    CR_Join=''
    CR_agg=''
    cityfile=''
    ded=''
    df=''
    j=''
    ori=''



