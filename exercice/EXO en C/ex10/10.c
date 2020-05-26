#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(){

	double x1, y1, z1, c1, x2, y2, z2, c2, x3, y3, z3, c3;
	double coef, x, y, z;

	printf("Systemes de trois tableau a trois inconnues \n\n");

	printf("Veillez entrer X, Y et Z et la constante de la premiere equation :\n");
	printf("X : ");
	scanf("%lf", &x1);
	printf("Y : ");
	scanf("%lf", &y1);
	printf("Z : ");
	scanf("%lf", &z1);
	printf("Constante : ");
	scanf("%lf", &c1);
	printf("\n");

	printf("Veillez entrer X, Y et Z et la constante de la deuxieme equation :\n");
	printf("X : ");
	scanf("%lf", &x2);
	printf("Y : ");
	scanf("%lf", &y2);
	printf("Z : ");
	scanf("%lf", &z2);
	printf("Constante : ");
	scanf("%lf", &c2);
	printf("\n");

	printf("Veillez entrer X, Y et Z et la constante de la troisieme equation :\n");
	printf("X : ");
	scanf("%lf", &x3);
	printf("Y : ");
	scanf("%lf", &y3);
	printf("Z : ");
	scanf("%lf", &z3);
	printf("Constante : ");
	scanf("%lf", &c3);
	printf("\n");

	coef = (-1 * x2 / x1 );

    x2 = (coef * x1) + x2;
    y2 = (coef * y1) + y2;
    z2 = (coef * z1) + z2;
    c2 = (coef * c1) + c2;

	coef = (-1 * x3 / x1);

    x3 = (coef * x1) + x3;
    y3 = (coef * y1) + y3;
    z3 = (coef * z1) + z3;
    c3 = (coef * c1) + c3;

	coef = (-1 * y3 / y2);

    x3 = (coef * x2) + x3;
    y3 = (coef * y2) + y3;
    z3 = (coef * z2) + z3;
    c3 = (coef * c2) + c3;


	z = c3 / z3;
	y = (c2 - (z2 * z)) / y2;
	x = (c1 - ((y1 * y) + (z1 * z))) / x1;

	printf("Solutions :\n");
	printf("X vaut %.2f \n", x);
	printf("Y vaut %.2f \n", y);
	printf("Z vaut %.2f \n", z);

	system("pause");
    return 0;
}
