x = input ()
X = float(x)

def func(n):
    g = 0.01*n*X
    G = "{0:.2f}".format(g)
    sum = g + X
    SUM = "{0:.2f}".format(sum)
    N = str(n)
   
    print(f"Novo salario: {SUM}")
    print(f"Reajuste ganho: {G}")
    print(f"Em percentual: {N} %")
    
    

if X > 0 and X <= 400.00:
    func(15)

if X > 400.00 and X <= 800.00:
    func(12)
    
if X > 800.00 and X <= 1200.00:
    func(10)
    
if X > 1200.00 and X <= 2000.00:
    func(7)
    
if X > 2000.00:
    func(4)