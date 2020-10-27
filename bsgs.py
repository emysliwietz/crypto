#!/usr/bin/env python

from math import ceil, sqrt


def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {}
    for i in range(N):
        bs = pow(g, i, p)
        tbl[bs] = i
        print(f"Baby step {str(i).zfill(3)} - Mod({g}^{i}, {p}) = {bs}")


    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        print(f"Giant step {str(j).zfill(3)} - Mod({h} * {c}^{j}, {p}) = {y}")
        if y in tbl:
            ret = j * N + tbl[y]
            print(f"Found match at {j}:\nBaby step = {tbl[y]}\nGiant step = {y}\n{j} * {N} + {tbl[y]} = {ret}")
            return ret

    # Solution not found
    return None


print(bsgs(7894352216, 355407489, 604604729))
