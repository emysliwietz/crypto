#!/bin/sage

from math import gcd
from copy import deepcopy

# start vector
start_vector = [25157, 17, 2]
N = 35533
ord_N = 35532


def passbyval(func):
    def new(*args):
        cargs = [deepcopy(arg) for arg in args]
        return func(*cargs)
    return new

def p(l):
    print(str(l).replace("[", "").replace("]", ""). replace(",", " &") + "\\\\")
    print("\hline")


@passbyval
def update_function(ll):
    l = ll
    if l[0] % 3 == 0:
        l[0] = (l[0]*3) % N
        l[1] = l[1] + 1 % ord_N
        l[2] = l[2] % ord_N
    elif l[0] % 3 == 1:
        l[0] = (l[0]*245) % N
        l[1] = l[1] % ord_N
        l[2] = l[2] + 1 % ord_N
    elif l[0] % 3 == 2:
        l[0] = (l[0]**2) % N
        l[1] = 2*l[1] % ord_N
        l[2] = 2*l[2] % ord_N
    else:
        print("Error")
        exit(-1)
    return l


def tortoise_crawl(l):
    p(f"Tortoise: {l}")
    return update_function(l)
  


def hare_hop(l):
    p(f"Hare: {l}")
    return update_function(update_function(l))


def hare_crawl(l):
    p(f"Hare: {l}")
    return update_function(l)


tortoise = tortoise_crawl(start_vector)
hare = hare_hop(start_vector)
print(f"{hare} {tortoise}")
while tortoise[0] != hare[0]:
    tortoise = tortoise_crawl(tortoise)
    hare = hare_hop(hare)
    if 1 < gcd(hare[0] - tortoise[0], N) < N:
        print(gcd(hare[0] - tortoise[0], N))
        print(f"{hare} {tortoise}")
        input()

print("Finding mu")
mu = 0
tortoise = start_vector
while tortoise[0] != hare[0]:
    tortoise = tortoise_crawl(tortoise)
    hare = hare_crawl(hare)
    mu += 1
    if 1 < gcd(hare[0] - tortoise[0], N) < N:
        print(gcd(hare[0] - tortoise[0], N))
        print(f"{hare} {tortoise}")
        input()

print(f"Found mu at {mu} with {hare} and {tortoise}")
b = tortoise[1] - hare[1]
c = hare[2] - tortoise[2]
print(f"Schoolbook a = {b}/{c} % {ord_N}")
