// On place ici l'ensemble des prédicats globaux. 

predicate resourceType: Resource x Type;
predicate priorMatchScore: Phrase x Resource x Int;
predicate hasRelatedness: Resource x Resource x Int;
predicate isTypeCompatible: Resource x Resource x Relation;
predicate hasQueryResults: Resource x Resource x Resource x Relation;

/* On définit ici l'ensemble des prédicats locaux de thebeast */

predicate phraseIndex: Int x Phrase;
predicate phrasePosTag: Phrase x PosTag;
predicate phraseDepTag: Phrase x Phrase x DepTag;
predicate phraseDepOne: Phrase x Phrase;
predicate hasMeanWord: Phrase x Phrase;
predicate hasPhrase: Phrase;
predicate hasResource: Phrase x Resource;
predicate hasRelation: Resource x Resource x Relation;
//predicate overlap: Int x Int x Int x Int;
// On liste les prédicats qu'il faudra prédire plus tard.
hidden : hasRelation,hasResource,hasPhrase;
observed : phraseIndex, phrasePosTag, phraseDepTag, phraseDepOne, hasMeanWord;
global :  resourceType, priorMatchScore, hasRelatedness, isTypeCompatible, hasQueryResults;

include "srl-global.pml";
include "srl-local.pml";
