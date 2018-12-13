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

 

# find percentage and winner


percent = []
maxvote=num_votes[0]
maxindex=0

for count in range(len(candidates)):
    vote_percent=round(num_votes[count]/total_votes*100,1)
    percent.append(vote_percent)
    
    if num_votes[count]>maxvote:
        maxvote=num_votes[count]
        maxindex=count
winner=candidates[maxindex]
    

#prints to file
output_file = os.path.join('..', 'PyPoll', 'OutputPoll.csv')

with open(output_file, 'w') as csvfile:
    csvfile.writelines('Election Results \n------ \nTotal Votes: ' + str(total_votes) + 
      '\n-------\n')
    for count in range(len(candidates)):
        csvfile.writelines(f"{candidates[count]}:{percent[count]}% ({num_votes[count]})\n")
    csvfile.writelines('---------- \nWinner: ' + winner+ '\n-------')

#prints file to terminal
with open(output_file, 'r') as readfile:
    print(readfile.read())
