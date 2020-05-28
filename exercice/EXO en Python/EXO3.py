import math, random, sys

valMin = 10
valMax = 1000
d = 0.1
charge = 5
msgEncrypte = 0
msgDecrypte = 0

def getMode():
    while True:
        print('Voulez vous cryptez votre message? o/n :')
        mode = input().lower()
        if mode in 'o n'.split():
            return mode
        else:
            print('Entrez un choix "o" ou "n".')

def msg():
     message = input("Entrez le message : ")
     return message

def verif(nombre):
    for i in range(2, int(math.sqrt(nombre)+1)):
        if nombre % i == 0:
            return False
    return nombre>1

def generateKey():
    global p, q, e, r
    p = random.choice([k for k in range(valMin, valMax) if verif(k)])
    q = random.choice([k for k in range(valMin, valMax) if (verif(k)) & (k != p)])
    e = random.choice([k for k in range(valMin, valMax) if (verif(k)) & (k > p) & (k > q)])
    r = p * q
    return (e, r)

def decrypteKey(p, q, e):
    z = (p - 1) * (q - 1)
    n = 1
    global d
    while d != int(d):
        d = ((z * n) + 1)/ e
        n += 1
    return d

def encrypte(message, keyE, keyR):
    global msgEncrypte
    msgEncrypte = ((message ** keyE) % keyR)
    return msgEncrypte

def listeEncrypte(liste, keyE, keyR):
    detailListeEncripte = [encrypte(x, keyE, keyR) for x in liste]
    return detailListeEncripte

def decrypt(messageToDecrypt, keyR, keyD):
    global msgDecrypte
    msgDecrypte = ((messageToDecrypt ** keyD) % keyR)
    return msgDecrypte

def listeDecrypte(liste, keyR, keyD):
    detailListeDecrypte = [decrypt(c, keyR, keyD) for c in liste]
    return detailListeDecrypte

def getOrd(message):
    messageList = list(message)
    resultat = [ord(c) for c in messageList]
    return resultat

def getChr(message):
    recompose = [chr(l) for l in message]
    resultat = "".join(recompose)
    return resultat

mode = getMode()

if mode == "o":
    generateKey()
    print("Vos clés RSA générées aléatoirement : (",e,",",r,")")
    message = msg()
    if (len(message) <= 80):
        messageAscii = getOrd(message)
        print("Votre message est passer par la fonction ord du tableau ascii :\n", messageAscii)
        msgEncrypte = listeEncrypte(messageAscii, e, r)
        print("Votre message encrypté avec la cle :\n", msgEncrypte)
        decrypteKey(p, q, e)
        print("Votre clé de decryptage est :",int(d),"\nVeuillez attendre la fin du chargement.")
        sys.stdout.write("[%s]" % (" " * charge))
        sys.stdout.flush()
        sys.stdout.write("\b" * (charge+1))
        for i in range(charge):
            msgDecrypte = listeDecrypte(msgEncrypte, r, int(d))
            sys.stdout.write("*")
            sys.stdout.flush()
        sys.stdout.write("]\n")
        print("Votre message décrypté :\n", msgDecrypte)
        messageChr = getChr(msgDecrypte)
        print("Votre message est passer par la fonction chr du tableau ascii :\n", messageChr)
    else:
        print("Le message dépasse 80 caractères.")
else:
    print("Une prochaine foix peut-etre.")
