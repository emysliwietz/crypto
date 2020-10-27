#!/bin/sage

xes = []

l = [3, 1, 0]

def p(l):
    print(str(l).replace("[", "").replace("]", ""). replace(",", " &") + "\\\\")
    print("\hline")


while True:
    p(l)
    xes += [l[0],]
    if l[0] % 3 == 0:
        l[0] = (l[0]*3) % 1013
        l[1] = l[1] + 1
        l[2] = l[2]
    elif l[0] % 3 == 1:
        l[0] = (l[0]*245) % 1013
        l[1] = l[1]
        l[2] = l[2] + 1
    elif l[0] % 3 == 2:
        l[0] = (l[0]**2) % 1013
        l[1] = 2*l[1]
        l[2] = 2*l[2]
    else:
        print("Error")
    if l[0] in xes:
        p(l)
        print("Found")

        
        exit(-1)
