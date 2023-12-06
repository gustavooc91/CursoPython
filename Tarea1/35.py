a, b ,c, d = input().split()

A = int(a)
B = int(b)
C = int(c)
D = int(d)

x = B > C
y = D > A
z = (C + D) > (A +B)
w = C > 0 and D > 0
v = A % 2 == 0

if x and y and z and w and v:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")