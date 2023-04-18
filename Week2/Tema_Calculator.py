state = 0
val_1 = 0
val_2 = 0
operator = ""

def sum(a, b):
    return a + b

def dif(a, b):
    return a - b

def div(a, b):
    if b != 0:
        return a/b
    else:
        return positive_infinity

def mult(a, b):
    return a * b

while True:
    if state == 0:
        val_1 = int(input("Primul numar: "))
        state +=1
    elif state == 1:
        operator = input("Operator: ")
        if operator == "C":
            print("Stergere")
            state = 0
        else:
            state+=1
    elif state == 2:
        val_2 = input("Al doilea numar")
        if val_2 == "C":
            print("Stergere")
            state = 1
        else:
            val_2 = int(val_2)
            if operator == "+":
                print(sum(val_1, val_2))
                state = 0
            elif operator == "-":
                print(dif(val_1, val_2))
                state = 0
            elif operator == "*":
                print(mult(val_1, val_2))
                state = 0
            else:
                print(div(val_1, val_2))
                state = 0


