#fonction inialisation polynom
def polynom(d = int):
    p = [0]*(int(d) + 1)
    for i in range(0,(int(d) + 1)):
        print("Votre indice pour X ^",i," :")
        p[i] = input()
    return p

#fonction opérations sur les polynoms
def operation(A = list, B = list, S = str):
    tab = []
    if len(A)>len(B): tab = [float(0)]*len(A)
    else: tab = [float(0)]*len(B)
    if S == "+":
        for i in range(len(A)):
            tab[i] += A[i]
        for i in range(len(B)):
             tab[i] += B[i]
    elif S == "-":
        for i in range(len(A)):
            tab[i] += A[i]
        for i in range(len(B)):
            tab[i] -= B[i]
    elif S == "*":
        for i in range(len(A)):
            tab[i] += A[i]
        for i in range(len(B)):
            tab[i] = A[i] * B[i]
    else: print("Sélectionné un caractère parmie les propositions pour effectuer une opération.")
    return tab

#affichage de l'équation
def affichage(p = list):
    for i in range(len(p)):
        print("",symbole(p[i]),p[i],"X ^",i, end="")

#fonction changer le symbole
def symbole(s = float):
    if (float(s) >= 0):
        symb = "+"
    else:
        symb = ""
    return symb

#phrase d'entre
print("Les polynomes : choisis parmie les opérations suivantes :\n + pour addition\n - pour soustraction\n * pour multiplication")

#initialisation de variable
#choix d operation
signe = input("Choisis ton opérations : ")

#premier polynome
degre = input("Quelle est le degré du polynome : ")
polynom = polynom(degre)
polynomFloat = list(map(float, polynom))

#affichage du premier polynome
print("Votre premier polynome :", polynomFloat)

#deuxième polynome
degre2 = input("Quelle est le degré du deuxieme polynome : ")
polynom2 = polynom(degre2)
polynomFloat2 = list(map(float, polynom2))

#affichage du deuxième polynome
print("Votre deuxieme polynome :", polynomFloat2)

#affichage du resultat de l'opération
print("Résultat de l'opération :", operation(polynomFloat, polynomFloat2, signe))

#affichage sous forme d'équation
print("Affichage sous forme d'équation :")
affichage(operation(polynomFloat, polynomFloat2, signe))
