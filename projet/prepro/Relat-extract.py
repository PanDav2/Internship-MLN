#-*- coding: utf-8 -*-
import re
from fyzz import parse

g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170, 173, 175, 182, 186]
i=0
with open ("./temp/requetes.txt", "r") as inp:
    rien=[]
    for ligne,elmt in enumerate(inp):
        search = re.search
        if not search("^#",elmt):
            print "REQUETE "+str(elmt)+'\n'
            temp =parse(elmt).where
            print "REFERENCE " +str(temp)
            for pos1,xValues in enumerate(temp):
                if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in str(xValues) or search('yago',str(xValues)) :
                    print "CODE0 : ResourceType("+xValues[2][1]+",Class)"
                else:
                    for pos2,yValues in enumerate(xValues):
                        #On vérifie qu'il s'agisse pas d'une variable
                        if isinstance(yValues,tuple):
                            # On recherche la catégorie dans laquelle la mettre
                            if search('ontology',yValues[0]):
                                if yValues[0][0]==yValues[0][0].lower():
                                    print "CODE2 :ResourceType(dbo_"+str(yValues[1]).title()+",Relation)"
                            elif search('resource',yValues[0]):
                                print "CODE4 : ResourceType(dbr_"+str(yValues[1]).title()+",Entity)"
                            elif search('http://dbpedia.org/property/',str(xValues[1][0])):
                                print 'CODE0 : ResourceType(' + str(xValues[1][1].title())+ ',Class)\n'
                            else:
                                print "\nTEST : "+str(xValues)
