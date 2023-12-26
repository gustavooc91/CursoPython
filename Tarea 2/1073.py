n = input()
L1 = []
L2 = []
L3 = []
L4 = []

try:
    N = int(n)
    L1 = list(range(1,N+1))
    if N < 2000 and N > 5:
        for i in L1:
            if i % 2 == 0 and i > 0:
                L2.append(i)
except:
    print("Error")

for i in L2:
    s = i**2
    print(f"{i}^2 = {s}")