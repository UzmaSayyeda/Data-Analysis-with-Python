# import libraries
import os
import csv

# set file path to csv and text files
csvpath = os.path.join("PyPoll\\resources\\election_data.csv")
analysis = os.path.join("PyPoll\\analysis","analysis.txt")

# set variables
total_votes = 0
candidates = []
candidate_vote = {}
winner_votes = 0
winner = " "

# open file
with open (csvpath) as csvfile:
    
    # set reader and header
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    # loop through to count total votes per candidate
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]

        # if statement to find candidate names
        # add them to a dictionary with candidate name as keys and votes as values
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_vote[candidate]=0
        candidate_vote[candidate]=candidate_vote[candidate]+1

# writing in output text file        
with open(analysis, "a") as txtfile:
    txtfile.write( f"Election Results \n"
                  
                  f"---------------------\n"
                  f"Total votes: {total_votes} \n"

                  f"---------------------\n"
                  )    
    # loop to find vote percentage from candidate_vote dictionary 
    for candidate in candidate_vote:
        votes = candidate_vote[candidate]
        vote_percent = votes / total_votes * 100

        #round to 3 decimal spaces.
        vote_percent = round(vote_percent,3)


        # find most number of votes and candidate name
        # write the percent of votes per candidate in the loop
        if (votes > winner_votes):
            winner_votes = votes
            winner = candidate


        txtfile.write(f"{candidate} : {vote_percent}% ({(votes)})  \n")
    
# Write the winner in output text file
with open(analysis, "a") as txtfile:
    txtfile.write(f"---------------------\n"

                  f"Winner : {winner} \n"
                  f"----------------------\n"                  
                  )
    
    # print results:

    print(f"Total votes : {total_votes} \n")

    for candidate in candidate_vote:
        votes = candidate_vote[candidate]
        vote_percent = votes / total_votes * 100
        vote_percent = round(vote_percent,3)
        print(f"{candidate} : {vote_percent}% ({(votes)})  \n")
   

    print(f"Winner : {winner}")