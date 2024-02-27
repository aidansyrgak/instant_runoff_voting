import pandas as pd
from pyrankvote import Candidate, Ballot, preferential_block_voting

# Reads the first column of the CSV (new format)
def process(input_path):
    df = pd.read_csv(input_path)

    # header (1st row) not included in the dataframe
    # start with 0
    candidates = []
    selected_columns = df.iloc[0, 1:].tolist()  # select a [row, column:] with candidate names
    for name in selected_columns:
        n = name.split("-")[-2].strip()
        candidates.append(Candidate(n))

    ballots = []
    for index, row in df.iloc[2:, 0].items():  # ballots start, [row:, column:]
        if pd.notna(row):
            a_ballot = []
            a_ballot_string = row.split(",")
            for i in a_ballot_string:
                a_ballot.append(Candidate(i))
            ballots.append(Ballot(ranked_candidates=a_ballot))




    finished = (candidates, ballots)
    return finished

