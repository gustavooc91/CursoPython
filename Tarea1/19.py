n = input()
N = int(n)

h = N // 3600
m, s = divmod(N, 60)
M = m % 60
print(f"{h}:{M}:{s}")