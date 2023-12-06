a = float(input())
A = float('%.2f'% a)
b = float(input())
B = float('%.2f'% b)

w1 = float(10*3.5/110)
w2 = float(10*7.5/110)

m = w1*A + w2*B
MEDIA = "%.5f" % m


print(f"MEDIA = {MEDIA}")