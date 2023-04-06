lista = [8, -2, 's', 3.1, 8, "Ana are mere", None, [1, 2, 3, [4, 5, 6]]]
print(len(lista))
print(lista.index(0))
print(len(lista))
print(lista[-1])
print(lista[0:8])
print(lista[3:])
print(lista[:4])
print(lista[0:7:2])
lista.append(5)
print(lista)
lista.insert(2, 6)
lista[3] = 7
lista.clear()
print(type(lista))

