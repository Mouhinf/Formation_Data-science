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
 
def calculatrice() :
    b = int(input("Saisissez le premier nombre : "))
    return b
for op in operation.values() :
    print(op)
should_continue = True
while should_continue:
    op = input("Donner l'opérateur que vous choisissez pour le programme :")
    m = int(input("Donner le deuxieme numéro "))
    print(m)
    calculation_function = calculatrice()
    if op == "+" : 
        reponse = ajouter(calculation_function, m )
    if op == "-" :
        reponse = soustraire(calculation_function, m ) 
    if op == "x" : 
        reponse = multiplier(calculation_function, m )
    if op == "/" : 
        reponse = division(calculation_function, m )
    print(calculation_function, op, m,"="