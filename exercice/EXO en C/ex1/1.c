#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
//fonction de cryptage ou decryptage
void fonctCrypt(char* msg, int cle) {

	int i = 0;
	int msgInt;
	int msgIntCrypt;
	printf("Resultat : \n");
    //boucle permetant de parcourir chacun des caractere de les transformer en valeur ascii puis de les
    //crypter ou ( decrypter si valeur negatif ) suivant la cle utiliser puis de convertir a nouveau le code ascii en lettres
	while( msg[i] != NULL && strlen(msg)-1 > i){

        msgInt = (((int)msg[i] - 'A'+ cle) % 26);
		if (msgInt >= 0) {
			msgIntCrypt = msgInt + 'A';
		}
        else {
			msgIntCrypt = ('Z' + 1 ) + ((int)msg[i] - 'A'+ cle);
		}

        msg[i] = (char)msgIntCrypt;
        i++;
	}
	printf("%s", msg);
	printf("\n");
}
//fonction permetant de mettre les caractère en majuscule
void fonctUpper(char text[]) {
   int cp = 0;

   while (text[cp] != NULL) {
      if (text[cp] >= 'a' && text[cp] <= 'z') {
         text[cp] = text[cp] - 32;
      }
      cp++;
   }
}

int main(void){

	int cle = 0;
	char msg[80];

	printf("Entrez le message a crypter ou a decrypter ? ");
	fgets(msg, sizeof(msg), stdin);
	fonctUpper(msg);

	printf("Entrez un nombre pour la cle (Entrez ce nombre en negatif pour decrypter) ? ");
	scanf("%i", &cle);
	printf("\n");

	fonctCrypt(msg, cle);

    //permet a application de ne pas se couper en exe
    system("pause");
    return 0;
}
