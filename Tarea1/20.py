i = input()
I = int(i)

a, a_r = divmod(I, 365)

m = a_r // 30
m_r = a_r % 30

d = m_r

print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")