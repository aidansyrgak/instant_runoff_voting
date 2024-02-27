import pandas as pd
from pyrankvote import Candidate, Ballot, preferential_block_voting

# Reads and processes the CSV data row by row
def process(input_path):
    df = pd.read_csv(input_path)

    # header (1st row) not included in the dataframe
    # start with 0
    candidates = []
    selected_columns = df.iloc[0, 1:].tolist() # select a [row, column:] with candidate names
    for name in selected_columns:
        n = name.split("-")[-2].strip()
        candidates.append(Candidate(n))

    ballots = []
    for index, row in df.iloc[2:, 1:].iterrows(): # ballots start, [row:, column:]
        ballot_list = []
        for column, value in row.items():
            ballot_list.append(value)

        ballot_with_rank = []
        for i in range(len(ballot_list)):
            entry = ballot_list[i]
            if pd.notna(entry):
                vote_for = candidates[i]
                rank_for = int(entry)
                tuple = (vote_for, rank_for)
                ballot_with_rank.append(tuple)
        ballot_with_rank.sort(key=lambda x: x[1])

        a_ballot = []
        for item in ballot_with_rank:
            a_ballot.append(item[0])

        ballots.append(Ballot(ranked_candidates=a_ballot))

    finished = (candidates, ballots)
    return finished

