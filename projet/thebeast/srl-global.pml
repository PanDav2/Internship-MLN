
/*
Des règles dur de notre système de MLN.

L'avantage c'est que l'on peut gérer les contraintes de cardinalité de manière plus transparente et directe.
*/

// Afin de permettre à l'algorithme d'apprendre les constantes qui ne sont pas toutes présentes dans ce document nous ajoutons la mention : 

// -> save types to "<filename>";

// Afin de se reservir de ces informations sur l'ensemble d'un domaine, nous utilisons la mention :

// -> include "<filename>";

//hf1
factor: for Phrase p, Resource r if hasPhrase(p) : hasResource(p,r);
//hf2
factor: for Phrase p if  hasResource(p,_) : hasPhrase(p);
//hf3
factor : for Phrase p if hasPhrase(p) : |Resource r : hasResource(p,r)|<=1;
//factor : |Phrase p: hasResource(p,_)|<=1;
//hf4
factor: for Phrase p, Resource r:  hasPhrase(p) |  !hasResource(p,r);
//hf5
factor: for Resource r if hasResource(_,r) : Relation rr1, Resource r2 hasRelation(r,r2,rr1) | Relation rr3 hasRelation(r2,r,rr3);
//hf6
factor: for Resource r1, Resource r2 : |Relation r: hasRelation(r1,r2,r)|<=1;
//factor : |Phrase p: hasRelation(r1,r2,p)|<=1;
//hf7
factor: for Resource r1, Resource r2 if hasRelation(r1,r2,_) :Phrase p1 hasResource(p1,r1) & hasResource(p2,r2);
//hf8
//factor: for Phrase p1, Int s1, Int e1, Phrase p2, Int s2, Int e2 if phraseIndex(s1,p1) & phraseIndex(s2,p2) & overlap(s1,e1,s2,e2) & hasPhrase(p1) : !hasPhrase(p2);
//hf9
//factor: resourceType(r,"Entity") => !hasRelation(r,_,"2_1") & !hasRelation(r,_,"2_2");
//hf 10
//factor: resourceType(r,"Entity") => !hasRelation(_,r,"2_1") & !hasRelation(_,r,"2_2");
//hf11
//factor: resourceType(r,"Class") => !hasRelation(r,_,"2_1") & !hasRelation(r,_,"2_2");
//hf12
//factor: resourceType(r,"Class") => !hasRelation(_,r,"2_1") & !hasRelation(_,r,"2_2");
//hf13
//factor: for Resource r1, Resource r2, Relation rr if !isTypeCompatible(r1,r2,rr) : hasRelation(r1,r2,rr);*/
