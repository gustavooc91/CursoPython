a , b , c = input().split()
pi = 3.14159
A = float(a)
B = float(b)
C = float(c)

t = float(A*C/2)
T = ("{0:.3f}".format(t))

ci = float(pi*(C**2))
CI = ("{0:.3f}".format(ci))

tr  = float((A+B)*C/2)
TR = ("{0:.3f}".format(tr))

cu  = float(B**2)
CU = ("{0:.3f}".format(cu))

r  = float(A*B)
R = ("{0:.3f}".format(r))


print(f"TRIANGULO: {T}")
print(f"CIRCULO: {CI}")
print(f"TRAPEZIO: {TR}")
print(f"QUADRADO: {CU}")
print(f"RETANGULO: {R}")
