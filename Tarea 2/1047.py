w, x, y, z = input().split()
W = int (w)
X = int (x)
Y = int (y)
Z = int (z)


if X == Z:
    if W == Y:
        print(f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
        
    elif W > Y:
        res_1 = (24 - W) + Y
        print(f"O JOGO DUROU {res_1} HORA(S) E 0 MINUTO(S)")
    
    elif W < Y:
        res_2 = Y - W
        print(f"O JOGO DUROU {res_2} HORA(S) E 0 MINUTO(S)") 
        
if X > Z:    
    if W >= Y:
        res_3 = (60 - X) + Z
        res_4 = (23 - W ) + Y
        
        print(f"O JOGO DUROU {res_4} HORA(S) E {res_3} MINUTO(S)")
    
    elif W < Y:
        res_5 = (60 + Z) - X
        res_6 = Y - (W + 1)
        
        print(f"O JOGO DUROU {res_6} HORA(S) E {res_5} MINUTO(S)")    
    
if X < Z:    
        
    if W > Y:      
        res_7 = W - Y
        res_8 = X - Z
        
        print(f"O JOGO DUROU {res_7} HORA(S) E {res_8} MINUTO(S)")
    
    elif W <= Y:
        res_9 = Z - X
        res_10 = Y - W
        
        print(f"O JOGO DUROU {res_10} HORA(S) E {res_9} MINUTO(S)")    