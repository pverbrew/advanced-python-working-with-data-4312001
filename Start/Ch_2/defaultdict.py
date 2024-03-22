# Demonstrate the usage of defaultdict objects
print("having to initalize dict adds unnecessary clutter to code")
print("collections.defaultdict is a cleaner way to do this/n/n")

print(" import default dict from collections library")
print("from collections import defaultdict\n")
from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']


print(' # use a dictionary to count each element')
print("using an of-the-shelf dict requires checking to add keys")
print('fruitCounter = dict()')
print('')
print('# Count the elements in the list')
print('for fruit in fruits:')
print('    if fruit in fruitCounter.keys()')
print('        fruitCounter[fruit] += 1')
print('    else:')
print('     fruitCounter[fruits] = 1')

print('\n\n# use a defaultdict dictionary to count each element')
print('# the argument for defaultdict is called a "factory method"')
print('fruitCounter = defaultdict(int)')
print('')
print('# Count the elements in the list')
print('for fruit in fruits:')
print('    fruitCounter[fruit] += 1\n\n')

# use a defaultdict dictionary to count each element
# the argument for defaultdict is called a "factory method"
fruitCounter = defaultdict(int)

# Count the elements in the list
for fruit in fruits:
    fruitCounter[fruit] += 1


# print the result
for (k, v) in fruitCounter.items():
    print(k + ": " + str(v))

#just print the dict
print(fruitCounter)
