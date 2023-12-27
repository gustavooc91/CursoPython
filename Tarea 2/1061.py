A = input().split()
B = input().split()
C = input().split()
D = input().split()

L1 = []
L2 = []

try:
    for i in A:
        if i.isdigit():
            a = int(i)
            L1.append(a)
except:
        pass
    
try:
    for i in C:
        if i.isdigit():
            c = int(i)
            L2.append(c)
except:
    pass
    
try:
    for i in B:
        if i != ":":
            b = int(i)
            L1.append(b)
except:
    pass
        
try:
    for i in D:
        if i != ":":
            d = int(i)
            L2.append(d)
            
except:
    pass

print(L1)
print(L2)

C1 = 86400*L1[0] + 3600*L1[1] + 60*L1[2] + L1[3]
C2 = 86400*L2[0] + 3600*L2[1] + 60*L2[2] + L2[3]

CR = C2 - C1

P = CR // 86400
PM = CR % 86400

H = PM // 3600
HM = PM  % 3600

M = HM // 60

S = HM % 60

print(f"{P} dia(s)")
print(f"{H} hora(s)")
print(f"{M} minuto(s)")
print(f"{S} segundo(s)")
