#!/usr/bin/env python

from mod import Mod

p = 673
q = 557
c = 153497
e = 5

n = p * q
phi_n = (p - 1) * (q - 1)


print(f"n = {n}")
print(f"phi_n = {phi_n}")

dp = Mod(e, p - 1) ^ -1
dq = Mod(e, q - 1) ^ -1
qinv = Mod(q, p) ^ -1

print(f"dp = 1/e (mod p-1) = 1/{e} (mod {p-1}) = {dp.i}")
print(f"dq = 1/e (mod q-1) = 1/{e} (mod {q-1}) = {dq.i}")
print(f"qinv = 1/q (mod p) = 1/{q} (mod {p}) = {qinv.i}")

mp = Mod(c, p) ^ dp
mq = Mod(c, q) ^ dq
h = Mod(qinv * Mod(mp.i - mq.i, p), p)
m = Mod(mq.i + h.i, n) * q

print(f"mp = c^dp (mod p) = {c}^{dp.i} (mod {p}) = {mp.i}")
print(f"mq = c^dq (mod q) = {c}^{dq.i} (mod {q}) = {mq.i}")
print(f"h = qinv * (mp - mq) (mod p) = {qinv.i} * ({mp.i} - {mq.i}) (mod {p}) = {h.i}")
print(f"m = mq + h*q (mod n) = {mq.i} + {h.i}*{q} (mod {n}) = {m.i}")
