def cross(A, B):
    return {a + b for a in A for b in B}
urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')

#EX2
print("EX2")

import itertools
U3 = list(itertools.combinations(urn, 3))

#a.
print("a.")
len_U3 = len(U3)
print(len_U3)

#b.
print("b.")
for size in U3:
    colorW = size[0][0]
    colorB = size[1][0]
    colorR = size[2][0]
    if len(set([colorW, colorB, colorR])) == 3:
        print(size)

#c.
for size in U3:
    if size[0][0] == 'W' and size[1][0] == 'R':
        print(size)