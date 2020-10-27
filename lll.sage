#!/bin/sage

e = 3
N = 529774210762246675161318616746995617835565246251635147
c = 221742016667880335235086977604419933217657946219108301
a = Integer("myfavoritenumberis000000", base=35)
X = Integer("xxxxxx", base=35)


M = Matrix([
    [X^3, 3*X^2*a, 3*X*a^2, a^3-c],
    [0, N*X^2, 0, 0],
    [0, 0, N*X, 0],
    [0,0,0, N]
])

#print(M.LLL())
B = M.LLL()
Q1 = (B[0][0]*(x^3/X^3))
Q2 = B[0][1]*(x^2/X^2)
Q3 = B[0][2]*(x/X)
Q4 = B[0][3]

print(B)
print()
print(Q1)
print(Q2)
print(Q3)
print(Q4)
Q = Q1 + Q2 + Q3 + Q4
print(Q.roots(ring=ZZ))


