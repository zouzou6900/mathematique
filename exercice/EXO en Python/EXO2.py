#varible 
numberBloc = 8
#tableau de 26 caractere + 0
liste_lettre = ["A","B","C","D","E","F","G","H","I","J","k","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0"]

def pas(): 
    while True:
        try:
            value = abs(int(input('Entre un nombre positif : ')))
            if 0<value:
                while value>27:
                    value-=27
                if value == 27:
                    value-=1
                return value
            else:
                print('Entre un nombre superieur a zero')
        except ValueError:
            print('Erreur de saisie...')

def mode():
    while True:
        print('Voulez vous cryptez (c) ou decryptez (d) votre message?')
        mode = input().lower()
        if mode in 'c d'.split():
            return mode
        else:
            print('Entrez un choix "c" ou "d".')
            
def crypteMsg():
    while True:
        phrase=(input("Entrez votre message : ")).upper()
        phrase = phrase.replace(' ', '0')
        
        while len(phrase) % numberBloc != 0:
            phrase += '0'
        if 0 < len(phrase) <= 80:
            return phrase
        else:
            print("Entrez un message avec minimun 1 caratere et maximum 80 caracteres!!!")

def decrypteMsg():
    while True:
        phrase=(input("Entrez votre message : ")).upper()
        if 0 < len(phrase) <= 80:
            return phrase
        else:
            print("Entrez un message avec minimun 1 caratere et maximum 80 caracteres!!!")

def decoupe(seq):
    while seq:
        yield seq[:numberBloc]
        seq = seq[numberBloc:]

def decrypte(msg, key):
    pot=0-key
    #initalisation de tableau
    phrase_codee =[]
    msg = msg.replace(' ', '')
    msg=msg.replace('0',' ')
    phrase=msg.split()
    #boucle le tableau afin executer l action sur chaque lettre
    for mot in phrase:
        #inialisation de tableau transformation
        liste_mot=[]
        #on reutiliser la cle de la premiere boucle pour connaitre sa possition dans le tableau
        for lettre in mot:
            i = liste_lettre.index(lettre)
            if (i + pot) > 26:
                i-=27
            #on ajoute a la variable la lettre a laquelle est fait reference ex pas=2 a=1 dans le tableau (a+pas)=c
            liste_mot.append(liste_lettre[i+pot])
        #on recompose la phrase
        phrase_codee.append("".join(liste_mot))
    #on affiche le resultat du message
    print(" ".join(phrase_codee))

def crypte(msg, key):
    #initalisation de tableau
    phrase_codee =[]
    #boucle le tableau afin executer l action sur chaque lettre
    for mot in msg:
        #inialisation de tableau transformation
        liste_mot = []
        #condition si zero on ajoute 0
        if mot == '0':
            liste_mot.append(mot)
        #on reutiliser la cle de la premiere boucle pour connaitre sa possition dans le tableau
        for lettre in mot:
            i = liste_lettre.index(lettre)
            if (i + key) > 26:
                i-=27
            #on ajoute a la variable la lettre a laquelle est fait reference 
            # si elle est differente de zero elle rajoute 
            if mot != '0':
                liste_mot.append(liste_lettre[i+key])
        #on recompose la phrase
        phrase_codee.append("".join(liste_mot))
    #on affiche le resultat du message
    crypte=("".join(phrase_codee))
    #passe par la fonction decoupe pour l affichage par bloc de huit
    print(' '.join(list(decoupe(crypte))))

mode = mode()

if mode == 'c':
    msg = crypteMsg()
    value = pas()
    crypte(msg ,value)
else:
    msg = decrypteMsg()
    value = pas()
    decrypte(msg ,value)
