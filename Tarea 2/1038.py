F_0 = ["CODE", "SPECIFICATION", "PRICE"]
F_1 = ["1", "Cachorro Quente", "4.00"]
F_2 = ["2", "X-Salada", "4.50"]
F_3 = ["3", "X-Bacon", "5.00"]
F_4 = ["4", "Torrada Simples", "2.00"]
F_5 = ["5", "Refrigerante", "1.50"]


I1 = int(F_1[0])
I2 = int(F_2[0])
I3 = int(F_3[0])
I4 = int(F_4[0])
I5 = int(F_5[0])


P1 = float(F_1[2])
P2 = float(F_2[2])
P3 = float(F_3[2])
P4 = float(F_4[2])
P5 = float(F_5[2])

pc, q = input().split()
PC = int(pc)
Q = int(q)

if PC == I1:
    c1 = Q*P1
    C1= "{0:.2f}".format(c1)
    print(f"Total: R$ {C1}")
elif PC == I2:
    c2 = Q*P2
    C2= "{0:.2f}".format(c2)
    print(f"Total: R$ {C2}")
elif PC == I3:
    c3 = Q*P3
    C3= "{0:.2f}".format(c3)
    print(f"Total: R$ {C3}")
elif PC == I4:
    c4 = Q*P4
    C4= "{0:.2f}".format(c4)
    print(f"Total: R$ {C4}")
elif PC == I5:
    c5 = Q*P5
    C5= "{0:.2f}".format(c5)
    print(f"Total: R$ {C5}")