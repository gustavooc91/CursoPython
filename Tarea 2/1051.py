s = input()
S = float(s)

def imp (p, s, r):
    if s > 2000.00 and s > 0:
        P = 0.01*p
        S = s - r
        T = S*P
        return T       


if S <= 2000.00 and S > 0:
    
    print (f"Isento")
    
if S > 2000.00 and S <= 3000.00:
    
    i = imp(8, S, 2000.00)
    
    I = "{0:.2f}".format(i)
    print(f"R$ {I}")
    
elif S > 3000.00 and S <= 4500.00:
    
    i1 = .08*1000
    i2 = imp(18, S, 3000.00)

    I = i1 + i2
    
    Ir = "{0:.2f}".format(I)
    print(f"R$ {Ir}")

elif S > 4500.00:
    i1 = .08*1000
    i2 = .18*1500
    i3 = imp(28, S, 4500.00)

    I = i1 + i2 + i3
    
    Ir = "{0:.2f}".format(I)
    print(f"R$ {Ir}")