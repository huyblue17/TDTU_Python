import itertools
cat_gender = ['M', 'F']

#a
List = list(itertools.combinations(cat_gender*3, 3))
S = []
for comb in List:
    S.append(''.join(comb))
print("a ",S)

#b
len_S = len(S)
print("b ",len(S))

#c
B = []

for comb in S:
    if 'F' in comb:
        B.append(comb)
print("c ", B)

#d
D = []

for comb in S:
    if 'FFF' in comb:
        D.append(comb)
print("d ", D)

#e
Pa_over_b = len(D) / len(B)
print("d ", Pa_over_b)