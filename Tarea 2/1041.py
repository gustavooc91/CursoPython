x, y = input().split()
X = float(x)
Y = float(y)

if X > 0 and Y > 0:
    print(f"Q1")
if X > 0 and Y < 0:
    print(f"Q4")
if X < 0 and Y < 0:
    print(f"Q3")
if X < 0 and Y > 0:
    print(f"Q2")
if X == 0 and Y == 0:
    print(f"Origem")
if X == 0 and Y != 0:
    print(f"Eixo Y")
if X != 0 and Y == 0:
    print(f"Eixo X")