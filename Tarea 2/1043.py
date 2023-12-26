x,y,z = input().split()

X = float(x)
Y = float(y)
Z = float(z)

xz = X + Z
xy = X + Y
yz = Y + Z

if xz > Y and xy > Z and yz > X:
    per = X+Y+Z
    P = "{0:.1f}".format(per)
    print(f"Perimetro = {P}")
else:
    area = (X+Y)*Z/2
    A = "{0:.1f}".format(area)
    print(f"Area = {A}")