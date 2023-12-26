n1 , n2 , n3 , n4 = input().split()
N1=float(n1)
N2=float(n2)
N3=float(n3)
N4=float(n4)

sum = (2*N1+3*N2+4*N3+1*N4)
prom =  (sum/10)
P = "{0:.1f}".format(prom)

print(f"Media: {P}")

if prom >= 7:
    print(f"Aluno aprovado.")
    
elif prom < 5:
    print(f"Aluno reprovado.")
    
elif prom <= 6.9 and prom >= 5:
    
    print(f"Aluno em exame.")
    
    e = input()
    E = float (e)
    
    print(f"Nota do exame: {E}")
    
    prom2 = (E+prom)/2
    
    if prom2 >= 5:
        print(f"Aluno aprovado.")
    elif prom2<= 4.9:
        print(f"Aluno reprovado.")
    
    print (f"Media final: {prom2}")