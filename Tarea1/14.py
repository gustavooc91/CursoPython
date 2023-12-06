x=input()
y=input()

X = int(x) #km
Y = float(y) #l

r = X /Y
R = "{0:.3f}".format(r)

print(f"{R} km/l")