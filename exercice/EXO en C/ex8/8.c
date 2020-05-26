#include<stdio.h>
#include<stdlib.h>
#include<math.h>

// Structure de l'arbre
typedef struct noeud {
		int valeur;
		struct noeud *gauche;
		struct noeud *droite;
	} noeud;

// Prototypes des fonctions
void addNoeud(noeud **arbre, int valeur);
void affichArbre(noeud *arbre);

void addNoeud(noeud **arbre, int valeur) {
	noeud *tmpNoeud;
	noeud *tmpArbre = *arbre;
	noeud *element = malloc(sizeof(noeud));
	element->valeur = valeur;
	element->gauche = NULL;
	element->droite = NULL;

	if(tmpArbre) {
		do {

			tmpNoeud = tmpArbre;

			if(valeur > tmpArbre->valeur) {
				tmpArbre = tmpArbre->droite;

				if(!tmpArbre) {
					tmpNoeud->droite = element;
				}
			}
			else {
				tmpArbre = tmpArbre->gauche;
				if(!tmpArbre) {
					tmpNoeud->gauche = element;
				}
			}
		}
		while(tmpArbre);
	}
	else {
		*arbre = element;
	}
}

void affichArbre(noeud *arbre) {
    if(!arbre) {
    	return;
    }

    if(arbre->gauche) {
    	affichArbre(arbre->gauche);
    }

    printf("%d\n", arbre->valeur);

    if(arbre->droite) {
    	affichArbre(arbre->droite);
    }
}

int main() {

	int valeur;
	int nombre;
	int i=0;
	noeud *arbre = NULL;

	printf("Entrez le nombre d'element que doit contenir l'arbre : ");
	scanf("%d",&nombre);

	while(i<nombre) {
		printf("Entrez l'element %d : ",i+1);
		scanf("%d",&valeur);
		addNoeud(&arbre,valeur);
		i++;
	}

	printf("L'arbre obtenu est\n");
	affichArbre(arbre);

    system("pause");
	return 0;
}
