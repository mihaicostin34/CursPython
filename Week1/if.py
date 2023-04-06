a = 2
b = 3
c = 4
d = 0
mesaj = "a egal cu b"
if a < b and (d := a+b):
    mesaj = "a mai mic decat b"
elif a > c and (d := a-b):
    mesaj = "a mai mare ca b"
elif a < c and (d := a+c):
    mesaj = "a mai mic decat c"
print(mesaj, d)
rez = a if a < b else b
