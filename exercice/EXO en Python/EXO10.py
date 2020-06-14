# libraries
import numpy as np

#verification de value soit un entier compris en 1 et 4 et qui ne soit pas une lettre
def operation():
    while True:
        try:
            value = int(input('Veuillez choisir votre opération : '))
            if(1<= value <= 4):
                return value
            else:
                print('Erreur de saisie... Veuillez entre un nombre entre 1 et 4 pour choisir votre opération')
        except ValueError:
            print('Erreur de saisie...Entre un nombre pour choisir votre opération')

#verification de value soit un entier et qui ne soit pas une lettre
def verifValue():
    while True:
        try:
            value = abs(int(input('Entrez la valeur : ')))
            return value
        except ValueError:
            print('Erreur de saisie...Entre un nombre')

#fonctione boucle pour initalise les matrices
def creationMatrix(l, c):
    a = np.arange(l * c).reshape(l , c)
    i = 0
    while i < l:
        j = 0
        while j < c:
            print("colonne :", j + 1 ," et ligne : ", i + 1)
            value = verifValue()
            a[i][j] = value
            j += 1
        i += 1
    return a

#fonction d'affichage des opérations de matrices
def affichageMatrix(symbole, matrice, matrice2 = 1, scalar = 1):
    print(matrice)
    if symbole == 1 :
        print("+")
        result = matrice + matrice2
        print(matrice2)
    elif symbole == 2 :
        print("*")
        result = matrice * matrice2
        print(matrice2)
    elif symbole == 3 :
        print("*")
        result = matrice * scalar
        print(scalar)
    elif symbole == 4 :
        result = np.transpose(matrice)
        print("Votre matrice :\n", matrice,"\nVotre matrice transposée : ")
    if  symbole <= 3 :
        print("=")
    print(result)

#phrase d'entre
print("1. Addition de deux matrices\n2. Multiplication de deux matrices\n3. Multiplication d'une matrice par un scalaire\n4. Transposition d'une matrice")
#choix d'opération
symbole = operation()
#si l'operation existe
if symbole :
    print("Lignes : ")
    l = verifValue()
    print("Colonnes : ")
    c = verifValue()
    matrice = creationMatrix(l, c)
    if symbole < 3 :
        print("Deuxième matrice : ")
        matrice2 = creationMatrix(l, c)
        if symbole == 1 :
            affichageMatrix(1, matrice, matrice2)
        elif symbole == 2 :
            affichageMatrix(2, matrice, matrice2)
    elif symbole == 3 :
        print("Scalaire : ")
        scalar = verifValue()
        affichageMatrix(3, matrice, scalar = scalar)
    elif symbole == 4 :
        affichageMatrix(4, matrice)
