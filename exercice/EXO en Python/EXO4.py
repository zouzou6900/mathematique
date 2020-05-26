from math import sqrt

#fonction valeur A 
def valeurA(): 
    while True:
        try:
            valeurA = int(input('Entre une valeur a : '))
            if valeurA != 0 :
                return valeurA
            else:
                print('Entre un nombre supérieur a zéro pour la valeur A.')
        except ValueError:
            print('Erreur de saisie...')
 
#fonction qui va calculer le delta (Δ = b²-4ac)
def deltaCalcule(a = float, b = float, c = float):
    global delta
    delta = (float(b) * float(b)) - (4 * float(a) * float(c)) 
    return delta

#fonction Si Δ > 0 il y adeux solutions qui sont x1 = (-b-√Δ)/(2a) et x2= (-b+√Δ)/(2a)
def deltaPlus(a = float, b = float, c = float, delta = float):
    resultat = ( - float(b) + sqrt(delta) ) / ( 2 * a )
    resultat1 = ( - float(b) - sqrt(delta) ) / ( 2 * a )
    return resultat, resultat1

#foncton Si Δ = 0, il y aune seule solution à l'équation : c'est x= -b/(2a)
def deltaZero(a = float, b = float):
    divise = ( - float(b) ) / (2 * float(a) )
    return divise

#fonction changer le symbole 
def symbole(s = float):
    if (float(s) >= 0):
        symb = "+"
    else:
        symb = ""
    return symb

#initialisation des variables 
valeurA = valeurA()
valeurB = float(input("Entre la valeur b : "))
valeurC = float(input("Entre la valeur c : "))
delta = float

#affichage de l'équation
print("Résultat de l'équation : ",valeurA,"x²",symbole(valeurB),valeurB,"x",symbole(valeurC),valeurC," = 0 \n Δ : ", deltaCalcule(valeurA, valeurB, valeurC))
#si le delta est inferieur a zéro 
if (delta < 0):
    print("Aucune solution réels. Le delta est négatif.")
#si le delta est égal
elif (delta == 0):
    print("Le delta est nul, une solution \n Résultat : ", deltaZero(valeurA, valeurB))
#si le delta est supérieur 
else:
    print("Le delta est positif, deux solutions \n Résultat : ", deltaPlus(valeurA, valeurB, valeurC, delta))
         