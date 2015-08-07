#-*- coding: utf-8 -*-

""" This class is intended to extract phrases according to the given parameters.
 TODO: Implement differents parameters for the phrase extraction from sentences.
Actual parameters are He,  the usual NER from Stanford CoreNLP and the unigramm model without stopwords """
#mport re
import numpy as np
from stanford_corenlp_pywrapper import CoreNLP

#Loading the Stanford CoreNLP Lib

data = "./extracted-quest/quest-en.txt"
loc= "/people/panou/Stage/projet/stanford-corenlp-full-2015-04-20/*"


#STOPWORDS is the list of words we'd like to discards in our 
stopwords =[".","?","!",',']

proc = CoreNLP("nerparse",corenlp_jars=[loc])
p=[]
i=1
with open(data,'r') as inp:
    for line in inp:
        print "traitement de la ligne " + str(i)
        p.append(proc.parse_doc(line))
        i+=1

with open('./phrases.txt','w') as out:
    for elmt in p:
        #print elmt["sentences"][0]["tokens"]
        for tok in elmt["sentences"][0]["lemmas"]:
            if not tok in stopwords: 
                out.write(tok+'\n')
        out.write('\n')

