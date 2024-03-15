# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print("json file dataset and title are",data["metadata"]["title"]) 
print("jason has dict instances for ", len(data["features"]), "features (which are earthquake events)")

print("create a function to pull 'mag' from 'properties' dict of 'features' dict")
print("since some entries are 'null', set mag to zero for those")
def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if magnitude is None:
        magnitude = 0
    return float(magnitude)

print("Print features with the min and max magnitudes")
print(min(data["features"], key=getmag))
print(max(data["features"], key=getmag))

datamin = min(data["features"], key=getmag)

datamax = max(data["features"], key=getmag)

print("min mag was", datamin["properties"]["mag"],"located", datamin["properties"]["place"])
print("max mag was", datamax["properties"]["mag"],"located", datamax["properties"]["place"])


