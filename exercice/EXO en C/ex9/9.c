#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

	double x1, y1, c1, x2, y2, c2, x, y, resultat;

	printf("Systemes de deux equations a deux inconnues \n\n");

	printf("Veillez entrer X, Y et la constante de la premiere equation :\n");
	printf("X : ");
	scanf("%lf", &x1);
	printf("Y : ");
	scanf("%lf", &y1);
	printf("Constante : ");
	scanf("%lf", &c1);
	printf("\n");

	printf("Veillez entrer X, Y et la constante de la seconde equation :\n");
	printf("X : ");
	scanf("%lf", &x2);
	printf("Y : ");
	scanf("%lf", &y2);
	printf("Constante : ");
	scanf("%lf", &c2);
	printf("\n");

	// sert a enlever les X de l equation
    // formule (X (1equation) * Y (2 equation)) - (X (2equation) * Y (1 equation))
    resultat =  x1 * y2 - x2 * y1;
    //formule (Y (1equation) * constantente (2 equation)) - (Y (2equation) * constantente (1 equation)) / par
    x = (y1 * c2 - y2 * c1) / resultat;
    //formule (constantente (1 equation) * X (2equation)) - (constantente (2 equation) * X (1equation))/ par
    y = (c1 * x2 - c2 * x1) / resultat;

    if (resultat == 0){
        printf ("Aucune solution.\n");
    }
    else{
		printf("X vaut %.2f \n", x);
		printf("Y vaut %.2f \n", y);
    }

	system("pause");
    return 0;
}
