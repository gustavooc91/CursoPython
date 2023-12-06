a, b ,c = input().split()

A = float(a)
B = float(b)
C = float(c)


if A == 0:
        print("Impossivel calcular")
    
if A!=0 :
    
    det = ((B**2)-4*A*C)
    
    x1=(-B+(det)**(1/2))/(2*A)
   
    x2=(-B-(det)**(1/2))/(2*A)
       
    X1 = "{0:.5f}".format(x1)
    
    X2 = "{0:.5f}".format(x2)
    
    if det < 1 :
        print("Impossivel calcular")
 
    else:
        print(f"R1 = {X1}")
        print(f"R2 = {X2}")