#-*-coding: utf-8 -*-

## Lecture du texte dans le fichier passé en paramètre 

import numpy as np
#from stanford_corenlp_pywrapper import CoreNLP


#TODO extraire a partir d'un fichier donnée en argument (adresse, puis interface graphique) 
def extract():
    loc = "./donnee.xml"
    data = "./data.txt"
    quest = "./quest-en.txt"
    #TODO gérer l'extraction multi-lingue par un tableau
    lan=["fr,en,es,it,fr,nl,ro"]
    
    with open(data,'w') as out:
        with open(loc,'r') as inp:
            for line in inp:
            #On détecte les lignes ou les phrases sont en anglais
                if "<string lang=\"en" in line:
                    out.write(inp.next())

    with open(data,'r') as inp:
        with open(quest,'w') as out:
            for line in inp:
                if len(line.split())>1:
                    """
                    #Tentative de concatenner l'ensemble des mots en une phrase
                    for i in len(line.split()):
                    print line.split()[i]
                    """
                    out.write(line[10:len(line)-4]+'\n')

#POS tagging using Stanford NLP tagger

#proc = CoreNLP("pos",corenlp_jars=["/people/panou/Stage/projet/stanford-corenlp-full-2015-04-20/*"])
