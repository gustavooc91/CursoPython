p1 , pu1 , pp1 = input().split()
p2 , pu2 , pp2 = input().split()

P1 = int(p1)
PU1 = int(pu1)
PP1 = float(pp1)

P2 = int(p2)
PU2= int(pu2)
PP2 = float(pp2)

m1 = PU1 * PP1
M1 = float(m1)
m2 = PU2 * PP2
M2 = float(m2)

s = M1 + M2
S =  "{0:.2f}".format(s)

print (f"VALOR A PAGAR: R$ {S}")