#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import Python Modules 
import os
import csv


# In[3]:


# set file path
fname = 'Resources/budget_data.csv'

# set variables
MonthCount = 0
Total = 0
PL = []
monthList = []
monthlyChanges = []


# In[5]:


# read input csv file
with open(fname, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip first row which contains headers
    csvheader = next(csvreader)
    
    for row in csvreader:
        MonthCount += 1
        Total += int(row[1])
        PL.append(row[1])
        monthList.append(row[0])


# In[6]:


# first month P&L value
firstPL = int(PL[0])

# this loop creates a list of monthly changes
for i in range(1, len(PL)):
    monthlyChanges.append(int(PL[i]) - firstPL)
    firstPL = int(PL[i])
    i += 1

# find max increase and min increase
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)


# In[8]:


# find month index for the Max Increase and Max Decrease
for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i - 1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i - 1)
    else:
        i += 1
        
MaxMonth = monthList[maxIndex]
MinMonth = monthList[minIndex]


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In[9]:


print("Financial Analysis")
print("-"*50)
print(f"Total Months: {MonthCount}")
print(f"Total: ${Total}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")


# In[13]:


# write financial analysis summary to txt file
outputfile = 'summary.txt'

# use "\n" to create a new line
with  open(outputfile, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Months: {MonthCount}\n")
    output.write(f"Total: ${Total}\n")
    output.write(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
 


# In[ ]:




