# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getsig(data):
    significance = data["properties"]["sig"]
    return 0 if significance is None else significance      


data["features"].sort(key=getsig, reverse=True)
sigevents = data["features"][:40]
sigevents.sort(key=lambda e: e["properties"]["time"], reverse=True)

rows = []
i = int(0)
header = ["magnitude", "place", "felt by", "date", "google maps link"]
for feature in sigevents:
    #note: time and date are combined into a single integer for milliseconds since a ref date
    t = datetime.date.fromtimestamp(int(feature["properties"]["time"])/1000) #get date & time from "time" 
    #get date only from date time - defaults to desired format yyyy-mm-dd
    #t = t.date


    ##maplink = #figure out google map link from "coordinates"
    #googlemaplink = "https://www.google.com/maps/place/" + latitude + "," + longitude
    #example: https://www.google.com/maps/place/49.46800006494457,17.11514008755796    
    gmlbase = "https://www.google.com/maps/place/"
    gml = gmlbase + str(feature["geometry"]["coordinates"][1]) + "," + str(feature["geometry"]["coordinates"][0])

    #build each row of the csv
    #note: assignment wants sorted by significance but we are outputting mag and not significance
    #      so I could verify sorting, I added significance to the rows (extra credit)
    #      if this was a deliverable, I'd delete the significance
    rows.append ([
        feature["properties"]["sig"], 
        feature["properties"]["mag"], 
        feature["properties"]["place"], 
        feature["properties"]["felt"], 
        t,
        gml
        ]) 

#print("test csv data by printing to terminal...")
#print(header)
#print(rows)

with open("challenge.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)







