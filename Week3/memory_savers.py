"""Lamda"""
# variabila = lambda x, y : x + y
# print(variabila(1, 2))
# def variabila_desfasurat(x, y):
#     return x + y
#
# players = [{"prenume": "Ion", "nume": "Popescu", "varsta": 32},
#            {"prenume": "Ana", "nume": "Badea", "varsta": 33},
#            {"prenume": "Ileana", "nume": "Oancea", "varsta": 12}]
# sortare = sorted(players, key=lambda player: player[varsta])

"""map"""
# lista1 = [1, 5, 4, 6, 8, 11, 3, 12]
# lista3 = map(lambda x: x*2, lista1)
# print(list(lista3))

"""zip"""
# list_with_int = [1, 2, 3, 4, 5]
# list_with_str = ("one", "two", "three", "four", "five")
# result = zip(list(list_with_int, list_with_str))

"""lista scrisa pe un singur rand"""
list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [i for i in list1 if i%2 == 0]
# list2 = [i if i%2 == 0 else 0 for i in list1]
# list2 = []
# for x in range(10):
#     if x % 2 == 0:
#         if x %5 == 0:
#             list2.append(x)
# list2 = [x for x in range(50) if x %2 == 0 if x % 5 == 0]
# print(list2)
dictionar = {}
for num in range(1, 11):
    dictionar[num] = num * num
dictionar2 = {num : num* num for num in range(1, 11) }
print(dictionar)