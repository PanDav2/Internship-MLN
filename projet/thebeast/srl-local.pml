/// ON DEFINIT ICI LES REGLES AJUSTABLE PAR UN CERTAIN COEFFICIENT

// La définition des formules modifiables par coefficient se fait par la définition d'un "prédicat" weight.


//sf1
weight w_sf1: Phrase x Resource -> Double+;
factor: for Resource r, Phrase p, Int s 
	if priorMatchScore(p,r,s) add [priorMatchScore(p,r,s)=>hasPhrase(p)]*double(s)*w_sf1(p,r);

//sf2
weight w_sf2: Phrase x Resource -> Double+;
factor: for Resource r, Phrase p, Int s
	add [priorMatchScore(p,r,s)=>hasResource(p,r)]*double(s)*w_sf2(p,r);

//sf3
weight w_sf31: PosTag -> Double+;
weight w_sf32: Type-> Double+;
weight w_sf33: Phrase x Resource -> Double+;
factor : for Resource r, PosTag pT, Phrase p, Type rT
	add [phrasePosTag(p,pT) & resourceType(r,rT)=>hasResource(p,r)]*w_sf31(pT)*w_sf32(rT)*w_sf33(p,r);
//sf4
weight w_sf41: DepTag -> Double+;
weight w_sf42: Relation -> Double+;
factor : for Phrase p1, Phrase p2, DepTag dT, Resource r1, Resource r2, Relation rr
	add [phraseDepTag(p1,p2,dT) & hasResource(p1,r1) & hasResource(p2,r2) => hasRelation(r1,r2,rr)]*w_sf41(dT)*w_sf42(rr);
//sf5
factor : for Phrase p1, Phrase p2, DepTag dT, Resource r1, Resource r2, Relation rr
	add [phraseDepTag(p1,p2,dT) & hasResource(p1,r1) & hasResource(p2,r2) & !hasMeanWord(p1,p2) => hasRelation(r1,r2,rr)]*w_sf41(dT)*w_sf42(rr);

//sf6
factor : for Phrase p1, Phrase p2, DepTag dT, Resource r1, Resource r2, Relation rr
	add [phraseDepTag(p1,p2,dT) & hasResource(p1,r1) & hasResource(p2,r2) & phraseDepOne(p1,p2) => hasRelation(r1,r2,rr)]*w_sf41(dT)*w_sf42(rr);

//sf7
weight w_sf7: Resource x Resource -> Double+;
factor : for Resource r1, Resource r2, Relation rr, Int s
	add [hasRelatedness(r1,r2,s) & hasResource(_,r1)& hasResource(_,r2) => hasRelation(r1,r2,_)]*double(s)*w_sf7(r1,r2);

//sf8
weight w_sf8: Resource x Resource x Resource x Relation x Relation -> Double+; 
/*factor : for Resource r1, Resource r2, Resource r3, Relation rr1, Relation rr2
	add [hasQueryResult(r1,r2,r3,rr1,rr2)=> hasRelation(r1,r2,rr1) & hasRelation(r2,r3,rr2)]*w_sf8(r1,r2,r3,rr1,rr2);
*/
