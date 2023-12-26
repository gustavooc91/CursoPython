n = input()
N = int(n)

L1 = [61, 71, 11, 21, 32, 19, 27, 31]
L2 = ["Brasilia", "Salvador", "Sao Paulo", "Rio de Janeiro", "Juiz de Fora", "Campinas", "Vitoria", "Belo Horizonte"]

if N in L1:
    i = L1.index(N)
    c = L2[i]
    print(f"{c}")
    
else:
    print(f"DDD nao cadastrado")