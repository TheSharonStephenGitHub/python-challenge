import os
import csv

#opened the csv file
election_csv = os.path.join("Resources", "election_data.csv")

with open(election_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #excludes the header row
    next(csvreader)

    #initializes all of the variables used
    total_votes = 0

    candidates = []

    candidate_votes = []

    percent_candidate_votes = []

    #loops through each row
    for row in csvreader:
        
        total_votes += 1

        #creates an array of unique candidates and initializes their votes to 0
        if str(row[2]) not in candidates:
            candidates.append(str(row[2]))
            candidate_votes.append(0)
        
        #increments each existing candidate found by 1
        candidate_votes[candidates.index(str(row[2]))] += 1

    #calculates the percentage of candidate votes to total votes and places it into a separate array
    for vote in candidate_votes:
        percent_candidate_votes.append(round((vote / total_votes) * 100, 3))

    
    print("")
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
   
    index = 0
    #prints the results of each candidate
    for candidate in candidates:
       print(f"{candidate}: {percent_candidate_votes[index]}% ({candidate_votes[index]})")
       index += 1

    print("----------------------------")

    print(f"Winner: {candidates[candidate_votes.index(max(candidate_votes))]}")

    print("----------------------------")

#exports to txt
file = open("Analysis/Analysis_PyPoll.txt","w")
file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("----------------------------\n")
index = 0
for candidate in candidates:
    file.write(f"{candidate}: {percent_candidate_votes[index]}% ({candidate_votes[index]})\n")
    index += 1

file.write("----------------------------\n")
file.write(f"Winner: {candidates[candidate_votes.index(max(candidate_votes))]}\n")
file.write("----------------------------\n")
file.close()