#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

void fonctAddi(){

	int lig, col, i, j, matrice1[4][4], matrice2[4][4], resultat[4][4];

	printf("Inseret le nombre de lignes : ");
	scanf("%i", &lig);
	printf("Inseret le nombre de colonnes : ");
	scanf("%i", &col);
	printf("\n");

	printf("Inseret les chiffres de la premiere matrice : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++){
			printf("matrice [%d][%d] : ",i,j);
			scanf("%d", &matrice1[i][j]);
		}
	}

	printf("Inseret les chiffres de la deuxieme matrice : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++) {
			printf("matrice [%d][%d] : ",i,j);
			scanf("%d", &matrice2[i][j]);
		}
	}

	printf("La somme des deux matrices : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++) {
            resultat[i][j] = matrice1[i][j]  + matrice2[i][j] ;
			printf("%d\t", resultat[i][j]);
		}
		printf("\n");
	}
}

void fonctScalaire(){

	int lig, col, i, j, scalaire, matrice1[4][4], resultat[4][4];

	printf("Inseret le scalaire : ");
	scanf("%i", &scalaire);
	printf("Inseret le nombre de lignes : ");
	scanf("%i", &lig);
	printf("Inseret le nombre de colonnes : ");
	scanf("%i", &col);
	printf("\n");

	printf("Inseret les chiffres de la matrice : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++){
			printf("matrice [%d][%d] : ",i,j);
			scanf("%d", &matrice1[i][j]);
		}
	}

	printf("La premiere matrice : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++) {
			printf("%d\t", matrice1[i][j]);
		}
		printf("\n");
	}

	printf("La matrice multipliee par le scalaire : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++) {
            resultat[i][j] = matrice1[i][j]  * scalaire ;
			printf("%d\t", resultat[i][j]);
		}
		printf("\n");
	}
}

void fonctTranspo(){

	int lig, col, i, j, matrice1[4][4], resultat[4][4];

	printf("Inseret le nombre de lignes : ");
	scanf("%i", &lig);
	printf("Inseret le nombre de colonnes : ");
	scanf("%i", &col);
	printf("\n");

	printf("Inseret les chiffres de la matrice : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++){
			printf("matrice [%d][%d] : ",i,j);
			scanf("%d", &matrice1[i][j]);
		}
	}

	printf("La premiere matrice : \n");
	for (i = 0; i < lig; i++) {
		for (j = 0; j < col; j++) {
			printf("%d\t", matrice1[i][j]);
		}
		printf("\n");
	}

	printf("La matrice transposee : \n");
	for (i = 0; i < col; i++) {
		for (j = 0; j < lig; j++) {
            resultat[i][j] = matrice1[j][i] ;
			printf("%d\t", resultat[i][j]);
		}
		printf("\n");
	}
}

void fonctMultipli(){

	int  i, j, k, lig1, col1, lig2, col2, matrice1[4][4], matrice2[4][4], resultat[4][4], converCol, converLig;

	printf("Inseret le nombre de lignes de la premiere matrice : ");
	scanf("%i", &lig1);
	printf("Inseret le nombre de colonnes de la premiere matrice : ");
	scanf("%i", &col1);
	printf("\n");

	printf("Inseret le nombre de lignes de la deuxieme matrice : ");
	scanf("%i", &lig2);
	printf("Inseret le nombre de colonnes de la deuxieme matrice : ");
	scanf("%i", &col2);
	printf("\n");

	printf("Inseret les chiffres de la premiere matrice : \n");
	for (i = 0; i < lig1; i++) {
		for (j = 0; j < col1; j++){
			printf("matrice [%d][%d] : ",i,j);
			scanf("%d", &matrice1[i][j]);
		}
	}

	printf("Inseret les chiffres de la deuxieme matrice : \n");
	for (i = 0; i < lig2; i++) {
		for (j = 0; j < col2; j++){
			printf("matrice [%d][%d] : ",i,j);
			scanf("%d", &matrice2[i][j]);
		}
	}

	converLig = (lig1 < lig2) ? lig1 : lig2 ;
	converCol = (col1 < col2) ? col1 : col2 ;

	printf("Le produit matriciel : \n");
	for (i = 0; i < converLig; i++) {
		for (j = 0; j < converCol; j++) {
            resultat[i][j]=0;
          	for (k = 0; k < col1; k++){

            	resultat[i][j] += matrice1[i][k]*matrice2[k][j];
          	}
			printf("%d\t", resultat[i][j]);
        }
		printf("\n");
	}
}

int main(){

	int choix;

    do {
		printf("Addition de deux matrices (1) \n");
		printf("Multiplication de deux matrices (2) \n");
		printf("Multiplication d une matrice par un scalaire (3) \n");
		printf("Transposition d une matrice (4) \n\n");
		printf("Votre choix : ");
		scanf("%i", &choix);

        if (choix == 1) {
			printf("Addition de deux matrices \n");
			fonctAddi();
        }
        else if (choix == 2) {
            printf("Multiplication de deux matrices  \n");
			fonctMultipli();
        }
        else if (choix == 3) {
			printf("Multiplication d une matrice par un scalaire \n");
			fonctScalaire();
		}
		else if (choix == 4) {
			printf("Transposition d une matrice \n");
			fonctTranspo();
        }
    } while (choix != 1 && choix != 2 && choix != 3 && choix != 4);

	system("pause");
    return 0;
}
