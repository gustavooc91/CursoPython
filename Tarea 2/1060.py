a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

# A = int(a)
# B = int(b)
# C = int(c)
# D = int(d)
# E = int(e)
# F = int(f)

L = [a,b,c,d,e,f]

L1 = []
for i in L:
    if i.isnumeric(): 
        I = int(i)
        L1.append(I)
L2 = []
for i in L1:
    if i > 0:
        L2.append(i)
cont = len(L2)
print(f"{cont} valores positivos") 