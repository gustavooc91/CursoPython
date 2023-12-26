x, y = input().split()
X = int(x)
Y = int(y)

xy = X % Y

yx = Y % X

if xy == 0 or yx == 0:
    print(f"Sao Multiplos")
else:
    print(f"Nao sao Multiplos")