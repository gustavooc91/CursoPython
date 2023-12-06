l_km = float(12) # km/l

t = input()
T = float(t) # h
v = input()
V = float(v) # km/h

d = V*T # km

l = d/l_km # l
L = "{0:.3f}".format(l)

print(f"{L}")