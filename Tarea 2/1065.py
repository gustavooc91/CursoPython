a = input()
b = input()
c = input()
d = input()
e = input()

L1 = [a,b,c,d,e]
L2=[]

try:
    for i in L1:
        I = int(i)
        if I%2==0:
            L2.append(i)

except:
    print("Error")
    
m = len(L2)
print(f"{m} valores pares")