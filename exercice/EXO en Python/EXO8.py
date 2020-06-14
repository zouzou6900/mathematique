# libraries
import numpy as np
from math import *

#verification de X n'est pas une lettre
def verifX():
    while True:
        try:
            value = abs(int(input('Entrez la valeur du coefficient de X : ')))
            return value
        except ValueError:
            print('Erreur de saisie...')

#verification de Y n'est pas une lettre
def verifY():
    while True:
        try:
            value = abs(int(input('Entrez la valeur du coefficient de Y : ')))
            return value
        except ValueError:
            print('Erreur de saisie...')

#verification de R n'est pas une lettre
def verifR():
    while True:
        try:
            value = abs(int(input('Entrez la valeur de la somme : ')))
            return value
        except ValueError:
            print('Erreur de saisie...')

#fonction cree pour resoudre l'équation grace a la fonction matrix de np
def inconnues(a, b, c, aa, bb, cc):
    x = np.matrix([[a, b], [aa, bb]])
    Y = np.matrix([[c], [cc]])
    solution = x.I * Y
    return solution

#fonction changer le symbole
def symbole(s = float):
    if (float(s) >= 0):
        symb = "+"
    else:
        symb = ""
    return symb

#phrase d'entre
print('Equations a deux inconnues.')
a = verifX()
b = verifY()
c = verifR()
print('Equation(1) :', ceil(a) ,'X', symbole(b), ceil(b),'Y = ', ceil(c))
aa = verifX()
bb = verifY()
cc = verifR()
print('Equation(2) :', ceil(aa) ,'X',symbole(bb), ceil(bb),'Y = ', ceil(cc))
resultat = inconnues(a, b, c, aa, bb, cc)
print('Resultat :\nX = {0}\nY = {1}'.format(ceil(resultat[0,0]),ceil(resultat[1,0])))
