#!/usr/bin/env python

from mod import Mod

p = 821
q = 701
e = 2 ** 16 + 1

n = p * q
phi_n = (p - 1) * (q - 1)
e = Mod(e, phi_n)
d = e ^ -1


print(f"public key is (n, e) = ({n}, {e.i})")
print(f"private key is (n, d) = ({n}, {d.i})")
if d * e == 1:
    print("Correct")
else:
    print("d is bullshit")


def encrypt(m):
    if isinstance(e, int):
        return (Mod(m, n) ^ e).i
    else:
        return (Mod(m, n) ^ e.i).i


def decrypt(c):
    if isinstance(e, int):
        return (Mod(c, n) ^ d).i
    else:
        return (Mod(c, n) ^ d.i).i


n = 374861
e = 5
d = 149453
c = 153497

print(decrypt(153497))

if encrypt(decrypt(c)) == c:
    print("Correct")
