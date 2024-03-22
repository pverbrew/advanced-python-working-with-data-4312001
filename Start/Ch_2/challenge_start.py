# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data
# Create a display that shows each of the seismic "type" and a count of how many times it occurred

from collections import defaultdict  
import json


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def gettype(dataitem):
    d = dataitem["properties"]["type"]
    return d

#create a list containing the set with each feature in "features" ["properties"]["type"]
e = list(filter(gettype,data["features"]))
##print(len(e))
##print(e[3])
##print("\n\n",e[3]["properties"]["type"])


#create a one dimensional list of all the events' type
el = list()
for i in range (0,len(e)):
   el.append(e[i]["properties"]["type"])

#get out a big hammer and print the list of 11745 events type
##print("\n",el)
##print("\n", len(el))

# initialize a counter for the events type array
eventCounter = defaultdict(int)

#populate the eventCounter defaultdict
for i in el:
    eventCounter[i] += 1

#print the defaultdict in its list form
#print("\n", eventCounter, "\n\n")


#print the defaultdict in the format requested by the challenge
#<eventType> : <numberOfOccurances>
print("\n\n  eventType  : occurrances")
for (k, v) in eventCounter.items():
    print(k + ": " + str(v))

print(f"\n\neventType      : occurrances")
for (k, v) in eventCounter.items():
    print(f"{k:15}: {v}")


