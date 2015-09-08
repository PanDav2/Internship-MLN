/// ON DEFINIT ICI LES REGLES AJUSTABLE PAR UN CERTAIN COEFFICIENT

// La définition des formules modifiables par coefficient se fait par la définition d'un "prédicat" weight.

//sf1
factor: for Resource r, Phrase p, Double s
       if priorMatchScore(p,r,s) add [hasPhrase(p)]*s;

//sf2
factor: for Resource r, Phrase p, Double s
	if priorMatchScore(p,r,s) add [hasResource(p,r)]*s;

//sf3
weight w_sf31: PosTag x Type -> Double;
//weight w_sf32: Type-> Double+;
//weight w_sf33: Phrase x Resource -> Double+;
factor :for Resource r, PosTag pT, Phrase p, Type rT
	if phrasePosTag(p,pT) & resourceType(r,rT) add [hasResource(p,r)]*w_sf31(pT,rT);

weight w_sf3 : PosTag -> Double;
factor :for Phrase p, PosTag pT
	if phrasePosTag(p,pT) add [hasPhrase(p)]*w_sf3(pT);
//sf4
/*weight w_sf41: DepTag -> Double+;
weight w_sf42: Relation -> Double+;
factor : for Phrase p1, Phrase p2, DepTag dT, Resource r1, Resource r2, Relation rr
	if phraseDepTag(p1,p2,dT) & hasResource(p1,r1) & hasResource(p2,r2) add [hasRelation(r1,r2,rr)]*w_sf41(dT)*w_sf42(rr);
*///sf5
//factor : for Phrase p1, Phrase p2, DepTag dT, Resource r1, Resource r2, Relation rr
//	if phraseDepTag(p1,p2,dT) & hasResource(p1,r1) & hasResource(p2,r2) & !hasMeanWord(p1,p2) add [hasRelation(r1,r2,rr)]*w_sf41(dT)*w_sf42(rr);

//sf6
/*factor : for Phrase p1, Phrase p2, DepTag dT, Resource r1, Resource r2, Relation rr
	if phraseDepTag(p1,p2,dT) & hasResource(p1,r1) & hasResource(p2,r2) & phraseDepOne(p1,p2) add [hasRelation(r1,r2,rr)]*w_sf41(dT)*w_sf42(rr);
*/
//sf7
/*weight w_sf7: Resource x Resource -> Double+;
factor : for Resource r1, Resource r2, Int s 
	if hasRelatedness(r1,r2,s) & hasResource(_,r1)& hasResource(_,r2) add [hasRelation(r1,r2,_)]*double(s)*w_sf7(r1,r2);
*/
//sf8
//weight w_sf8: Resource x Resource x Resource x Relation x Relation -> Double+; 
set collector.all.w_sf31 = true;
