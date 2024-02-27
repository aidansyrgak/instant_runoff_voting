from pyrankvote import Candidate, Ballot
import csvconvert
import simplecsv
import pyrankvote

# Specify the path to the CSV file here
csv_file = "path/to/csv"

# Specify the required number of seats here
number_of_seats = 0



# ----------------------------------------------------------------------------------------------------------------------
# Driver code for running the results - shouldn't need to touch
election_data = simplecsv.process(csv_file)
candidates = election_data[0]
ballots = election_data[1]
num_of_winners = 0
while (num_of_winners != number_of_seats):
    election_result = pyrankvote.preferential_block_voting(candidates, ballots, number_of_seats)
    #election_result = pyrankvote.instant_runoff_voting(candidates, ballots)
    winners = election_result.get_winners()
    num_of_winners = len(winners)
print(election_result)
