#inialisation tableau de lettres 26 lettre + un blanc
liste_lettre=["A","B","C","D","E","F","G","H","i","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
#variable bolean 
continuer = True
#boucle qui verifier tant que le message qu il a au moin un caratère et maximun 80 
while continuer:
    #variable qui stock le message transforme en minuscule
    phrase=(input("Entre votre phrase : ")).upper()
    #supression des espace en debut et en fin
    trim=phrase.strip()
    #nombres de caratère
    lent=len(trim)
    #si le nombre est plus grand que zero
    if lent>0:
        #si le nombre est inferrieur ou egal a 80
        if lent<=80:
            #on arrete la boucle  
            continuer = False
            #variable qui stock le pas 
            pas=int(input("Entre un nombre positif pour crypte(Entre un nombre negatif pour decrypter) : "))
    else:
        True
while pas>27:
    pas-=27
#inialisation tableau de la phrase a coder ou decoder
phrase_codee=[]
#decoupage de la phrase dans un tableau
phrase=phrase.split()
#boucle le tableau afin executer l action sur chaque lettre
for mot in phrase:
    #inialisation de tableau transformation
    liste_mot=[]
    #on reutiliser la cle de la premiere boucle pour connaitre sa possition dans le tableau
    for lettre in mot:
        i=liste_lettre.index(lettre)
        if i+pas>26:
            i-=27
        #on ajoute a la variable la lettre a laquelle est fait reference ex pas=2 a=1 dans le tableau (a+pas)=c
        liste_mot.append(liste_lettre[i+pas])
    #on recompose la phrase
    phrase_codee.append("".join(liste_mot))
#on affiche le resultat du message
print(" ".join(phrase_codee))