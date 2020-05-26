#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

//fonction permetant de parcourir chacun des caractere de les transformer en valeur ascii puis de les
//crypter suivant la cle utiliser puis de convertir a nouveau le code ascii en lettres
void fonctCrypt(char* msg, int cle) {

	int i = 0;
	int block = 8;
	int msgInt;
	int msgIntCrypt;
	printf("Message crypte : ");

	while( msg[i] != NULL && strlen(msg)-1 > i) {
        //la premiere condition permette de transformer les espaces en 0
		if ((int)msg[i] == 32) {
			msgIntCrypt = 48;
		}
		else {
			msgInt = (((int)msg[i] - 'A'+ cle) % 26);
			if (msgInt >= 0) {
				msgIntCrypt = msgInt + 'A';
			}
			else{
				msgIntCrypt = ('Z' + 1 ) + ((int)msg[i] - 'A'+ cle);
			}
		}

		if ((i % block) == 0) {
			printf(" ");
		}
		printf("%c", (char)msgIntCrypt);
		i++;
	}

	if ((i % block) != 0) {
		while((i % block) != 0) {
			printf("0");
			i++;
		}
	}
	printf("\n");
}

//fonction permetant de parcourir chacun des caractere de les transformer en valeur ascii puis de les
//decrypter suivant la cle utiliser puis de convertir a nouveau le code ascii en lettres
void fonctDecrypt(char* msg, int cle){
	cle = cle - (cle*2); // inversion de l'entier

	int i = 0;
	int msgInt;
	int msgIntCrypt;
	printf("Message decrypte : ");
    //boucle permettant de parcourir chacun des caracteres et en meme temps faire des verification sur le message introduit
	while( msg[i] != NULL && strlen(msg)-1 > i){
        //la premiere condition permette de transformer les 0 en espace
		if ((int)msg[i] == 48) {
			msgIntCrypt = 32;
		}
		else {
			msgInt = (((int)msg[i] - 'A'+ cle) % 26);
			if (msgInt >= 0) {
				msgIntCrypt = msgInt + 'A';
			}
			else {
				msgIntCrypt = ('Z' + 1 ) + ((int)msg[i] - 'A'+ cle);
			}
		}

		printf("%c", (char)msgIntCrypt);
		i++;
	}
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

int main(void) {

	int cle = 0;
	char cryptDecrypt;
	char msg[80];

	printf("Entrez le message a crypter ou decrypter ? ");
	fgets(msg, sizeof(msg), stdin);
	fonctUpper(msg);
	printf("\n");

	printf("Pour crypter appuier sur (c) ou pour décrypter appuier sur (d) ? ");
	scanf("%c", &cryptDecrypt);
	printf("\n");

	printf("Rentrez la cle de de/cryptage : ");
	scanf("%i", &cle);
	printf("\n");

	//condition pour savoir si l application doit crypter ou decrypter
	if (cryptDecrypt == 'd') {
		fonctDecrypt(msg, cle);
	}
	else {
		fonctCrypt(msg, cle);
	}

	//permet a application de ne pas se couper en exe
    system("pause");
    return 0;
}
