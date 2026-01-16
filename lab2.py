#division algorithm
a = int(input("Enter value of a (dividend): "))
b = int(input("Enter value of b (divisor): "))

q = a // b      # Quotient
r = a % b       # Remainder

print("According to Division Algorithm:")
print("a =", a, "=", b, "*", q, "+", r)
print("Quotient =", q)
print("Remainder =", r)
