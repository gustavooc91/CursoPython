n = input()
L1 = []
L2 = []
L3 = []
L4 = []

try:
    N = int(n)
    L1 = list(range(1,N+1))
    if N < 10000:
        for i in L1:
            x = int(input())
            L2.append(x)
except:
    print("Error")
    
for i in L2:
    if i <= 20 and i >= 10:
        L3.append(i)
    elif i > 20 or i < 10:
        L4.append(i)

l1 = len(L3)
l2 = len(L4)

print(L1)
print(f"{l1} in")
print(f"{l2} out")