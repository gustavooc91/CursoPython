a = input("Dia ")
B = input().split()
c = input("Dia ")
D = input().split()

if a.isnumeric():
    L1 = [int(a)]
else:
    L1 = []

if c.isnumeric():
    L2 = [int(c)]

else:
    L2 = []

for i in B:
    try:   
        I = int(i)
        L1.append(I)
    except:
        if i.isnumeric():
            L1.append(0)
        else:
            pass

for i in D:
    try:   
        I = int(i)
        L2.append(I)
    except:
        if i.isnumeric():
            L2.append(0)
        else:
            pass
if len(L1) == 4 and len (L2) == 4:
    C1 = 24*60*60*L1[0] + 60*60*L1[1] + 60*L1[2] + L1[3]
    C2 = 24*60*60*L2[0] + 60*60*L2[1] + 60*L2[2] + L2[3]
else:
    for i in L1:
        if len(L1) < 4:
            L1.append(0)
    for i in L2:
        if len(L2) < 4:
            L2.append(0)
    
    C1 = 24*60*60*L1[0] + 60*60*L1[1] + 60*L1[2] + L1[3]
    C2 = 24*60*60*L2[0] + 60*60*L2[1] + 60*L2[2] + L2[3]


cr = C2 - C1

CR = float (cr)

P = CR // 86400
PM = CR / 86400 - P
p = int(P)

H = PM * 24
HR = round(H)
HM = H - HR
h = int (HR)

M = HM * 60
MR = round(M)
MM = M - MR
m = int (MR)

S = MM * 60
SR = round(S)
SM = S - SR
s = int (SR)


# print(B)
# print(D)
# print(L1)
# print(L2)
# print(C1, C2, CR)
# print(P, PM, p)
# print(H, HR, HM, h)
# print(M, MR, MM, m)
# print(S, SR, SM, s)

print(f"{p} dia(s)")
print(f"{h} hora(s)")
print(f"{m} minuto(s)")
print(f"{s} segundo(s)")