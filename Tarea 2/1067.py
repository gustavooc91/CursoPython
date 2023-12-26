x = input()
try:
    X = int(x)
except:
    print("Error")

if X <= 1000 and X >= 1:
    L1 = list(range(X + 1))
    for i in L1:
        if i % 2 != 0:
            print (i)