import math as mti

x1, y1 = input().split()
x2, y2 = input().split()

X1 = float(x1)
Y1 = float(y1)

X2 = float(x2)
Y2 = float(y2)

e =  float((X2 - X1)**2 + (Y2 - Y1)**2)
r = e**(1/2)

R = "{0:.4f}".format(r)

print(R)
