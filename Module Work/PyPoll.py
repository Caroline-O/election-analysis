# The data we need to retrieve.
import csv
import os
# 1. The total number of votes cast
# 2. A complete list of candiates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# Assign a variable for the file to laod and path.
file_to_load = os.path.join("Module Work","election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
# To do: perform analysis.
      print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Module Work", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
     # Write three counties to the file.
     txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")   
# --------------------------------------------------------------------------
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Module Work", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Module Work", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    print(next(file_reader))

    
