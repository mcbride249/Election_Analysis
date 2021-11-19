# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "Election_Analysis.txt")

# Initialize a total vote counter.
total_votes = 0


#Create a state list and state votes dictionary.
state_list = []
state_votes = {}

#Track the largest state and state voter turnout.
winning_state = ""
winning_state_turnout = 0


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

         # 3: Extract the state name from each row.
        state_name = row[1]

        # 4a: Write an if statement that checks that the
        # state does not match any existing state in the state list.
        if state_name not in state_list:

            # 4b: Add the existing state to the list of counties.
            state_list.append(state_name)

            # 4c: Begin tracking the state's vote count.
            state_votes[state_name] = 0 

        # 5: Add a vote to that state's vote count.
        state_votes[state_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"state Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the state from the state dictionary.
    for state_name in state_list:

        # 6b: Retrieve the state vote count.
        votes = state_votes.get(state_name)

        # 6c: Calculate the percentage of votes for the state.
        vote_percentage = float(votes) / float(total_votes) * 100
        state_results = (
            f"{state_name}: {vote_percentage:.1f}% ({votes:,})\n")

         # 6d: Print the state results to the terminal.
        print(state_results)

         # 6e: Save the state votes to a text file.
        txt_file.write(state_results)

         # 6f: Write an if statement to determine the winning state and get its vote count.
        if (votes > winning_state_turnout):
            winning_state = state_name
            winning_state_turnout = votes

    # 7: Print the state with the largest turnout to the terminal.
    winning_state_turnout_summary = (
        f"-------------------------\n"
        f"Largest state Turnout: {winning_state}\n"
        f"-------------------------\n")
    print(winning_state_turnout_summary)

    # 8: Save the state with the largest turnout to a text file.
    txt_file.write(winning_state_turnout_summary)


