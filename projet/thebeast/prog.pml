/*On définit l'ensemble des prédicats dont on aura besoin pour notre implémentation des MLN's */ 
predicate phraseIndex: Phrase x Position x Position;
predicate phrasePosTag: Phrase x PosTag;
predicate phraseDepTag: Phrase x Phrase x DepTag;
predicate phraseDepOne: Phrase x Phrase;
predicate hasMeanWord: Phrase x Phrase;
predicate resourceType: Resource x Type;
predicate priorMatchScore: Phrase x Resource x Score;
predicate hasRelatedness: Phrase x Phrase x Score;
predicate isTypeCompatible: Resource x Resource x Relation;
predicate hasQueryResults: Resource x Resource x Resource x Relation;
predicate hasPhrase: Phrase;
predicate hasResource: Phrase x Resource;
predicate hasRelation: Resource x Resource x Relation;
