#

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Extended Euclidean to find inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

a = int(input("Enter a: "))
b = int(input("Enter b: "))
m = int(input("Enter m: "))

d = gcd(a, m)

if b % d != 0:
    print("No solution exists")
else:
    print("Solution exists")

    a1 = a // d
    b1 = b // d
    m1 = m // d

    inv = mod_inverse(a1, m1)

    x0 = (inv * b1) % m1

    print("One solution is: x =", x0)

    print("All solutions are:")
    for i in range(d):
        print("x =", x0 + i * m1)
