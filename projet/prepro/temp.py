#-*- coding: utf-8 -*-
## This script is meant to pre-process the data #TO COMPLETE
import sys
from stanford_corenlp_pywrapper import CoreNLP

java= "../stanford-corenlp-full-2015-04-20/*"
quest = "./output/quest-en.txt"
typeOfContent = ["Class","Entity","Relationship"]

def phrases():
    #STOPWORDS is the list of words we'd like to discards in our phrases and relation extraction
    stopwords =[".","?","!",',']
    proc = CoreNLP("nerparse",corenlp_jars=[java])
    p=[]
    i=1
    print "####  Traitement et mise en forme des questions extraites  ####"
    with open(quest,'r') as inp:
        for line in inp:
            print "traitement de la ligne " + str(i)
            p.append(proc.parse_doc(line))
            i+=1

