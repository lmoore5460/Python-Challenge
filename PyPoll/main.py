import csv

#Read the CSV file
filename = "election_data.csv"
with open('/Users/Repository/PyPoll/Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    data = list(csvreader)

#variables
total_votes = 0
candidate_votes = {}
candidates = set()

#Loop the data
for row in data[1:]:
    # Increment total vote count
    total_votes += 1
    
    # Add candidate to the set of unique candidates
    candidate = row[2]
    candidates.add(candidate)
    
    # Increment vote count for the candidate
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

#Calculate the percentage of votes ea candidate won
vote_percentages = {}
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    vote_percentages[candidate] = percentage

#Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

#Print and export the analysis results
output_file = "election_results.txt"
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    file.write("Candidates:\n")
    for candidate in candidates:
        percentage = vote_percentages[candidate]
        votes = candidate_votes[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

    # Print the analysis results to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print("Candidates:")
    for candidate in candidates:
        percentage = vote_percentages[candidate]
        votes = candidate_votes[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

print("Analysis results exported to", output_file)

