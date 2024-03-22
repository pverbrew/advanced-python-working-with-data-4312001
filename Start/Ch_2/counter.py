# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

print("a counter is a dict that can help with lists of things")


# TODO: Create a Counter for class1 and class2
c1 = Counter(class1)
c2 = Counter(class2)

# TODO: How many students in class 1 named James?
print(c1["James"])
print(c2["James\n"])

# TODO: How many students are in class 1?
print(sum(c1.values()), "students in class 1\n")

# TODO: Combine the two classes
#note c1.update is an "in-place" operation on c1
c1.update(class2)
print(sum(c1.values()), "students in class1 and class2 after combining with 'c1.update'\n")

# TODO: What's the most common name in the two classes?
print(c1.most_common(3), "are the 3 most common names in the combined classes\n")

# TODO: Separate the classes again
c1.subtract(class2)
print(c1.most_common(1), "is the most common name in class 1 only now\n")

# TODO: What's common between the two classes?
print(c1 & c2)


#extra
for (k, v) in c1.items():
   print(k + ": " + str(v))

c1.update(class2)

print("\n update c1 with class2")
for (k, v) in c1.items():
   print(k + ": " + str(v))

