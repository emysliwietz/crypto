#!/usr/bin/env python

from mod import Mod

p = 35533
g = Mod(2, p)
ord_g = 35532
if ord_g == g.ord():
    print("Order correct")

a = Mod(2101, p)
ha = g ^ a
print(f"Ha: {ha}")

hb = Mod(11245, p)
b = 0
for i in range(p):
    if g ^ i == hb:
        b = i

hab = hb ^ a
print(f"Shared key is {hab}")
hba = ha ^ b
if hab == hba:
    print("Correct")
else:
    print(f"Someone fucked up: other shared key is {hba}")
