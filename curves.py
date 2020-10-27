#!/usr/bin/env python3

from mod import Mod


class EdwardCurve:
    def __init__(self, f, g, mod):
        """E = x^2 + y^2 = f + g*x^2*y^1."""
        self.mod = mod
        self.f = Mod(f, self.mod)
        self.g = Mod(g, self.mod)

    def on_curve(self, p, quiet=False):
        (x, y) = p
        x = Mod(x, self.mod)
        y = Mod(y, self.mod)
        if not quiet:
            print(
                f"({x.i}, {y.i}): {(x^2).i} + {(y^2).i} = "
                f"{((x ^ 2) + (y ^ 2)).i} = "
                f"{self.f.i} + {self.g.i} * {(x^2).i} * {(y^2).i} = "
                f"{(self.f + (self.g * (x ^ 2) * (y ^ 2))).i} (mod {self.mod})",
                end="",
            )
        if (x ^ 2) + (y ^ 2) == self.f + (self.g * (x ^ 2) * (y ^ 2)):
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


E = EdwardCurve(1, 11, 17)

E.on_curve((3, 7))

E.points()
print()
E.add((3, 7), (9, 6))
print()
E.double((3, 7))
