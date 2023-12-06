a, b ,c = input().split()

A = int(a)
B = int(b)
C = int(c)

M_AB = int((A+B+abs(A-B))/2)

M_AC = int((A+C+abs(A-C))/2)

if M_AB > M_AC:
    L = M_AB
elif M_AC > M_AB:
    L = M_AC
elif M_AB == M_AC:
    L = M_AB

print (f"{L} e o maior")