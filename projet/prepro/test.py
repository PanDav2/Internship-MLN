#-*- coding: utf-8 -*-
import re
from fyzz import parse

g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170, 173, 175, 182, 186]
i=0
with open ("./temp/requetes.txt", "r") as inp:
    for elmt in inp:
        #if re.search("^#",elmt)==None:
        if i not in g:
            #print "ligne "+ str(i)
            temp =parse(elmt).where
            print "REFERENCE " +str(temp)
            print "\n\n"
            for pos1,xValues in enumerate(temp):
                print "Il y a "+ str(len(xValues)) +" valeurs dans l'élement " + str(xValues)
                print "\n Elles sont :  \n "
                for pos2,yValues in enumerate(xValues):
                    #On vérifie qu'il s'agisse pas de valeurs 
                    if isinstance(yValues,tuple):
                        # On recherche la catégorie dans laquelle la mettre
                        if re.search('ontology',yValues[0]):
                            if yValues[0][0]==yValues[0][0].lower():
                                print "ResourceType("+str(yValues[1]).title()+",Relation)"
                            else:
                                print "ResourceType("+str(yValues[1]).title()+",Class)"
                        else :
                            print "ResourceType("+str(yValues[1]).title()+",Class)"
                        
                        
                        
            #print str(len(parse(str(elmt)).where))+' tuples alain Térieur \n'
            print "\n\n"
        i+=1
"""
with open ("./res.txt", "r+") as file:
    old = file.read()
    file.seek(0)
    file.write(str(g)+'\n'+old)

with open ("./res.txt", "r+") as file:
    print str(file.seek(2))
    
"""
