# Example file for Advanced Python: Working With Data by Joe Marini
# sorting data with the sorted() and sort() functions

import json


numbers = [42, 54, 19, 17, 23, 31, 16, 4]
names = ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "Stacy"]

# TODO: the sorted() function can be used to return a new list with sorted data
print("use sorted for number array[42,54,19,17,23, 31, 16,4]\n", sorted(numbers))
print('use sorted for names array: ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "stacy"]\n', sorted(names)) 


# TODO: alternately, you can use the list object's sort() method, which sorts the list in-place
numbers.sort(reverse=True)
print("use reverse sort on number array[42,54,19,17,23, 31, 16,4]\n", numbers)
names.sort(reverse=True)
print('use reverse sort on names array: ["Jeff", "Bill", "Addie", "Stephanie", "Zach", "Lukas", "Joe", "stacy"]\n', names) 


# TODO: To sort custom objects, we can tell the sort function which property to use
# by specifying a key function

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
     data = json.load(datafile)


def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)


print ("\n\n\n====================================================================")
print("generate a list of the earthquakes from largest to smallest magnitude")
print("recall that sort goes from smallest to largest")
print('data["features"].sort(key=getmag, reverse=True)')
print ("====================================================================")
data["features"].sort(key=getmag, reverse=True)
for i in range(0,10):
    print(data["features"][i]["properties"]["place"],
          data["features"][i]["properties"]["mag"])
    
