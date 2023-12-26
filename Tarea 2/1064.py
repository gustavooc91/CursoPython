a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

L = [a,b,c,d,e,f]

L1 = []
try:
    for i in L:
        I = float(i)
        L1.append(I)
except:
    pass

L2 = []
for i in L1:
    if i > 0:
        L2.append(i)

cont = len(L2)

s = sum(L2)

prom = s / float(cont)

p = round(prom , 1)

print(f"{cont} valores positivos") 
print(f"{p}")
