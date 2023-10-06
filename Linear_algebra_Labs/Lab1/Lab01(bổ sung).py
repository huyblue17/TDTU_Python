import numpy as np  
import math as m

#EX1
print("1.")
x = [1, 3, 5, 2, 9]
y = [1, 3, 15, 27, 29]

vector_x = np.array(x)
vector_y = np.array(y)

print("Vector x")
print(vector_x, "have", len(x), "elements")

print("Vector y")
print(vector_y ,"have", len(y), "elements")

#EX2
print("2.")
print("Type n: ")
n = int(input())
a = np.arange(12,12+n*2,2)
b = np.arange(31,31+n*2,2)
c = np.arange(round(-n/2),round(n/2+1),1)
d = np.arange(round(n/2),round(-(n/2-1)),-1)
e = np.arange(n/2,-(n-2),-2)
f = 1/(2**np.arange(0,n))
fibonacci = [1,1]
for i in range (2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
g = 1/np.array(fibonacci)
prime = []
for i in range (2, int(n**0.5)+1):
    if n % i == 0:
        prime.append(i)
h = 1/np.array(prime)
countt = []
sumcount = 0
for i in range (1, 9):
    sumcount += i
    countt.append(sumcount)
i = np.array(countt)


print("(a) b =", a)
print("(b) c =", b)
print("(c) x =", c)
print("(d) y =", d)
print("(e) z =", e)
print("(f) w =", f)
print("(g) d =", g)
print("(h) e =", h)
print("(i) a =", i)

#EX3
print("3.")
print("Type num: ")
num = int(input())
x = np.logspace(1,n,n)
np.set_printoptions(formatter={'float':lambda x: f"10^{int(np.log10(x))}"})
print("Logarithmic", x)

#EX4
print("4.")
list_x  = [1, 2, 3]
list_y = [98, 12, 33]

list_z = list_x + list_y
print("z =", list_z)

#EX5
print("5.")
x = [1, 2, 3]
y = [4, 5, 6]
z = np.array([x,y])
print("Matrix z:", z)

#EX6
print("6.")
vec_x = np.arange(0, 22, 2)
print("a. first 6 ele:", vec_x[0:6])
print("b. last 5 ele:", vec_x[-5:])
print("c. 1st, 4th, and last ele", "[",vec_x[1],"]","[",vec_x[4],"]","[",vec_x[-1],"]")
print("d. 1st, 3rd, 5th, and 7th ele", "[",vec_x[1],"]","[",vec_x[3],"]","[",vec_x[5],"]","[",vec_x[7],"]")
print("e. Odd ele:", vec_x[1::2])
print("f. Even ele:", vec_x[0::2])

#EX7
print("7.")
vectorX = np.array([3, 11, -9, -131, -1, 1, -11, 91, -6, 407, -12, -11, 12, 153, 371])

maxX = max(vectorX)
print("a. Maximize:", maxX)

minX = min(vectorX)
print("b. Minimize", minX)

print("c. Index ele greater than 10:", vectorX[vectorX > 10])

print("d. Reverse a x vector:", np.flipud(vectorX))

sortx = sorted(vectorX)
print("e. Sort Ascending order:",sortx)

sortx_x = sorted(vectorX, reverse = True)
print("f. Sort descending order:",sortx_x)


