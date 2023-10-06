import numpy as np                                                
import sympy as sp
import math as m

#Tạo ma trận A
A = np.random.randint(1, 100, (10,10))                            

#Tạo ma trận B                                                              
B = np.random.randint(1, 20, (2,10))

#Tạo ma trận C
C = np.random.randint(1, 20, (10,2))

print("Matrix A: \n", A)                                          
print("Matrix B: \n", B)
print("Matrix C: \n", C)
print("-------------------------------------------------------------------")
#a.
print("a.")                                                       
#Chuyển vị các ma trận bằng hàm .T hoặc np.transpose
A_T = A.T                                                         
B_T = B.T                                                                     
C_T = C.T
# Tính toán kết quả bằng cách thêm A với chuyển vị của nó, nhân C và B,
# và nhân chuyển vị của B với chuyển vị của C
res_a = A + A_T + np.matmul(C,B) + np.matmul(B_T,C_T)             
print("Result: \n", res_a)

print("-------------------------------------------------------------------")
#b
print("b.")
res_b = 0
plus = 9
#Khởi tạo mảng từ 10 đến 21 bước nhảy 1 bằng np.arange
n = np.arange(10, 21, 1)                           
#Sử dụng vòng lặp chạy i trong n và sự dụng hàm np.linalg.matrix_power
for i in n:
    res_b += np.linalg.matrix_power(A/(plus+1), i)                        
print("Result: \n", res_b)

print("-------------------------------------------------------------------")
#c
print("c.")
def c (matrix) :
    mask = np.array([True, False] * (matrix.shape[0]//2))
    #Sử dụng mask để chọn hàng lẻ trong ma trận A  
    A_odd = matrix[mask] 
    return A_odd
print("Matrix A:\n", A)
print()
print("A_odd:\n",c(A))

print("-------------------------------------------------------------------")
#d
print("d.")
def d (matrix) :
    #Tạo boolean mask để chọn số nguyên lẻ trong ma trận 
    mask = matrix % 2 == 1
    #Chọn các số nguyên lẻ từ ma trận và làm phẳng thành một vecto
    odd_integers = matrix[mask].flatten()
    return odd_integers  
print("Matrix A:\n", A)
print()
print("A_odd interger :\n",d(A).tolist())

print("-------------------------------------------------------------------")
#e
print("e.")
res_e = []                                                
#Sử dụng vòng lặp để tìm số nguyên tố
for row in A:                                              
    for ele in row:                                                                                     
        if ele > 1:
            isprime = True                                    
            for i in range(2, ele):        
                if ele % i == 0:                              
                    isprime = False                            
                    break 
        if isprime:                                        
            res_e.append(ele)
print("Matrix A:\n", A)
print()
print("Result: \n", res_e)

print("-------------------------------------------------------------------")
#f
print("f.")
# Calculate D = CB
D = np.dot(C, B)

# Reverse elements in odd rows of D
def reverse_odd_rows(matrix):
    # Create a boolean mask to select odd rows
    mask = np.array([True, False] * (matrix.shape[0]//2))
    # Reverse odd rows
    matrix[mask] = np.fliplr(matrix[mask])
    return matrix

D_reversed = reverse_odd_rows(D)

# Print the matrices
print("Matrix B:")
print(B)
print("Matrix C:")
print(C)
print("Matrix D:")
print(D)
print("Matrix D with odd rows reversed:")
print(D_reversed)

print("-------------------------------------------------------------------")
#g
print("g.")
#Khởi tạo mảng rỗng và biến đếm
rows = []
max_count = 0
#Sử dụng vòng lặp để tìm số nguyên tố
for row in A:
    prime_count = 0
    for ele in row:
        if ele > 1:
            isprime = True
            for i in range (2, ele):
                if ele % i == 0:
                    isprime = False
                    break
            if isprime:
                prime_count += 1
    if prime_count > max_count:
        max_count = prime_count
        rows = [row]
    elif prime_count == max_count:
        rows.append(row)

print("Matrix A:\n", A)
print()
print("Rows with maximum count of prime:")
for row in rows:
    print(row)

print("-------------------------------------------------------------------")
#h
print("h.")
def longest_contiguous_odd_rows(matrix):
    rows = []
    max_length = 0
    for i in range(len(matrix)):
        current_row = []
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 != 0:
                current_row.append(matrix[i][j])
            else:
                if len(current_row) > max_length:
                    max_length = len(current_row)
                    rows = [matrix[i]]
                elif len(current_row) == max_length:
                    rows.append(matrix[i])
                current_row = []
        if len(current_row) > max_length:
            max_length = len(current_row)
            rows = [matrix[i]]
        elif len(current_row) == max_length:
            rows.append(matrix[i])
    return rows

print("Matrix A:",A)
result = longest_contiguous_odd_rows(A)
print("Rows with longest contiguous odd sequence:")
for row in result:
    print(row)


