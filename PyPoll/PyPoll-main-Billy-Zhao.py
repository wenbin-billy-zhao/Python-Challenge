# import moduels
import os
import csv

# create file path
fname="Resources/election_data.csv"
outputfile = "election_result.txt"

# these are the important variables for the election result
voteList = []
# the following lists are 1- unique candidates, 2- percentage of their votes, 3- total count of their votes
candidates = []
pctCandidate = []
countCandidate = []

totalVote = 0

with open(fname, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        voteList.append(row[2])
        
totalVote = len(voteList)

# find all the candidates and assign their indexes
for name in voteList:
   if name not in candidates:
        candidates.append(name)
        x = name

# counter for the total votes for each candidates
count = 0
# set the first candidate on the voteList for the loop
candidate = voteList[0]
#
lastCount = 0
# Print out top part of the Election Results
print("Election Results")
print("-"*50)
print(f"Total Votes: {totalVote}")
print("-"*50)

for candidate in candidates:
    for vote in voteList:
        if candidate == vote:
            count += 1
    percent = count / len(voteList)
    pctCandidate.append(percent)
    countCandidate.append(count)
    
    if lastCount < count:
        Winner = candidate    
    print(f"{candidate}: {percent:.3%} ({count})")
    
    # reset vote count to zero
    lastCount = count
    count = 0

# print out the winner
print("-"*50)
print(f"Winner: {Winner}")
print("-"*50)

# Output result to txt file
with open(outputfile, 'w') as output:
    output.write("Election Results\n")
    output.write("-"*50+"\n")
    output.write(f"Total Votes: {totalVote}\n")
    output.write("-"*50+"\n")
    for candidate in candidates:
        index = candidates.index(candidate)
        output.write(f"{candidate}: {pctCandidate[index]:.3%} ({countCandidate[index]})\n")
    output.write("-"*50+"\n")
    output.write(f"Winner: {Winner}\n")



