"""
r (read, vine cu valoarea asta default, daca fisierul nu exista apare eroare),
w (write, daca fisierul nu exista il adauga, daca exista ceva deja scris suprascrie continutul)
a (append pe randul urmator, nu apare eroare daca fisierul nu exista)
r+ (pt scriere si citire, eroare daca nu exista)
"""
# file = open('data2.txt', "r+")
# file.write("hello2")
# file.close()

# file = open('data1.txt', "r")
# try:
#     file.write("hello")
# finally:
#     file.close()
# with open('data.txt', 'a') as file:
#     file.write('hello\n')
#     file.write('hello3\n')
#     file.write('hello2')

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
    # for line in list(file):
        # print(line)

with open('data.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)