def ajouter(a, b) :
    return (a + b)

def soustraire(a, b) :
    t = a - b
    return t

def multiplier(a, b) : 
    m = a * b
    return m

def division(a, b) :
    d = a / b
    return d

operation = {ajouter : "+", soustraire : "-", multiplier : "x", division : "/"} 
 
def calculatrice(a) :
    int(input("Saisissez le premier nombre : "))

for op in operation.values() :
    print(op)

while op == "+" or op == "-" or op == "/" or op == "x" :
    op = input("Donner l'opérateur que vous choisissez pour le programme :")
    n = int(input("Donner le deuxieme numéro "))
    calculation_function = calculatrice(n)
    



