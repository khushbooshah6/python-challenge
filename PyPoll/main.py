import os
import csv
import statistics
from statistics import mean
filepath = os.path.join('.','Resources','election_data.csv')
voter=[]
country=[]
candidate=[]
candidatelist123=[]
with open (filepath, newline='') as fileopen:
    freader = csv.reader(fileopen, delimiter=',')
    next(freader)
    for row in freader :
        voter.append(row[0])
        candidate.append(row[2])
print("Total Voters: " + str(len(voter)))
outputpath = os.path.join('.','Output','ElectionData.txt')
def unique(candidate):
    #candidatelist123 = []
    for x in candidate:
        if x not in candidatelist123:
            candidatelist123.append(x)
    for x in candidatelist123:
        print(x)
unique(candidate)
candidatelist1230Count=0
candidatelist1231Count=0
candidatelist1232Count=0
candidatelist1233Count=0
for i in range(len(candidate)):
    if candidatelist123[0] == candidate[i]:
        candidatelist1230Count=candidatelist1230Count+1
    if candidatelist123[1] == candidate[i]:
        candidatelist1231Count=candidatelist1231Count+1
    if candidatelist123[2] == candidate[i]:
        candidatelist1232Count=candidatelist1232Count+1
    if candidatelist123[3] == candidate[i]:
        candidatelist1233Count=candidatelist1233Count+1
print(candidatelist123[0] + " : " + str(candidatelist1230Count))
print(candidatelist123[1] + " : " + str(candidatelist1231Count))
print(candidatelist123[2] + " : " + str(candidatelist1232Count))
print(candidatelist123[3] + " : " + str(candidatelist1233Count))
Percentage1 = (candidatelist1230Count/3521001)*100
Percentage2 = (candidatelist1231Count/3521001)*100
Percentage3 = (candidatelist1232Count/3521001)*100
Percentage4 = (candidatelist1233Count/3521001)*100
print("Election Results")
print("-------------------------------")
print("Total Votes:3521001")
print("-------------------------------")
print(candidatelist123[0]+ ": " + str(Percentage1) + "% " + "("+str(candidatelist1230Count)+")")
print(candidatelist123[1]+ ": " + str(Percentage2) + "% " + "("+str(candidatelist1231Count)+")")
print(candidatelist123[2]+ ": " + str(Percentage3) + "% " + "("+str(candidatelist1232Count)+")")
print(candidatelist123[3]+ ": " + str(Percentage4) + "% " + "("+str(candidatelist1233Count)+")")
if candidatelist1230Count>candidatelist1231Count and candidatelist1230Count>candidatelist1232Count and candidatelist1230Count>candidatelist1233Count:
    winner=candidatelist123[0]
elif candidatelist1231Count>candidatelist1230Count and candidatelist1231Count>candidatelist1232Count and candidatelist1231Count>candidatelist1233Count:
    winner=candidatelist123[1]
elif candidatelist1232Count>candidatelist1230Count and candidatelist1232Count>candidatelist1231Count and candidatelist1232Count>candidatelist1233Count:
    winner=candidatelist123[2]
else:
    winner=candidatelist123[3]
print("------------------")
print("The Election Winner is: ", winner)
print("------------------")
pypoll_output_path = os.path.join("..", "PyPoll", "pypoll_out.txt")
with open(pypoll_output_path,'w', newline='') as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write("Total Votes:3521001\n")
    file.write("------------------\n")
    file.write(candidatelist123[0]+ ": " + str(Percentage1) + "% " + "("+str(candidatelist1230Count)+")\n")
    file.write(candidatelist123[1]+ ": " + str(Percentage2) + "% " + "("+str(candidatelist1231Count)+")\n")
    file.write(candidatelist123[2]+ ": " + str(Percentage3) + "% " + "("+str(candidatelist1232Count)+")\n")
    file.write(candidatelist123[3]+ ": " + str(Percentage4) + "% " + "("+str(candidatelist1233Count)+")\n")
    file.write("------------------\n")
    file.write("The Election Winner is: "+ winner)
    file.write("\n")
    file.write("------------------")
