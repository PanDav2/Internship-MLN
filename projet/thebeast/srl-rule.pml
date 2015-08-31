/*
Des règles dur de notre système de MLN.

L'avantage c'est que l'on peut gérer les contraintes de cardinalité de manière plus transparente et directe.
*/

// Afin de permettre à l'algorithme d'apprendre les constantes qui ne sont pas toutes présentes dans ce document nous ajoutons la mention : 

// -> save types to "<filename>";

// Afin de se reservir de ces informations sur l'ensemble d'un domaine, nous utilisons la mention :

// -> include "<filename>";

type Phrase: "J'aime", "le", "chocolat";
type Resource: "Moi", "Aimer", "Kinder";
type Relation: "1_1", "2_2", "1_2", "2_1";
type PosTag: "M", "N", "For";
type DepTag: "nmod", "det", "subj";
type Type: "Entity", "Class", "Relation";

predicate phraseIndex: Phrase x Int x Int;
predicate phrasePosTag: Phrase x PosTag;
predicate phraseDepTag: Phrase x Phrase x DepTag;
predicate phraseDepOne: Phrase x Phrase;
predicate hasMeanWord: Phrase x Phrase;
predicate resourceType: Resource x Type;
predicate priorMatchScore: Phrase x Resource x Int;
predicate hasRelatedness: Phrase x Phrase x Double;
predicate isTypeCompatible: Resource x Resource x Relation;
predicate hasQueryResults: Resource x Resource x Resource x Relation;
predicate hasPhrase: Phrase;
predicate hasResource: Phrase x Resource;
predicate hasRelation: Resource x Resource x Relation;
predicate overlap: Int x Int x Int x Int;
predicate isTypeCompatible: Resource x Resource x Relation;
// On liste les prédicats qu'il faudra prédire plus tard.
hidden: hasRelation,hasResource,hasPhrase; 

//hf1
factor : for Phrase p, Resource r if hasPhrase(p) : hasResource(p,r);
//hf2
factor: for Phrase p if hasResource(p,_): hasPhrase(p);
//hf3
factor: for Phrase p: |Resource r: hasResource(p,r)|<=1;
//hf4
factor: for Phrase p, Resource r if !hasPhrase(p) : hasResource(p,r);
//hf5
factor: for Resource r if hasResource(_,r) : hasRelation(r,_,_) | hasRelation(_,r,_);
//hf6
factor: for Resource r1, Resource r2 : |Relation r: hasRelation(r1,r2,r)|<=1;
//hf7
factor: for Resource r1, Resource r2 : hasResource(_,r1) & hasResource(_,r2);
//hf8
factor: for Phrase p1, Int s1, Int e1, Phrase p2, Int s2, Int e2 if phraseIndex(p1,s1,e1) & phraseIndex(p2,s2,e2) & overlap(s1,e1,s2,e2) & hasPhrase(p1) : !hasPhrase(p2);
//hf9
factor: for Resource r if resourceType(r,"Entity"): !hasRelation(r,_,"2_1") & !hasRelation(r,_,"2_2");
//hf 10
factor: for Resource r if resourceType(r,"Entity"): !hasRelation(_,r,"2_1") & !hasRelation(_,r,"2_2");
//hf11
factor: for Resource r if resourceType(r,"Class"): !hasRelation(r,_,"2_1") & !hasRelation(r,_,"2_2");
//hf12
factor: for Resource r if resourceType(r,"Class"): !hasRelation(_,r,"2_1") & !hasRelation(_,r,"2_2");
//hf13
factor: for Resource r1, Resource r2, Relation rr if !isTypeCompatible(r1,r2,rr) : hasRelation(r1,r2,rr);


/// ON DEFINIT ICI LES REGLES AJUSTABLE PAR UN CERTAIN COEFFICIENT

// La définition des formules modifiables par coefficient se fait par la définition d'un "prédicat" weight.


//sf1
weight w_sf1: Phrase x Resource -> Double+;
factor: for Resource r, Phrase p, Int s 
	if priorMatchScore(p,r,s) add [priorMatchScore(p,r,s)=>hasPhrase(p)]*double(s)*w_sf1(p,r);

//sf2
weight w_sf2: Phrase x Resource -> Double+;
factor: for Resource r, Phrase p, Int s
	if priorMatchScore(p,r,s) add [priorMatchScore(p,r,s)=>hasResource(p,r)]*double(s)*w_sf2(p,r);

//sf3
weight w_sf3: 
factor: for PosTag pT, ResourceType rT, Phrase p
	if phrasePosTag(p,pT) & resourceType(r,rT) add [phrasePosTag(p,pT)]
