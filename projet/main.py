#-*-coding: utf-8 -*-

## Lecture du texte dans le fichier passé en paramètre 


import re
import numpy as np

loc = "./donnee.xml"
data = "./data.txt"
quest = "./quest.txt"

with open(data,'w') as out:
    with open(loc,'r') as inp:
        for line in inp:
            #On détecte les lignes ou les phrases sont en allemand
            if "<string lang=" in line:
                out.write(inp.next())

with open(data,'r') as inp:
    with open(quest,'w') as out:
        for line in inp:
            if len(line.split())>1:
                #Tentative de concatenner l'ensemble des mots en une phrase
                for i in len(line.split()):
                    print line.split()[i]
                #out.write(line[1:len(line)-2])
