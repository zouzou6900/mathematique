#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

int main() {

	int nombre = 1;
	char *a;
	char *b;
	char *c;

	printf("diagramme de Venn compose de trois ensembles. \n");
	printf("A Le nombres doit etre pairs \n");
    printf("B Le nombre doit etre un multiples de 6 \n");
    printf("C Le nombre * 9 doit etre superieur a 139 \n");
	printf("\n");

	while(1) {

		printf("Nombre a verifier : ");
		scanf("%i", &nombre);

		if ((nombre%2) == 0) {
           a = "A";
		}
		else {
            a = "";
		}

        if ((nombre%6) == 0) {
            b = "B";
        }
		else {
            b = "";
		}

		if ((nombre * 9) > 139) {
		    c = "C";
		}
		else {
            c = "";
		}

        if ((a=="") && (b=="") && (c=="")) {
            printf("Le nombre %i est hors diagramme \n", nombre);
            system("pause");
            return 0;
        }
        else {
            printf("Le nombre %i appartient a %s%s%s \n", nombre, a, b, c);
            system("pause");
            return 0;
        }
	}
}
