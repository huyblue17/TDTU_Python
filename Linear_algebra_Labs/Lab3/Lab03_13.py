import numpy as np

#EX13
print("EX13: ")
def det(m):
    return np.linalg.det(m)

def generate_matrices(n):
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)
    return A, B

def check_equation(A, B):
    det_sum = det(A + B)
    det_AB = det(A) + det(B)
    return abs(det_sum - det_AB) < 1e-6

for dim in [2, 3, 4, 5, 6, 7, 10]:
    A, B = generate_matrices(dim)
    if check_equation(A, B):
        print("The equation det(A+B) = detA + detB holds for {dim}x{dim} matrices.")
    else:
        print("The equation det(A+B) = detA + detB does not hold for {dim}x{dim} matrices.")

