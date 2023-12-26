a = input()
b = input()
c = input()
d = input()
e = input()

L1 = [a,b,c,d,e]
L2 = []
L3 = []
L4 = []
L5 = []

try:
    for i in L1:
        I = int(i)
        if I%2==0:
            L2.append(i)
except:
    print("Error")
    
try:
    for i in L1:
        I = int(i)
        if I%2!=0:
            L3.append(i)
except:
    print("Error")    

try:
    for i in L1:
        I = int(i)
        if I > 0:
            L4.append(i)
except:
    print("Error")

try:
    for i in L1:
        I = int(i)
        if I < 0:
            L5.append(i)
except:
    print("Error")


m = len(L2)
n = len(L3)
o = len(L4)
p = len(L5)

print(f"{m} valor(es) par(es)")
print(f"{n} valor(es) impar(es)")
print(f"{o} valor(es) positivo(s)")
print(f"{p} valor(es) negativo(s)")