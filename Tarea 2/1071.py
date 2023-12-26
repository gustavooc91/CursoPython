x = input()
y = input()
try:
    X = int(x)
    Y = int(y)
except:
    print("Error")

L1 = [X,Y]
L1.sort()
L2 = list(range(L1[0]+1,L1[1]))
L3 = []

for i in L2:
    if i % 2 != 0:
        L3.append(i)

s = sum(L3)

print(f"{s}")