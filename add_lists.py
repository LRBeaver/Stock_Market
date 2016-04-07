first = [1,2,3,4,5]
second = [6,7,8,9,10]

third = [x + y for x, y in zip(first, second)]
print(third)

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
A = {(3,'x'):-2, (6,'y'):3, (8, 'b'):9}
B = {(3,'y'):4, (6,'y'):6}
print({k: A.get(k,0) + B.get(k,0) for k in A.keys() | B.keys()})
#{(8, 'b'): 9, (3, 'x'): -2, (6, 'y'): 9, (3, 'y'): 4}

