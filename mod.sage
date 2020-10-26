#!/bin/sage

class Mod:
    def __init__(self, i, mod):
        self.i = i
        self.m = mod

    def __add__(self, o):
        if self.m != o.m:
            print("Modulus has to match")
            exit(-1)
        return Mod((self.i + o.i) % self.m, self.m)

    def __sub__(self, o):
        if self.m != o.m:
            print("Modulus has to match")
            exit(-1)
        return Mod((self.i - o.i) % self.m, self.m)

    def __mul__(self, o):
        if self.m != o.m:
            print("Modulus has to match")
            exit(-1)
        return Mod((self.i * o.i) % self.m, self.m)

    def __truediv__(self, o):
        if self.m != o.m:
            print("Modulus has to match")
            exit(-1)
        return Mod((pow(o.i, -1, o.m) * self.i) % self.m, self.m)

    def __pow__(self, o):
        return Mod(pow(self.i, o.i, o.m), self.m)

    def __xor__(self, o):
        return self.__pow__(o)

    def __str__(self):
        return f"Mod({self.i}, {self.m})"

