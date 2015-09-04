
/* Load the types we generated based on the training corpus */
include "types.pml";

/* Load the SRL mln */
include "srl.pml";

/* Load the weights we allowed to be nonzero in the collection step (init.pml) */
load weights from dump "srl.weights";

/* Load a test corpus */
load corpus from "test.atoms";

print atoms;

/* Now we want to apply our MLN to all worlds in the test corpus
   and write out the result. Note that this will also print out
   some statistics. */
test to "system.atoms";

