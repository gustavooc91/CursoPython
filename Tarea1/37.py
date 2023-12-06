
a = (input())

A = float (a)

v = A < 0 or A > 100

w = A >= 0 and A <= 25

x = A > 25 and A <= 50

y = A > 50 and A <= 75

z = A > 75 and A <= 100

if v:
    print("Fora de intervalo")

elif w:
    print("Intervalo [0,25]")
    
elif x:
    print("Intervalo (25,50]")
    
elif y:
    print("Intervalo (50,75]")    
    
elif z:
    print("Intervalo (75,100]")