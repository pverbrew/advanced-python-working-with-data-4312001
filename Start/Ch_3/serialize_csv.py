# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates how to serialize data to a CSV file

import csv
import json
import datetime

# read in the contents of the JSON file
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5


# Filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))
#print(largequakes[0], "\n\n", largequakes[1], "\n\n")
print("length of largequakes is", len(largequakes))

#review: simplify largequakes
def simp(data):
    return {
        "place"     : data["properties"]["place"], 
        "magnitude" : data["properties"]["mag"],
        "numreport" : data["properties"]["felt"]
        }

simpstruct = list(map(simp, largequakes))
print("type for simpstruct is:", type(simpstruct))
print("typr for elements in simpstruct is:", type(simpstruct[0]), "\n")
print(simpstruct[0], "\n\n")





#TODO: Create the header and row structures for the data
header = ["Place", "Magnitude", "Date", "Link"]
rows = []

# TODO: populate the rows with the resulting quake data
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"])/1000)
    rows.append([quake["properties"]["place"], quake["properties"]
                ["mag"], thedate, quake["properties"]["url"]])


# TODO: write the results to the CSV file
print("NOTE: csv module writerow NO ENDLINE, writerows does ENDLINE at each row")
with open("largequakes.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)


print("type for largequakes is:", type(largequakes))
print("type for quake is:", type(quake), "\n")
#print("type for quake[0] is:", type(quake[0]), "\n")
print("type for rows is:", type(rows), "\n")
print("type for rows[0] is:", type(rows[0]), "\n")
