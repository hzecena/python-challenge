# import modules
import os
import csv

# csv file path
csvpath = os.path.join('Resources','election_data.csv')


# variables
votes = 0 
ballot_box = [] 
cand_list = [] 
cand_votes = 0 
winner = ""
votes_won = 0
create_file = 'election_results.txt'

# open csv file
with open(csvpath) as csvfile:
	election_data = csv.reader(csvfile, delimiter=',')

# SKIP HEADER
    election_data2 = next(election_data)

    for row in election_data2:
		candidate = str(row[2])
		ballot_box.append(candidate)
		
		votes += 1
		if cand_list.count(candidate) == 0:
			cand_list.append(candidate)

## PRINT RESULTS
	print('\nElection Results')
	print('-------------------------')
# The total number of votes cast
	total_votes = "{:,.0f}".format(votes)
	print("Total Votes: " + str(total_votes))
	print('-------------------------')

	for nominee in cand_list:
		cand_votes = ballot_box.count(nominee)
		Percent = (cand_votes/votes)*100
		if votes_won < cand_votes:
			votes_won = cand_votes
			winner = nominee 
		print(nominee + ': ' + '{:.3f}'.format(Percent) + '% (' + "{:,.0f}".format(cand_votes) + ')')
	
	print('-------------------------')
	print('Winner: ' + winner)
	print('-------------------------\n')

