# first = [1,2,3,4,5]
# second = [6,7,8,9,10]
#
# third = [x + y for x, y in zip(first, second)]
# print(third)

# four = {'a':1, 'b':2,'c':3,'d':4,'e': 5}
# five = {6,7,8,9,10}
#
# sixth = [x + y for x, y in zip(four, five)]
# print(sixth)

#
# dic0 = {'dic0':0}
# dic1 = {'dic1':1}
# #ndic = dict(dic0.items() + dic1.items())
# ndic = list(dict(dic0.items()) + list(dic1.items()))
# print(ndic)


# This works
# A = {(3,'x'):-2, (6,'y'):3, (8, 'b'):9}
# B = {(3,'y'):4, (6,'y'):6}
# print({k: A.get(k,0) + B.get(k,0) for k in A.keys() | B.keys()})
# #{(8, 'b'): 9, (3, 'x'): -2, (6, 'y'): 9, (3, 'y'): 4}

#NO
# X = {(10,12):'ABC', (10,14):'DEF', (10, 13):'GHI'}
# C = {(10,14):'ABC', (10,16):'JKL'}
# print({k: X.get(k,0) + C.get(k,0) for k in X.keys() | C.keys()})

#NO
# X = {(10,12):'ABC', (10,14):'DEF', (10, 13):'GHI'}
# C = {(10,14):'ABC', (10,16):'JKL'}
# print({k: X.get(k,0) + C.get(k,0) for k in X.keys() | C.keys()})

#THIS WORKS
# A = {(3,'x'):-2, (6,'y'):3, (8, 'b'):9}
# B = {(3,'y'):4, (6,'y'):6}
# import collections
# C = collections.Counter(A)
# C.update(B)
# print(dict(C))
#print({(3, 'y'): 4, (8, 'b'): 9, (3, 'x'): -2, (6, 'y'): 9})

#WORKS NOT GREAT
# X = {(10,'ABC'):12, (10,'DEF'):14, (10, 'GHI'):16}
# Z = {(10,'ABC'):13, (10,'JKL'):15}
# import collections
# D = collections.Counter(X)
# D.update(Z)
# print(dict(D))
# #print({(3, 'y'): 4, (8, 'b'): 9, (3, 'x'): -2, (6, 'y'): 9})

#NO
# # A = {(3,'x'):-2, (6,'y'):3, (8, 'b'):9}
# B = {(3,'y'):4, (6,'y'):6}
# C = dict()
# for key in set(A.keys() + B.keys()):
#     C[key] = A.get(key, 0) + B.get(key, 0)
# print(C)

#WORKS
#Needed if you're using python3
# from functools import reduce
#
# A = {(3,'x'):-2, (6,'y'):3, (8, 'b'):9}
# B = {(3,'y'):4, (6,'y'):6}
#
# #Merging all the key/value(s) inside one big list
# C = list(A.items()) + list(B.items())
# #C = [((3,'x'), -2), ((6,'y'), 3), ...]
#
# #Keeping a list of all unique (hence the set) keys available
# keys = set([key[0] for key in C])
# #keys = set([(3,'x'), (6,'y'), ...])
#
# result = {}
# for key in keys:
#     #Extracing the pairs that corresponds to the current key
#     local = [item for item in C if item[0] == key]
#     #local = [((6,'y'), 3), ((6,'y'), 6)]
#
#     #Actually doing the sum and storing the ready to insert result
#     my_sum = reduce(lambda x,y: (x[0], x[1] + y[1]), local)
#     #my_sum = [((6,'y'), 9)]
#
#     #Actually inserting the result into the result set
#     result.update({my_sum[0]: my_sum[1]})
#     #result.update({(6,'y'): 9})
#
# print(result)

# a=[("13.5",100)]
# b=[("14.5",100), ("15.5", 100)]
# c=[("15.5",100), ("16.5", 100)]
# input=[a,b,c]

# from collections import Counter
#
# print(sum((Counter(dict(x)) for x in input), Counter()))

#WORKS
# from collections import Counter
# A = Counter({'a':1, 'b':2, 'c':3})
# B = Counter({'b':3, 'c':4, 'd':5})
# A + B
# print(Counter({'c': 7, 'b': 5, 'd': 5, 'a': 1}))

from collections import Counter

A = Counter({'ABC':{10: 12}, 'DEF':{10, 13}, 'GHI':{10:15})
B = Counter({'ABC':{10:14}, 'DEF':{10:15}})
print(A + B)
#print(Counter({'c': 7, 'b': 5, 'd': 5, 'a': 1}))