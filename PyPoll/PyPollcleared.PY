import csv

csvpath = "Resources/election_data.csv"

totalVotes = 0
candidates = set()
candidate_dict = {
    "Li": 0,
    "Khan": 0,
    "O'Tooley": 0,
    "Correy": 0
}

with open(csvpath, "r") as file:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')

    csvheader = next(csvreader)

    print(csvheader)
    print()

    for row in csvreader:
        #print(row)
        totalVotes += 1
        candidates.add(row[2])
    
        if row[2] == "Li":
            candidate_dict["Li"] += 1
        elif row[2] == "Khan":
            candidate_dict["Khan"] += 1
        elif row[2] == "O'Tooley":
            candidate_dict["O'Tooley"] += 1
        else:
            candidate_dict["Correy"] += 1


    print(totalVotes)
    print(candidates)
    print(candidate_dict)
    print()

#https://stackoverflow.com/questions/52603027/how-can-i-interpret-maxstats-key-stats-get-where-stats-is-some-dictionary
    max_cand = max(candidate_dict, key=candidate_dict.get)
    max_votes = candidate_dict[max_cand]

results = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------\n"""

for persons in candidate_dict.keys():
    perc = 100*(candidate_dict[persons] / totalVotes)
    results += f"{persons}: {round(perc, 2)}% ({candidate_dict[persons]})\n"


results += f"""-------------------------
Winner: {max_cand}
-------------------------
"""
print(results)


# writes to file
with open("analysis.txt", "w") as file:
    file.write(results)
