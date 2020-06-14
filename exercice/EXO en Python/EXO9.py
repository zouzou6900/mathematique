# libraries
import numpy as np

#fonction cree pour resoudre l'équation grace a la fonction matrix de np
def equation(a, b, c, d, e, f, g, h, i, j, k, l):
    A = np.matrix([ [a, b, c],
                    [e, f, g],
                    [i, j, k]])
    B = np.matrix([[d], [h], [l]])
    resultat = A.I * B
    return resultat

#fonction changer le symbole
def symbole(s = float):
    if (float(s) >= 0):
        symb = "+"
    else:
        symb = ""
    return symb

#phrase d'entre
print('Equations a trois inconnues :\nVeuillez entrer les valeurs')

#variable de X, Y, Z des trois équations
a = float(input('de X pour la première équation: '))
b = float(input('de Y pour la première équation: '))
c = float(input('de Z pour la première équation: '))
d = float(input('La somme de la première équation : '))
a2 = float(input('de X pour la seconde équation: '))
b2 = float(input('de Y pour la seconde équation: '))
c2 = float(input('de Z pour la seconde équation: '))
d2 = float(input('La somme de la seconde équation : '))
a3 = float(input('de X pour la troisième équation: '))
b3 = float(input('de Y pour la troisième équation: '))
c3 = float(input('de Z pour la troisième équation: '))
d3 = float(input('La somme de la troisième équation : '))

#affichage des équations
print('Première équation :',a,'X',symbole(b),b,'Y',symbole(c),c,'X = ',d)
print('Seconde équation :',a2,'X',symbole(b2),b2,'Y',symbole(c2),c2,'X = ',d2)
print('Troisème équation :',a3,'X',symbole(b3),b3,'Y',symbole(c3),c3,'X = ',d3)

#resultat des equations passer a la fonction pour les resoudres
resultat = equation(a, b, c, d, a2, b2, c2, d2, a3, b3, c3, d3)
#affichage resultat
print('X, Y et Z ont été résolu :\nX = ',resultat[0,0],'\nY = ',resultat[1,0],'\nZ = ',resultat[2,0])
