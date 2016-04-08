from collections import Counter

A = Counter({'ABC':[10, 12], 'DEF':[10, 13], 'GHI':[10, 15]})
A = Counter({'ABC':[10, 12], 'DEF':[10, 13], 'GHI':[10, 15]})
B = Counter({'ABC':[10, 14], 'DEF':[10, 15]})
print(A + B)
#print(Counter({'c': 7, 'b': 5, 'd': 5, 'a': 1}))