#6. Write a python program to find the repeated items of a tuple.
from collections import Counter
tup = [2,3,4,5,3,4,2]
alist = list(tup)
result = dict(Counter(alist))
print (result)
