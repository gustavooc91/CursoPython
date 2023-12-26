x = input()
try:
    X = int(x)
except:
    print("Error")

L1 = L1 = list(range(X,X + 12))

for i in L1:
    if i % 2 != 0:
        print (i)