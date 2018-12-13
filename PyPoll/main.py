import os
import csv



csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

total_votes = 0

candidates = []
num_votes = []

#gets data file
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    row=next(csvread, None)
    
   
    #counts votes 
    for row in csvread:
        candidate=row[2]
        total_votes += 1
        if candidate in candidates:
            index=candidates.index(candidate)
            num_votes[index]+= 1
        else:
            candidates.append(candidate)
            num_votes.append(1)


# creates vote percent list
vote_percent = []

percent = []

for count in range(len(candidates)):
    vote_percent=round(num_votes[count]/total_votes*100,1)
    percent.append(vote_percent)
    
 vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))   

#zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, range(len(candidates)), percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

 #makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
   for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#prints to file
output_file = os.path.join('..', 'PyPoll', 'OutputPoll.csv')

with open(output_file, 'w') as csvfile:
    csvfile.writelines('Election Results \n------ \nTotal Votes: ' + str(total_votes) + 
      '\n-------\n')
    for count in range(len(candidates)):
        csvfile.writelines(f"{candidates[count]}:{percent[count]}% ({num_votes[count]})\n")
    csvfile.writelines('---------- \nWinner: ' + winner + '\n-------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
