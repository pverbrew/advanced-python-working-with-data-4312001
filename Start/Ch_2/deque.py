# deque objects are like double-ended queues
print("deque is pronounced 'deck'")
print("its name comes from 'double-ended queue\n")
print("d = collections.deque('abcde') forms a deque")
print("appendleft to add to front, append to add to end")
print("popleft for front, pop for end")

import collections
import string


# TODO: initialize a deque with lowercase letters
d = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(len(d), "is the lenth of the deque\n")

# TODO: deques can be iterated over
for elem in d:
    print(elem.upper())

# TODO: manipulate items from either end
d.pop()
print("pop 1: ", d)
d.popleft()
print("popleft 1: ", d)
d.append(2)
print("append 2: ", d)
d.appendleft(1)
print("appendleft 1: ", d)

# TODO: use an index to get a particular item
d.rotate(1)
print("rotate(1)  right: ", d)
d.rotate(-1)
print("rotate(-1)  left: ", d)
