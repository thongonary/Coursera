#!/usr/bin/python

import math

def getN(x):
    return len(str(x))

def karatsuba(x,y):
    if getN(x) < 2 or getN(y) < 2:
            return (x*y)
    else:
        m = getN(x)/2
        a = x/(10**m)
        b = x - a*(10**m)
        c = y/(10**m)
        d = y - c*(10**m)
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        adbc = karatsuba(a+b,c+d)-ac-bd
        return ((10**(2*m))*ac + (10**m)*(adbc) + bd)
        
x = input("Enter x: ")
y = input("Enter y: ")

print karatsuba(x,y)
