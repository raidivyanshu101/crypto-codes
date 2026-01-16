#
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None

a = int(input("Enter a: "))
n = int(input("Enter n: "))

if gcd(a, n) != 1:
    print("Modular inverse does not exist")
else:
    inv = mod_inverse(a, n)
    print("Modular inverse of", a, "mod", n, "is:", inv)
