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


##  Set path  ##
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join ("analysis", "election_analysis.txt")















