a = float(input())
A = float('%.1f'% a)
b = float(input())
B = float('%.1f'% b)
c = float(input())
C = float('%.1f'% c)

w_a = float(2/10)
w_b = float(3/10)
w_c = float(5/10)

m = w_a*A + w_b*B + w_c*C
MEDIA = "%.1f" % m


print(f"MEDIA = {MEDIA}")