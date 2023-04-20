import random
from lista_cuvinte import cuvinte_de_ghicit as lista_cuv
# cuvant = "onomatopee"
cuvant = random.choice(lista_cuv).lower()
cuvant_initial = list(cuvant)
litera_incercata = input("Alege o litera: ")
for index, value in enumerate(cuvant_initial):
    if cuvant_initial[0]!=value and cuvant_initial[-1]!=value:
        cuvant_initial[index] = '_'
print("".join(cuvant_initial))
numar_incercari = 1
set_litere_incercate = set()
while numar_incercari<=3:
    litera_incercata = input("Alege o litera: ").lower()
    if litera_incercata in cuvant and litera_incercata not in set_litere_incercate:
        for index, value in enumerate(cuvant):
            if litera_incercata == value:
                cuvant_initial[index] = litera_incercata
    else:
        if litera_incercata in set_litere_incercate:
            print("Ai incercat deja litera aceasta")
        else:
            set_litere_incercate.add(litera_incercata)
            numar_incercari+=1
            if numar_incercari>3:
                print("Pierdut")
                print(cuvant)
                break
    if '_' not in cuvant_initial:
        print("Ai castigat")
        break
    else:
        print(f"Mai ai {3-numar_incercari} incercari")
    print("".join(cuvant_initial))