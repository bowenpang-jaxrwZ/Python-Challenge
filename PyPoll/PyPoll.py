import csv

input_file = "Resources/election_data.csv"

totalcount = 0
candidate_list = []
CCS_count = 0
DD_count = 0
RAD_count = 0

with open(input_file, encoding='utf-8') as election_data_file:
    rows = csv.reader(election_data_file, delimiter=",")
    #header
    next(rows)
 
    for row in rows:
        totalcount+=1
        voterid=row[0]
        country=row[1]
        candidate=row[2]
    
        if row[2] not in candidate_list:
            #candidates+=[row[2]]
            candidate_list.append(row[2])


        if candidate == "Charles Casper Stockham":
            CCS_count+=1
        if candidate == "Diana DeGette":
            DD_count+=1
        if candidate == "Raymon Anthony Doane":
            RAD_count+=1

    CCS_percentage = round(CCS_count/totalcount *100,3)
    DD_percentage = round(DD_count/totalcount *100,3)
    RAD_percentage = round(RAD_count/totalcount *100,3)
    winner = max(CCS_count,DD_count,RAD_count)
 
    #total votes
    print(totalcount)
    #unique candidates (3 in total)
    print(candidate_list)
    print(CCS_count)
    print(DD_count)
    print(RAD_count)

    print(CCS_percentage)
    print(DD_percentage)
    print(RAD_percentage)



output = f"""
Election Results
-------------------------
Total Votes: {totalcount}
-------------------------
{candidate_list[0]}: {CCS_percentage}% ({CCS_count})
{candidate_list[1]}: {DD_percentage}% ({DD_count})
{candidate_list[2]}: {RAD_percentage}% ({RAD_count})
-------------------------
Winner: Diana DeGette
-------------------------
"""

print (output)

with open("analysis/pypoll_output.txt", "w") as txt_file:
    txt_file.write(output)