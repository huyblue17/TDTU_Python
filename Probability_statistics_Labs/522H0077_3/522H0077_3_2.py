import itertools
from fractions import Fraction

S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'), ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

#A Student named Thanh
A = []
for student in S:
    if student[0] == 'Thanh':
        A.append(student)

#Gender female
B = []
for student in S:
    if student[1] == 'Nữ':
        B.append(student)

#A ∩ B: Student's name is Thanh and is female
A_B = []
for student in S:
    if student[0] == 'Thanh' and student[1] == 'Nữ':
        A_B.append(student)


#Probabilities
P_A = Fraction(len(A), len(S))
P_B = Fraction(len(B), len(S))
P_A_B = Fraction(len(A_B), len(S))

#prob Thanh is female
P_Thanh_fm = P_A_B / P_B

# Print the results
print("a.Event A (Student's name is Thanh):", A)
print("b.Event B (Student is female):", B)
print("c.Event A_B: ", A_B)
print("d1..Prob Event A (P(A)): ", P_A)
print("d2.Prob Event B (P(B)): ", P_B)
print("d3.Prob P(A_B): ", P_A_B)
print("e.Prob named Thanh is femmale: ", P_Thanh_fm)
