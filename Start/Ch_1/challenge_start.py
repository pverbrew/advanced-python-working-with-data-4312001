# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)
    
def getQuake(data):
    if data["properties"]["type"] == "earthquake":
        return True
    return False

#create a new list of events that are quakes
quakes = list(filter(getQuake, data["features"]))


print("1: How many quakes are there in total?")
print(f"    There were {len(quakes)} quakes total")


print("\n\n")
print("2: How many quakes were felt by at least 100 people?")
feltThresh = 100
def feltQuake(data):
   feltby = data["properties"]["felt"]
#   if feltby is not None and feltby >= 100: ###these three lines replaced by one!!!
#       return True
#   return False
   return (feltby is not None and feltb >=100)


feltOverThresh= list(filter(feltQuake, quakes))
print("    ", len(feltOverThresh), "earthquakes were felt by more than", feltThresh, "people.")


print("\n\n")
print("3. Print the name of the place whose quake was felt by the most people, with the number of reports")
def feltNumber(data):
   feltnum = data["properties"]["felt"]
   if feltnum is None:
       feltnum = 0
   return feltnum

mostFelt = max(feltOverThresh, key=feltNumber)
print("    The quake felt by the most people was", mostFelt["properties"]["place"], "with", mostFelt["properties"]["felt"], "reports.")
   

#-----need to rework this---------      
#mostFeltQuake = (max(quake["properties"]["felt"]) is not None for quake in data["features"])
#print(f"The most felt quake was {mostFeltQuake["properties"]["place"]} and was felt by {mostFeltQuake["properties"]["felt"]} people.")
#-----need to rework this---------      
#
print("\n\n")
print("4. Print the top 10 most significant events, with the significance value of each")
def getsig(dataitem):
    significance = dataitem["properties"]["sig"]
    if significance is None:
        significance = 0
    return significance
quakes.sort(key=getsig, reverse=True)
for i in range (0,10):
  print(f'    {i+1}. {quakes[i]["properties"]["place"]} significance {quakes[i]["properties"]["sig"]}')
#
#
#
#
#
#
