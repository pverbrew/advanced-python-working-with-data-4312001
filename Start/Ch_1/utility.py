# Example file for Advanced Python: Working With Data by Joe Marini
# demonstrates the use of the any, all, and sum functions
import json

values = [0, 1, 2, 3, 4, 5]

# TODO: any() can be used to see if any value in a sequence is True
x = any(values)
print(x)

# TODO: all() will detect if all of the values in a sequence are True
x = all(values)
print(x)


# TODO: sum() can be use to add all of the values in a sequence
x = sum(values)
print(x)


# these utility functions don't have callbacks like min or max,
# but we can use a generator for more fine control

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

feltAboveThresh = 0


def getAnyFelt(dataitem, minFelt):
    numfelt=features[properties][felt]
    if numfelt == null:
        numfelt = 0
    if numFelt > minFelt:
        exceedsThresh = True
    else:
        exceedsThresh = False

    return exceedsThresh

# TODO: are there any quake reports that were felt by more than 25,000 people?
feltThreshold = 25000
print("Were any quakes felt by more than", feltThreshold, "people?  ", any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > feltThreshold
          for quake in data["features"]))

# TODO: how many quakes were felt by more than 500 people?
feltThreshold = 500
print("How many quakes felt by more than", feltThreshold, "people?  ", sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > feltThreshold
          for quake in data["features"]))

# TODO: how many quakes had a magnitude of 6 or larger?
magThreshhold = 6
print("How many quakes had magnitudes of",magThreshhold, "or higher?    ", sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] >= magThreshhold
          for quake in data["features"]))
