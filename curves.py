#!/usr/bin/env python3

from mod import Mod


class EdwardsCurve:
    def __init__(self, d, mod, f=1, a=1):
        """E = a*x^2 + y^2 = f + d*x^2*y^2."""
        self.mod = mod
        self.f = Mod(f, self.mod)
        self.d = Mod(d, self.mod)
        self.a = Mod(a, self.mod)

    def on_curve(self, p, quiet=False):
        (x, y) = p
        x = Mod(x, self.mod)
        y = Mod(y, self.mod)
        if not quiet:
            print(
                f"({x.i}, {y.i}): {self.a.i}*{(x^2).i} + {(y^2).i} = "
                f"{(self.a*(x ^ 2) + (y ^ 2)).i} = "
                f"{self.f.i} + {self.d.i} * {(x^2).i} * {(y^2).i} = "
                f"{(self.f + (self.d * (x ^ 2) * (y ^ 2))).i} (mod {self.mod})",
                end="",
            )
        if (self.a * (x ^ 2)) + (y ^ 2) == self.f + (self.d * (x ^ 2) * (y ^ 2)):
            if not quiet:
                print(" | on curve")
            return True
        else:
            if not quiet:
                print(" | not on curve")
            return False

    def points(self):
        i = 0
        for x in range(self.mod):
            x = Mod(x, self.mod)
            for y in range(self.mod):
                y = Mod(y, self.mod)
                if self.on_curve((x, y), quiet=True):
                    print(f"{str(i).zfill(2)} - ({x.i}, {y.i})")
                    i += 1

    def add(self, p, q):
        (x1, y1) = p
        x1 = Mod(x1, self.mod)
        y1 = Mod(y1, self.mod)
        (x2, y2) = q
        x2 = Mod(x2, self.mod)
        y2 = Mod(y2, self.mod)
        print(
            f"({x1.i}, {y1.i}) + ({x2.i}, {y2.i}) = "
            "("
            f"({x1.i}*{y1.i} + {x2.i}*{y2.i})"
            " / "
            f"({x1.i}*{x2.i} + {y1.i}*{y2.i}), "
            f"({x1.i}*{y1.i} - {x2.i}*{y2.i})"
            " / "
            f"({x1.i}*{y2.i} - {y1.i}*{x2.i})) = "
        )
        print(
            f"({(x1*y1 + x2*y2).i}/{(x1*x2 + y1*y2).i}, {(x1*y1 - x2*y2).i}/{(x1*y2 - y1*x2).i}) = "
        )
        x3 = ((x1 * y1) + (x2 * y2)) / ((x1 * x2) + (y1 * y2))
        y3 = ((x1 * y1) - (x2 * y2)) / ((x1 * y2) - (y1 * x2))
        print(f"({x3.i}, {y3.i})")

    def double(self, p):
        (x1, y1) = p
        x1 = Mod(x1, self.mod)
        y1 = Mod(y1, self.mod)
        print(f"2({x1.i}, {y1.i}) = ")
        print(
            f"(({x1.i} * {y1.i} * 2) / ({x1.i}^2 + {y1.i}^2), "
            f"({y1.i}^2 - {x1.i}^2) / (2 - {x1.i}^2 - {y1.i}^2)) = "
        )
        print(
            f"({(x1 * y1 * 2).i}/{(((x1 ^ 2) + (y1 ^ 2))).i}, "
            f"{((y1 ^ 2) - (x1 ^ 2)).i}/{(Mod(2, self.mod) - (x1 ^ 2) - (y1 ^ 2)).i}) = "
        )
        x3 = (x1 * y1 * 2) / ((x1 ^ 2) + (y1 ^ 2))
        y3 = ((y1 ^ 2) - (x1 ^ 2)) / (Mod(2, self.mod) - (x1 ^ 2) - (y1 ^ 2))
        print(f"({x3.i}, {y3.i})")

    def __str__(self):
        return f"{a}*x^2 + y^2 = {self.f} + {self.d}*x^2*y^2"


class Montgomery:
    def __init__(self, A, B, mod):
        """B*v^2 = u^3 + Au^2 + u"""
        self.A = Mod(A, mod)
        self.B = Mod(B, mod)
        self.mod = mod

    def __init__(self, E):
        """Convert from EdwardsCurve."""
        self.mod = E.mod
        self.A = ((E.a + E.d) * 2) / (E.a - E.d)
        print(f"A = 2({E.a.i}+{E.d.i}) / ({E.a.i} - {E.d.i}) = ")
        print(f"2({(E.a + E.d).i}) / {(E.a - E.d).i} = ")
        print(f"{((E.a + E.d)*2).i} / {(E.a - E.d).i} = ")
        print(f"{self.A.i}")
        four = Mod(4, self.mod)
        self.B = four / (E.a - E.d)
        print(f"B = 4/({E.a.i} - {E.d.i}) =")
        print(f"4 / {(E.a - E.d).i} =")
        print(f"{self.B.i}")

    def __str__(self):
        return f"{self.B.i}*v^2 = u^3 + {self.A.i}*u^2 + u"

    def on_curve(self, p, quiet=False):
        (u, v) = p
        u = Mod(u, self.mod)
        v = Mod(v, self.mod)
        if not quiet:
            print(
                f"({u.i}, {v.i}): {self.B.i}*{v.i}^2 ="
                f"{self.B.i}*{(v^2).i} ="
                f"{(self.B.i * (v^2)).i} ="
                f"{u.i}^3 + {self.A.i}*{u.i}^2 + {u.i} ="
                f"{(u^3).i} + {self.A.i}*{(u^2).i} + {u.i} ="
                f"{((u^3) + (self.A*(u^2)) + u).i} (mod {self.mod})",
                end="",
            )
        if self.B * (v ^ 2) == (u ^ 3) + (self.A * (u ^ 2)) + u:
            if not quiet:
                print(" | on curve")
            return True
        else:
            if not quiet:
                print(" | not on curve")
            return False

    def add(self, p, q):
        pass

    def double(self, p):
        pass

    def E2M(self, E, p):
        """Import point p=(x,y) from EdwardsCurve E."""
        if self.mod != E.mod:
            print("Curves have different modulus")
            return
        (x, y) = p
        x = Mod(x, self.mod)
        y = Mod(y, self.mod)
        one = Mod(1, self.mod)
        print(f"u = (1+{y.i})/(1-{y.i}) =")
        print(f"{(one + y).i}/{(one - y).i} =")
        u = (one + y) / (one - y)
        print(f"{u.i}")
        v = u / x
        print(f"v = {u.i}/{x.i} = {v.i}")


E = EdwardsCurve(11, 17)

E.on_curve((3, 7))

E.points()
print()
E.add((3, 7), (9, 6))
print()
E.double((3, 7))
print()
print("Montgomery")
M = Montgomery(E)
print()
print(M)
print()
M.E2M(E, (3, 7))
