c_1 = input()
c_2 = input()
c_3 = input()

D = [c_1, c_2, c_3]
    
if "vertebrado" in D:
        
    if "ave" in D:
        if "carnivoro" in D:
            print(f"aguia")
        elif "onivoro" in D:
            print(f"pomba")
        else:
            print(f"Error")
                
    if "mamifero" in D:
        if  "onivoro" in D:
            print(f"homem")
        elif "herbivoro" in D:
            print(f"vaca")
        else:
            print(f"Error")
            
            
elif "invertebrado" in D:
    if "inseto" in D:
            
        if "hematofago" in D:
            print(f"pulga")
        elif "herbivoro" in D:
            print(f"lagarta")
        else:
            print(f"Error")

    if "anelideo" in D:
        if "hematofago" in D:
            print(f"sanguessuga")
        elif "onivoro" in D:
            print(f"minhoca")
        else:
            print(f"Error")



