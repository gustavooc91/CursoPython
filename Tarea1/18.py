n = input()
N = int(n)

if 0 < N < 1000000:
    
    t1, t1_r = divmod(N, 100000)
    T1= int(t1*1000)
    
    t2 = t1_r // 10000
    t2_r = t1_r % 10000
    T2= int(t2*100)
    
    t3 = t2_r // 1000
    t3_r = t2_r % 1000
    T3= int(t3*10)
    
    t4 = t3_r // 100
    t4_r = t3_r % 100
    T4= int(t4*1)
    
    t5 = t4_r // 50
    t5_r = t4_r % 50
    T5= int(t5*1)
    
    t6 = t5_r // 20
    t6_r = t5_r % 20
    T6= int(t6*1)
    
    t7 = t6_r // 10
    t7_r = t6_r % 10
    T7= int(t7*1)
    
    t8 = t7_r // 5
    t8_r = t7_r % 5
    T8= int(t8*1)
    
    t9 = t8_r // 2
    t9_r = t8_r % 2
    T9= int(t9*1)
    
    t10 = t9_r // 1
    t10_r = t9_r % 1
    T10= int(t10*1)
    
    B100 = T1+T2+T3+T4
    B50 = T5
    B20 = T6
    B10 = T7
    B5 = T8
    B2 = T9
    B1 = T10
    
    print("NOTAS")
    print(f"{B100} nota(s) de R$ 100.00")
    print(f"{B50} nota(s) de R$ 50.00")
    print(f"{B20} nota(s) de R$ 20.00")
    print(f"{B10} nota(s) de R$ 10.00")
    print(f"{B5} nota(s) de R$ 5.00")
    print(f"{B2} nota(s) de R$ 2.00")
    print(f"{B1} nota(s) de R$ 1.00")
    

