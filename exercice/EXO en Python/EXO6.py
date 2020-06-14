# libraries
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import numpy as np

#initialisation tableau
tab=[]

#verifie le nombre
def verifNombre():
    while True:
        try:
            value = abs(int(input('Entre un nombre positif : ')))
            if 0<value:
                return value
            else:
                print('Entre un nombre superieur a zero')
        except ValueError:
            print('Erreur de saisie...')

#verifie n que le nombre soit pair si oui rajoute dans le tableau A
def verifA(n):
    if (n % 2) == 0:
       print("{0} est Paire".format(n))
       tab.append("A")
    else:
       pass

#verifie n que le nombre soit divisible par 6 si oui rajoute dans le tableau B
def verifB(n):
    if (n % 6) == 0:
       print("{0} est un multiple de 6".format(n))
       tab.append("B")
    else:
       pass

#verifie n que le nombre multiplier par 9 est inférieur a 139 si oui rajoute dans le tableau C
def verifC(n):
    if (n * 9) > 139:
       print("{0} le nombre * 9 est superieur a 139".format(n))
       tab.append("C")
    else:
       pass

#verifie que le tableau est remplie ou sinon le nombre est hors diagramme
def verifD(tab):
    if not tab:
        print("Le nombre {0} est hors diagramme".format(valeur))
    else:
        pass

#pour connaitre la position dans le diagramme
def position(tab):
    if tab == 'A':
        print('100')
    if tab == "B":
        print("010")
    if tab == "C":
        print("001")
    if tab == "AB":
        print("110")
    if tab == "AC":
        print("101")
    if tab == "BC":
        print("011")
    if tab == "ABC":
        print("111")

#question bonus voir le diagramme
def getModeGraph():
    while True:
        print('Voulez vous voire la representation graphique? o/n :')
        mode = input().lower()
        if mode in 'o n'.split():
            return mode
        else:
            print('Entrez un choix "o" ou "n".')

#phrase d'entre
print('Diagramme de Venn compose de trois ensembles.\nGroupe A : Le nombre doit etre pairs.\nGroupe B : Le nombre doit etre un multiples de 6.\nGroupe C : Le nombre * 9 doit etre superieur a 139.')

#verification du nombre
valeur = verifNombre()
verifA(valeur)
verifB(valeur)
verifC(valeur)

#affichage
print("L'ensemble appartient a :")
print("".join(tab))
print("Indice bonus :")
rep=("".join(tab))
position(rep)

#bonus graphique
mode = getModeGraph()
if mode == "o":
    bonus=input("Entre la valeur Bonus")
    # Make a Basic Venn
    v = venn3(subsets=( 1, 1, 1, 1, 1, 1, 1 ), set_labels = ('A', 'B', 'C'))

    # Custom it
    #v.get_patch_by_id('100').set_alpha(1.0)
    v.get_patch_by_id('100').set_color('white')
    v.get_patch_by_id('101').set_color('white')
    v.get_patch_by_id('110').set_color('white')
    v.get_patch_by_id('111').set_color('white')
    v.get_patch_by_id('001').set_color('white')
    v.get_patch_by_id('011').set_color('white')
    v.get_patch_by_id('010').set_color('white')
    v.get_label_by_id('100').set_text(' ')
    v.get_label_by_id('101').set_text(' ')
    v.get_label_by_id('110').set_text(' ')
    v.get_label_by_id('111').set_text(' ')
    v.get_label_by_id('001').set_text(' ')
    v.get_label_by_id('011').set_text(' ')
    v.get_label_by_id('010').set_text(' ')
    v.get_label_by_id('A').set_text('A : le nombre est pairs')
    v.get_label_by_id('B').set_text('B : le nombre doit etre multiples de 6')
    v.get_label_by_id('C').set_text('C : le nombre doit etre superieur a 139')
    c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

    # Add title and annotation
    plt.title("Sample Venn diagram")

    plt.annotate(valeur, xy=v.get_label_by_id(bonus).get_position() - np.array([0, 0.05]), xytext=(-70,-70),
             ha='center', textcoords='offset points', bbox=dict(boxstyle='round,pad=0.5', fc='gray', alpha=0.1),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='red'))

    # Show it
    plt.show()
else:
    print("Une prochaine fois peut-etre.")
