/* 
Des règles dur de notre système de MLN.

L'avantage c'est que l'on peut gérer les contraintes de cardinalité de manière plus transparente et directe.


//hf1
factor : for Phrase p, Resource r if hasPhrase(p) add [hasResource(p,r)];
//hf2
factor: for Phrase p if hasResource(p,_): hasPhrase(p);
//hf3
factor: for Phrase p: |Role r: hasResource(p,r)|<=1;*/
//hf4
type Phrase: "J'aime", "le", "chocolat";
type Resource: "Amour", "Moi", "Lindt", "Ferrero";

predicate hasResource: Phrase x Resource;
predicate hasPhrase: Phrase;
factor: for Phrase p, Resource r if !hasPhrase(p) : hasResource(p,r);
