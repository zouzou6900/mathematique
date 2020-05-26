#include <stdio.h>
#include <math.h>

void fonctScalaire() {

    int degre, i, j;
    printf("Entrez le degre de vos polynomes \n");
    scanf("%d",&degre);
    float tableau[2][degre+1], scalaire;

    //Boucle d'entrée des coefficients des polynômes
    printf("Entrez les donnees du polynome : \n");
    for(j=degre;j>=0;j--){
        printf("Entrez la donnee de x^%d : ",j);
        scanf("%f",&tableau[0][j]);
    }

    printf("Entrez le scalaire : \n");
    scanf("%f",&scalaire);

    for(j=0;j<=degre;j++){
        tableau[1][j] = tableau[0][j] * scalaire;
    }

    //Affichage du résultat
    printf("Résultat du produit du polynome par le scalaire : \n");
    for(j=degre;j>=0;j--){
        printf("%f x^%d",tableau[1][j],j);
        if(j>0){
            printf(" + ");
        }
        else{
            printf("\n");
        }
    }
}

void fonctProduit(){

        int degre, i, j;
        printf("Entrez le degre de vos polynomes \n");
        scanf("%d",&degre);
        float tableau[3][degre+1];

        //Boucle d'entrée des donnees des polynômes
        for(i=0;i<=1;i++){
            printf("Entrez les donnees du polynome %d : \n",i+1);
            for(j=degre;j>=0;j--){
                printf("Entrez la donnee de x^%d : ",j);
                scanf("%f",&tableau[i][j]);
            }
        }
        //Calcul du produit des donnees et sauvegarde dans le tableau
        for(j=0;j<=degre;j++){
            for(i=0;i<=degre;i++){
                tableau[2][j] = tableau[0][j] * tableau[1][j];
            }
        }
        //Affichage du résultat
        printf("Résultat du produit des deux polynomes : \n");
        for(j=degre;j>=0;j--){
            printf("%f x^%d",tableau[2][j],j);
            if(j>0){
                printf(" + ");
            }
            else{
                printf("\n");
            }
        }
}

void fonctSom(){

    int degre, i, j;
    printf("Entrez le degré de vos polynomes \n");
    scanf("%d",&degre);
    float tableau[3][degre+1];

    //Boucle d'entrée des donnees des polynômes
    for(i=0;i<=1;i++){
        printf("Entrez les donnees du polynome %d : \n",i+1);
        for(j=degre;j>=0;j--){
            printf("Entrez la donnee de x^%d : ",j);
            scanf("%f",&tableau[i][j]);
        }
    }

    //Calcul de la somme des donnees et sauvegarde dans le tableau
    for(j=0;j<=degre;j++){
        tableau[2][j] = tableau[0][j] + tableau[1][j];
    }

    //Affichage du résultat
    printf("Résultat de la somme des deux polynomes : \n");
    for(j=degre;j>=0;j--){
        printf("%f x^%d",tableau[2][j],j);
        if(j>0){
            printf(" + ");
        }
        else{
            printf("\n");
        }
    }
}

int main(){

	int choix;

	do {
		printf("Somme de deux polynomes (1) \n");
		printf("Produits de deux polynomes (2) \n");
		printf("Produit d'un polynome par un scalaire (3) \n");
		printf("Votre choix : ");
		scanf("%i", &choix);

        if (choix == 1) {
			printf("Somme de deux polynomes \n");
			fonctSom();
	   }
	   else if (choix == 2) {
            printf("Produits de deux polynomes \n");
			fonctProduit();
	   }
		else if (choix == 3) {
			printf("Produit d'un polynome par un scalaire \n");
			fonctScalaire();
		}
	} while (choix != 1 && choix != 2 && choix != 3);

	system("pause");
    return 0;
}
