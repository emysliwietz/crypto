#!/usr/bin/env python


class Mod:
    def __init__(self, i, mod):
        if isinstance(i, Mod):
            self.i = i.i % mod
        else:
            self.i = i % mod
        self.m = mod

    def __add__(self, o):
        if isinstance(o, int):
            o = Mod(o, self.m)
        if self.m != o.m:
            print(f"Modulus has to match: {self} + {o}")
            exit(-1)
        return Mod((self.i + o.i) % self.m, self.m)

    def __sub__(self, o):
        if isinstance(o, int):
            o = Mod(o, self.m)
        if self.m != o.m:
            print(f"Modulus has to match: {self} - {o}")
            exit(-1)
        return Mod((self.i - o.i) % self.m, self.m)

    def __mul__(self, o):
        if isinstance(o, int):
            o = Mod(o, self.m)
        if self.m != o.m:
            print(f"Modulus has to match: {self} * {o}")
            exit(-1)
        return Mod((self.i * o.i) % self.m, self.m)

    def __truediv__(self, o):
        if isinstance(o, int):
            o = Mod(o, self.m)
        if self.m != o.m:
            print(f"Modulus has to match: {self} / {o}")
            exit(-1)
        return Mod((pow(o.i, -1, o.m) * self.i) % self.m, self.m)

    def __pow__(self, o):
        if isinstance(o, int):
            o = Mod(o, self.m)
        return Mod(pow(self.i, o.i, o.m), self.m)

    def __xor__(self, o):
        return self.__pow__(o)

    def __str__(self):
        return f"Mod({self.i}, {self.m})"

    def __eq__(self, o):
        if isinstance(o, int):
            return self.i == (o % self.m)
        else:
            return self.i == o.i and self.m == o.m

    def __neg__(self):
        return Mod(0, self.m) - self

    def ord(self):
        for i in range(1, self.m):
            a = self ^ i
            if a == 1:
                return i
        print("Error finding order")


if __name__ == "__main__":
    g = Mod(2, 35533)
    print(g.ord())
