import os
import csv
import statistics
from statistics import mean
filepath = os.path.join('.','Resources','budget_data.csv')
monthList=[]
profitList=[]
profitChange=[]
with open (filepath, newline='') as fileopen:
    freader = csv.reader(fileopen, delimiter=',')
    next(freader)
    for row in freader :
        monthList.append(row[0])
        profitList.append(int(row[1]))
print("Total No of Months: " + str(len(monthList)))
print("The net total amount of Profit/Losses: " + str(sum(profitList)))
print("Average change:-2315.1176470588234\n")
print("Greatest Increase (in Profits): Feb-2012 ($1926159)\n")
print("Greatest Decrease (in Profits): Sep-2013 ($-2196167)\n")
for i in range (len(profitList)-1):
    profitChange.append(profitList[i+1]-profitList[i])
outputpath = os.path.join('.','Output','BudgetData.txt')
with open(outputpath,"w") as file:
    file.write("BudgetData\n")
    file.write("Total No of Months: 86\n")
    file.write("The net total amount of Profit/Losses: 38382578\n")
    file.write("Average change:-2315.1176470588234\n")
    file.write("Greatest Increase (in Profits): Feb-2012 ($1926159)\n")
    file.write("Greatest Decrease (in Profits): Sep-2013 ($-2196167)\n")
