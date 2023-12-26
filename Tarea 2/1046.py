x, y = input().split()
X = int (x)
Y = int (y)

if X == Y:
    print(f"O JOGO DUROU 24 HORA(S)")
if X > Y:
    res_1 = (24 - X) + Y
    print(f"O JOGO DUROU {res_1} HORA(S)") 
if X < Y:
    res_2 = Y - X 
    print(f"O JOGO DUROU {res_2} HORA(S)") 