#!/usr/bin/env python
# coding: utf-8

# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
# 15,Samantha Lara,1993-09-08,848-80-7526,Colorado
# 411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania
# 

# In[6]:


import os
import csv
from datetime import datetime


# In[7]:


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# In[8]:


def changeDOB(DOB):
    DOB = datetime.strptime(DOB, '%Y-%m-%d')
    DOB = DOB.strftime('%m/%d/%Y')
    return DOB


# In[9]:


def maskSSN(SSN):
    SSN = "***-**-" + SSN[-4:]
    return SSN


# In[10]:


def abbreState(State):
    for stateName, abbre in us_state_abbrev.items():
        if State == stateName:
            State = abbre
        else:
            State = 'NA'
        return State


# In[11]:


file_name = 'employee_data.csv'
output_file_name = "employee_data_modified.csv"

with open(file_name, 'r') as csvfile, open(output_file_name, 'w') as outfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvwriter = csv.writer(outfile, delimiter = ',', lineterminator='\n')
    
    # skip the first row
    csvheader = next(csvreader)
    
    data = list(csvreader)

    for row in data:
        Name = row[1]
        firstName = Name.strip().split(' ')[0]
        lastName = Name.strip().split(' ')[1]
        row.append(firstName)
        row.append(lastName)
        
        # notice two different functions from datetime library
        # strptime() and strftime()
        DOB = changeDOB(row[2])
        row.append(DOB)
        
        SSN = maskSSN(row[3])
        row.append(SSN)
        
        State = abbreState(row[4])
        row.append(State)
        
        # remove rows that are no longer needed
        for i in range(4):
            del row[1]

    csvwriter.writerow(['Emp ID','First Name', 'Last Name','DoB', 'SSN', 'ST'])
    for row in data:
        csvwriter.writerow(row)

        
        
        


# In[12]:


data


# In[ ]:




