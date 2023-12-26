n = input()
N = int(n)

M1 = [1,2,3,4,5,6,7,8,9,10,11,12]
M2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if N in M1:
    i = M1.index(N)
    R = M2[i]
    print(f"{R}")
else:
    print(f"Error")