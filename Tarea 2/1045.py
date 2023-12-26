x, y, z = input().split()
X = float (x)
Y = float (y)
Z = float (z)

L1 = [X, Y, Z]

L1.sort(reverse=True)

A = L1[0]
B = L1[1]
C = L1[2]

if A >= B + C :
    print(f"NAO FORMA TRIANGULO")
elif A**2 == B**2 + C**2:
     print(f"TRIANGULO RETANGULO")
elif A**2 > B**2 + C**2:
     print(f"TRIANGULO OBTUSANGULO")
elif A**2 < B**2 + C**2:
     print(f"TRIANGULO ACUTANGULO")
else:
    pass

if A == B and A == C:
    print(f"TRIANGULO EQUILATERO")
elif A == B or A == C or B == C:
    print(f"TRIANGULO ISOSCELES")