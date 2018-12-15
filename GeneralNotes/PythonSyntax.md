



Join a set:
a = set([1,2,3])
b = set([4])
a = a.union(b) # {1,2,3,4}


sort by multiple keys in a nested array:
a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
a = sorted(a, key= lambda x: (x[0], x[1])) # [[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]

sort by multiple keys and some are in reverse
a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
b = sorted(sorted(a, key = lambda x : x[1]), key = lambda x : x[0], reverse = True) 
b == [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

This is because in Python sorting the relative order does not change.


How inserting work with index:
>>> a = [1,2,3,4]
>>> a.insert(2,10)
>>> a
[1, 2, 10, 3, 4]
It will insert to the index that will be the new index for the element  