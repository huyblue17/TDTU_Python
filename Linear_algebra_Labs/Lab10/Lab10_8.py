import numpy as np

#EX8
print("EX8")
#B1
B1 = np.array([[-18, 13, -4, 4],
               [2, 19, -4, 12],
               [-14, 11, -12, 8],
               [-2, 21, 4, 8]])

#B2
B2 = np.array([[6, -8, -4, 5, -4],
               [2, 7, -5, -6, 4],
               [0, -1, -8, 2, 2],
               [-1, -2, 4, 4, -8]])

# Compute the SVD of B1
U1, S1, VT1 = np.linalg.svd(B1)

# Compute the SVD of B2
U2, S2, VT2 = np.linalg.svd(B2)

# Print the singular value decomposition of B1
print("Singular Value Decomposition of B1:")
print("U1:")
print(U1)
print("S1:")
print(S1)
print("VT1:")
print(VT1)

# Print the singular value decomposition of B2
print("Singular Value Decomposition of B2:")
print("U2:")
print(U2)
print("S2:")
print(S2)
print("VT2:")
print(VT2)
