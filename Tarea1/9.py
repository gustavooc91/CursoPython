# INPUT

n = input() #str

s = input()
S = float(s) 
S_2 = "{0:.2f}".format(S) # 2p float

v = input()
V = float(v) 
V_2 = "{0:.2f}".format(V) # 2p float

t = S + 0.15*V
T = "{0:.2f}".format(t) # 2p float

print(f"TOTAL = R$ {T}")