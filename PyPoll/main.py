#[Vote Counting](Images/Vote_counting.png)
# In this challenge, you are tasked with helping a small, rural town 
#odernize its vote counting process.
# You will be give a set of poll data called [election_data.csv](PyPoll
#esources/election_data.csv). The dataset is composed of three columns:
#Voter ID`, `County`, and `Candidate`. Your task is to create a Python 
#cript that analyzes the votes and calculates each of the following:
# * The total number of votes cast
# * A complete list of candidates who received votes
# * The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
# ```text
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# ```
# In addition, your final script should both print the analysis to the 
#erminal and export a text file with the results.


import csv
import os

#initialize variables
candidates = []
votes = 0
vote_counts = []

#set path
file_name = 'election_data.csv'
filepath = os.path.join('Resources',file_name)

#open the file
with open(filepath,newline="") as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the header
    line = next(csvreader,None)

    #process votes
    for line in csvreader:

        #add to total number of votes
        votes = votes + 1

        #candidate voted for
        candidate = line[2]

        #add other votes to candidate total
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
#percentage of vote for each candidate
for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {votes}")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_summary.txt"

#open write file
filewriter = open(write_file, mode = 'w')

#print analysis to file
filewriter.write("Election Results\n")
filewriter.write("--------------------------\n")
filewriter.write(f"Total Votes: {votes}\n")
for count in range(len(candidates)):
    filewriter.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
filewriter.write("---------------------------\n")
filewriter.write(f"Winner: {winner}\n")
filewriter.write("---------------------------\n")

#close file
filewriter.close()
##  Set path  ##
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join ("analysis", "election_analysis.txt")















