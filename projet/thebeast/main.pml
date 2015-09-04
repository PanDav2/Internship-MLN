// On charge le fichier de types

include "srl-types.pml";

// On charge le fichier avec les règles SRL 

influde "srl.pml";

// On charge les atomes globaux qui sont vrais dans tous les monde possibles 
load global from "global.atoms";

// On charge en entrainement l'ensemble de tous les mondes possibles.
load corpus from "train.atoms";

// On récupère l'ensemble des formules d'instantiation qui peuvent ne pas être violées
collect;

// on affiche les poids obtenus

print weights;

// On enregistre le corpus obtenu dans le fichier indiqué
save corpus to instances "srl.instances";

// On effectue l'apprentissage en ligne en 10 epochs 
learn for 10 epochs;

// On affiche les nouveaux poids à l'écran 
print weights;


// On enregistre les poids obtenus dans un fichier
save weights to dump "srl.weights";

//On charge un corpus de tes 

