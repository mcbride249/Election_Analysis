# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

Goals:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on the popular vote.

##Resources
-Data Source: election_results.csv
-Software: Python 3.7.10, Visual Studio Code, 1.38.1

**##Summary**
The analysis of the election show that:
-There were 369,711 votes case in the election.

-The Candidates were:
  -Diana DeGette
  -Charles Casper Stockham
  -Ratymon Anthony Doane
  
-The Candidate resuts were:
  -Diana DeGette received 73.8% of the vote and 272,892 number of votes
  -Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
  -Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
  
-The winner of the election was:
  -Diana Gette who received 73.8% of the vote and 272,892 number of votes

**##Module 3 Challenge - Written Analysis**

**##Challenge Overview - Overview of Election Audit**

The purpose of the election audit analysis was to write a series of code that would pull data from the Election Analysis CSV file and determine the total votes, votes for each candidate, percentage of votes, and determine the winning candidate in addition to calculating the total number and percentage of votes based on county, and then state which county had the largest voter turnout. This code would then output the respective totals and winners in a text file that could be easily ready and understood.

**##Election Audit Results**

https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Election_Analysis_Results.PNG

•	**How many votes were cast in this congressional election?**

    •	369,711 votes were cast in the congressional election.
  
    •	Code Reference: https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Code%20Snippet%201.PNG
  

•	**Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**

   •	County Votes:
  
     •	Jefferson: 10.5% percent of total votes; 38,855 total votes
    
     •	Denver: 82.8% percent of total votes; 306,055 total votes
        
     •	Arapahoe: 6.7% percent of total votes; 24,801 total votes
        
     •	Code Reference: https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Code%20Snippet%202.PNG
    
   
•**Which county had the largest number of votes?**

    •	Denver county had the largest number of votes with 306,055 total votes of 82.8% of the election votes.
  
  
•	**Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**

  •	Candidate Votes:
     
    •	Charles Casper Stockham: 23.0% percent of total votes; 85,213 total votes
  
    •	Diana DeGette: 73.8% percent of total votes; 272,892 total votes
  
    •	Raymon Anthony Doane: 3.1% percent of total votes; 11,606 total votes
  
    •	Code Reference: https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Code%20Snippet%203.PNG
  

•	**Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**

    •	Diana DeGette won the election with a winning vote count of 272,892 votes and a winning percentage of 73.8% of the vote.
    
    •	Code Reference: https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Code%20Snippet%204.PNG
  

**##Challenge Summary - Election Audit Summary**

This script could be used in any election by modifying the variable you want to analyze such as candidate name or different counties. Additionally, information could be included such as the number of candidates (for elections with a high number of them) as well as the number of counties involved in the election. The ranking of candidate results could be included in the code, or the production of a list of the candidates who lost. Furthermore, this code could be used to analyze data at different levels of government for an election such as the state level, in which case the code would be modified to reflect State instead of County. 

**Code Modification 1 – State Level: A simply change of the code that already exists could be used to calculate the election results at the State level:**

  https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Code%20Modification%201.py
  
**Code Modification 2 – Candidate Counter: The addition of a code could also be used to list the candidate names if there was a large list of candidates:**

https://github.com/mcbride249/Election_Analysis/blob/main/Resources/Code%20Modification%202.PNG
