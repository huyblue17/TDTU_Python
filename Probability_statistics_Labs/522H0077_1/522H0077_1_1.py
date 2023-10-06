import itertools

#EX1
print("EX1")
A = {1, 2, 3, 4, 5}
n = 3

num_length = len(A)
num_3_digit = list(itertools.permutations(A, n))

for i in num_3_digit:
  print(i)
print("Size =", "%i!/(%i-%i)! = " %(num_length ,num_length ,n), len(num_3_digit))