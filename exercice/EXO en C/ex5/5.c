#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

	int a, b, c;
	double delta;

	printf("Equation du second degre \n");

	printf("Veillez entrer A : ");
	scanf("%i", &a);
	printf("\n");
	printf("Veillez entrer B : ");
	scanf("%i", &b);
	printf("\n");
	printf("Veillez entrer C : ");
	scanf("%i", &c);
	printf("\n");
    // formule = b2 - 4ac
	delta = pow(b,2) - 4.0*a*c;
    //condition permettant de savoir si delta et superieur ou inferieur ou egal a 0
	if (delta<0) {
	    printf("Pas de solution.\n");
	}
	else if (delta==0) {
        //  formule -b / 2 * a
        //  %.4f = permet d avoir 4 chiffre apres la virgule
	    printf("Solution  :\n");
	    printf(" x =  %.4f\n", (double)-b/(2*a));
    }
	else {
	    //  formule -b (+ ou - ) racine carre de delta / 2 * a
	    printf("Solutions :\n");
	    printf(" x1 = %.4f\n", (-b+sqrt(delta))/(2*a));
	    printf(" x2 = %.4f\n", (-b-sqrt(delta))/(2*a));
    }

    //permet a application de ne pas se couper en exe
	system("pause");
    return 0;


}
