n=3.14159
N="{0:.6f}".format(n)
N2=float(N)

r=float(input())
R = "{0:.2f}".format(r)
R2 = float(R) # 2p float

a = N2*(r**2)
A = "{0:.4f}".format(a) # 2p float

print(f"A={A}")
