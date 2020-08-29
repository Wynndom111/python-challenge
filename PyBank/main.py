#In this challenge, you are tasked with creating a Python script for analyzing the financial 
# records of your company. You will give a set of financial data called[budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

#Your task is to create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits(date and amount) over the entire period

#The greatest decrease in losses(date and amount) over the entire period

#As an example, your analysis should look similar to the one below:

#```text
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)


# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#__________________________________________________________________________________________________________________________#

##  Import modules  ##

import csv
import os


##  Set path  ##
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join ("analysis", "budget_analysis.txt")



#Define Variables

count_months = 0
net_profit = 0
monthly_changes = 0
monthly_profit = 0
profit = []
month_list = []
monthchange_list = []




##  Read .csv using chocolate cake recipe  ##

with open(file_to_load) as budget_data:

    reader = csv.reader(budget_data, delimiter= ",")

    #print(reader)

    next(reader)

    #print(header)


## The total number of months and profit ##
    for row in reader:
        count_months += 1
        month_list.append(row[0])
        #print(count_months)

        net_profit = net_profit + int(row[1])
        #profit.append(row[1])


## Find/Calculate profit change ##
        if monthly_changes !=0:

            monthly_profit = int(row[1])

            monthly_changes = monthly_profit - monthly_changes

            monthchange_list.append(monthly_changes)

            monthly_changes = int(row[1])

        elif monthly_changes == 0:
            monthly_changes = int(row[1])
    monthchange_list.pop(0) 


## Most profitable and least profitable months ##

    #Most 
pmax = monthchange_list.index(max(monthchange_list))
    #Least 
pmin = monthchange_list.index(min(monthchange_list))  

## Match pmin and pmax with corresponding months ##  

GreatestIncrease = (month_list[int(pmax)], max(monthchange_list))

GreatestDecrease = (month_list[int(pmin)], min(monthchange_list))
    
## Average change ##      
average = sum(monthchange_list)/len(monthchange_list)
average = round(average,2)
    
        


## Print out results ##

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {count_months}")
print(f"Total:  ${net_profit}")
print(f"Average Change:  ${average}")
print(f"Greatest Increase in Profit:  {GreatestIncrease}")
print(f"Greatest Decrease in Profit:  {GreatestDecrease}")


#Write to .txt file
with open('file_to_output', 'w') as budget_analysis:
    budget_analysis.write("Financial Analysis\n")
    budget_analysis.write("----------------------------\n")
    budget_analysis.write(f"Total Months: {count_months}\n")
    budget_analysis.write(f"Total:  ${net_profit}\n")
    budget_analysis.write(f"Average Change:  ${average}\n")
    budget_analysis.write(f"Greatest Increase in Profit:  {GreatestIncrease}\n")
    budget_analysis.write(f"Greatest Decrease in Proft:  {GreatestDecrease}\n")

    budget_analysis.write("")
    budget_analysis.close()













