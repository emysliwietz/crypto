#!/usr/bin/env python3

a = int(input("Enter a: "))
b = int(input("Enter b: "))

A = [a, 1, 0]
B = [b, 0, 1]
C = [0, 0, 0]

while B[0] != 0:
    C[0] = A[0] - int(A[0] / B[0]) * B[0]
    C[1] = A[1] - int(A[0] / B[0]) * B[1]
    C[2] = A[2] - int(A[0] / B[0]) * B[2]
    print(
        (str(A) + " & " + str(B) + " & " + str(C)).replace("[", "(").replace("]", ")")
        + "\\\\"
    )
    A[0] = B[0]
    A[1] = B[1]
    A[2] = B[2]
    B[0] = C[0]
    B[1] = C[1]
    B[2] = C[2]
print((str(A) + " & " + str(B) + " & ").replace("[", "(").replace("]", ")") + "\\\\")
