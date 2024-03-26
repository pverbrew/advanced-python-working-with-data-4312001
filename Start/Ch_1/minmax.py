#  Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen"]


# TODO: The min() function finds the minimum value
# TODO: The min() function finds the minimum vale
print("# TODO: The min() function finds the minimum value")
print('NOTE: using f-strings: format print(f"min value is {min(values)}")') 
print(f"minimum value of values is {min(values)}")
print(f"minimum value of strings is {min(strings)}")


# TODO: The max() function finds the maximum value
print("# TODO: The max() function finds the maximum value")
print(f"maximum value of values is {max(values)}")
print(f"maximum value of strings is {max(strings)}")


# TODO: define a custom "key" function to extract a data field
print("default key for max and min for str is alphabetic order")
print("to key on length of strings for max and min, call the function with a key")
print('print(f"maximum value of strings is {max(strings,key=len))}")')
print('print(f"minimum value of strings is {min(strings,key=len))}")')
print(f"maximum value of values is {max(strings,key=len)}")
print(f"minimum value of strings is {min(strings,key=len)}")

# TODO: open the data file and load the JSON
#with open("../../30DayQuakes.json", "r") as datafile:
#    data = json.load(datafile)
#
#print("json file dataset and title are",data["metadata"]["title"]) 
#print("jason has dict instances for ", len(data["features"]), "features (which are earthquake events)")
#
#print("create a function to pull 'mag' from 'properties' dict of 'features' dict")
#print("since some entries are 'null', set mag to zero for those")
#def getmag(dataitem):
#    magnitude = dataitem["properties"]["mag"]
#    if magnitude is None:
#        magnitude = 0
#    return float(magnitude)
#
#print("Print features with the min and max magnitudes")
#print(min(data["features"], key=getmag))
#print(max(data["features"], key=getmag))


      
