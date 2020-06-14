#class object
class Arbre:
    #initialisation de l'arbre
    def __init__(init, value):
        init.data = value
        init.left = None
        init.right = None
        init.parent = None

    #affichage de l'arbre
    def affichage(aff, niv=0):
        if aff.right:
            aff.right.affichage(niv + 1)
        print(f"{' ' * 4 * niv}{aff.data}")
        if aff.left:
            aff.left.affichage(niv + 1)

    #placement des noeuds
    def dataInsert(move, value):
        if value <= move.data:
            if move.left is None:
                move.left = Arbre(value)
                move.left.parent = move
            else:
                move.left.dataInsert(value)
        elif value > move.data:
            if move.right is None:
                move.right = Arbre(value)
                move.right.parent = move
            else:
                move.right.dataInsert(value)

#phrase d'entre
print('Arbre binaire.')

#initialisation de variable
arbre = int(input("Entre le nombre d'element que doit contenir l'arbre : "))
nombre = int(input("Entre le nombre de noeuds que doit contenir l'arbre : "))

new = Arbre(arbre)
i = 0

#boucle pour le nombre de noeuds
while i < nombre:
    listeNombre = int(input("Entrer un nombre : "))
    new.dataInsert(listeNombre)
    i += 1

#affichage de l'object
new.affichage()
