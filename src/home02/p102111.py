"""import math
a=int(input("a: "))
b=int(input("b: "))
print(math.gcd(a,b))"""

#másik megoldás


def LKO(x, y):
    if x > y:
        kisebb = y
    else:
        kisebb = x
    for i in range(1, kisebb + 1):
        if ((x % i == 0) and (y % i == 0)):
            lko = i

    return lko

print(LKO(15,10))

