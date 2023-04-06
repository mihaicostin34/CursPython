a = 2
b = 3
rezultat = 0
while a<10:
    print("ana are mere")
    a +=1

for i in range(0, 10, 2):
    print(f"Instr {i}")

lista = [9, 8, 7]
dictionar = {1: 'a', 2: 'b', 3: 'c'}

for index, value in enumerate(dictionar.items()):
    print(f"key: {index}, value: {value}")

for i in lista:
    print(i)