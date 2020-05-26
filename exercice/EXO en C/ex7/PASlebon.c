#include <stdio.h>
#include <stdlib.h>

int main(){

	int e, a, b, c, ab, ac, bc, abc;
	int somE, somA, somB, somC, somAB, somAC, somBC;

	printf("Diagramme de Venn a trois ensembles \n\n");

	printf("Entrer les donnees :\n");
	printf("A = ");
	scanf("%i", &a);
	printf("B = ");
	scanf("%i", &b);
	printf("C = ");
	scanf("%i", &c);
	printf("AB = ");
	scanf("%i", &ab);
	printf("AC = ");
	scanf("%i", &ac);
	printf("BC = ");
	scanf("%i", &bc);
	printf("ABC = ");
	scanf("%i", &abc);
	printf("E (Somme hors diagramme) = ");
	scanf("%i", &e);
	printf("\n");

	somAB = ab - abc;
	somAC = ac - abc;
	somBC = bc - abc;
	somA = a - (somAB + somAC + abc);
	somB = b - (somAB + somBC + abc);
	somC = c - (somAC + somBC + abc);
	somE = e - (somA + somB + somC + somAB + somAC + somBC + abc);

	printf("Resultats :\n");

	printf("A = %i \n", somA);
	printf("B = %i \n", somB);
	printf("C = %i \n", somC);
	printf("AB = %i \n", somAB);
	printf("AC = %i \n", somAC);
	printf("BC = %i \n", somBC);
	printf("ABC = %i \n", abc);
	printf("E (Somme hors diagramme) = %i \n", somE);

    system("pause");
    return 0;
}
