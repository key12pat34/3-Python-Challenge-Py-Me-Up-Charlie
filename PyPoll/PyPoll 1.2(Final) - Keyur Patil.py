#PyPoll

import os
import csv
import sys 

#file path
election_data_csvfile = os.path.join('..', 'Resources', 'election_data.csv')


def election_calc(rowdata):
   
    

    print('----------------------------')
    print('Election Results')
    print('----------------------------')
    
    #--------variables/lists:-----------
    # ----------------------------------      
    voterid_list = []               #Colume 1 (from data set)
    candidate_list = []             #Colume 3 (from data set)
    unique_candidate_list=[]        #the candidates from data set
    percentage = []                 #percentage of each candidate
    
    for a,b,c in rowdata:
        #inserting column a and c into their own lists
        voterid_list.append(int(a))
        candidate_list.append(str(c))
        
        #checks if each row-data from c-column(from dataset) is not in the unique_candidate_list. Appends/adds into a list if its not there
        if c not in unique_candidate_list:
            unique_candidate_list.append(str(c))



    #The total number of votes cast
    total_votes = len(voterid_list)
    print(f'Total Votes: {total_votes}')
    print('----------------------------')




    #for range 1 to length of unique_candidate_list    
    for i in range(len(unique_candidate_list)):
        
        #percentage formula, rounded, then put into a percentage list
        percentage.append(round(((candidate_list.count(unique_candidate_list[i]) / total_votes) * 100),3))
   
        #prints candidate name, percentage and number of votes
        print(f'{unique_candidate_list[i]}: {percentage[i]}% ({candidate_list.count(unique_candidate_list[i])})') 
    

    


    print('----------------------------')
    #finding the winner's index, and then using the index position to find the name
    winner_can = percentage.index(int(max(percentage)))
    print (f'Winner: {unique_candidate_list[winner_can]}')
    print('----------------------------')
    
    # stdoutOrigin = sys.stdout 
    # sys.stdout = open("PyPoll_output.txt", "a")

    with open("PyPoll_output.txt", "w") as f:
        sys.stdout = f # Change the standard output to the file we created.
        
        print('----------------------------')
        print('Election Results')
        print('----------------------------')
        print(f'Total Votes: {total_votes}')
        print('----------------------------')
        
        for i in range(len(unique_candidate_list)):
            percentage.append(round(((candidate_list.count(unique_candidate_list[i]) / total_votes) * 100),3))
            print(f'{unique_candidate_list[i]}: {percentage[i]}% ({candidate_list.count(unique_candidate_list[i])})') 
        
        print('----------------------------')
        print (f'Winner: {unique_candidate_list[winner_can]}') 
        print('----------------------------')
        stdoutOrigin = sys.stdout # Reset the standard output to its original value
    
   
        
  



#opens files, sets delimiters, and passes data into 'election_calc' function
with open(election_data_csvfile, 'r') as csvfile:    

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #sendig csvreader data into election_calc funtion
    election_calc(csvreader)


