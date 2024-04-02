# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("largequakes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    print("type for reader is:", type(reader))
    #csv module has a sniffer to look for headers in the file
    sniffer = csv.Sniffer()
    #read the first 1024 locations in file looking for headers
    sample = csvfile.read(1024)
    #reset the file to the beginning after looking for headers
    csvfile.seek(0)

    #check sample for header using built-in sniffer function has_header
    #built-in "next" 

    if (sniffer.has_header(sample)):
        next(reader)

    for row in reader:
        #print(row)
        result.append(
            {
                "place" : row[0],
                "magnitude" : row[1],
                "date" : row[2],
                "link" : row[3]
            }      
        )

pprint.pp(result)
