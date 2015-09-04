#-*-coding: utf-8 -*-

import re
from fyzz import parse
from stanford_corenlp_pywrapper import CoreNLP
import random
import numpy
import difflib
from numpy import floor
tempq='./temp/question.txt'

r=random.random
# g est la liste des questions posant problème au parseur SPARQL
java= "../stanford-corenlp-full-2015-04-20/*"
space = "  "

def EntityType(resource,files):
    #On vérifie si on a passé une liste de fichiers à notre système.
    if type(files) is file:
        files.write("\n>resourceType\n")
        files.write(str(resource.title())+"   Entity\n")
    else :
        for elmt in files:
            elmt.write("\n>resourceType\n")
            elmt.write(str(resource.title())+"   Entity\n")
        
def ClassType(resource,files):
    #On vérifie si on a passé une liste de fichiers à notre système.
        files.write("\n>resourceType\n")        
    if type(f) is file:
        files.write(str(resource.title())+"   Class\n")
    else :
        for elmt in files:
            elmt.write(str(resource.title())+"   Class\n")



def RelationType(resource,files):
    if type(f) is file:
        files.write("\n>resourceType\n")
        files.write(str(resource.title())+"   Relation\n")
    else :
        for elmt in files:
            elmt.write(str(resource.title())+"   Relation\n")


def resourceType(typ,resource,fichiers):
    switcher = {
        'Entity' : EntityType,
        'Class' : ClassType,
        'Relation' : RelationType
    }
    func = switcher.get(typ,lambda :'nothing')

    return func(resource,fichiers)

#def priorMatchScore(phrase,resource,score):

def priorMatchScore(phrases,resource,files):
    for phrase in phrases:
        res=simi(None,str(resource),str(phrase.title()),None).ratio()
        if  res >MatchCriterium:
            if type(files) is file:
                files.write("\n>hasPhrase\n"+str(phrase.title())+'\n')
                files.write("\n>priorMatchScore\n")
                files.write(phrase.title()+space+"Dbr_"+str(yValues[1].title())+space+str(res)[0:5]+"\n")
        else:
            for elmt in files:
                elmt.write("\n>hasPhrase\n"+str(phrase.title())+'\n')
                elmt.write("\n>priorMatchScore\n")
                elmt.write(phrase.title()+space+"Dbr_"+str(yValues[1].title())+space+str(res)[0:5]+"\n")

def question(loc="./input/donnee.xml",MatchCriterium=50):
    i=0
    quest=1
    res=[] # // L'ensemble des ressources que l'on utilisera avec notre logiciel
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    with open(loc,'r') as inp, open("./beast/requetes.txt","w") as req, open("./beast/general.pml","w") as gen, open("./beast/resourceType.txt","w") as resType, open("./beast/priorMatchScore","w") as pms, open('./test.test','w') as test:
        # TAB CONTIENT L'ENSEMBLE DES LIGNES DU DOCUMENT DE DONNES (XML)
        tableau=[]
        tab=[]
        for line in inp:
            tab.append(line)
        compteur=0
        simi=difflib.SequenceMatcher

        for j,line in enumerate(tab):
            stock_ressources=[]
            #if j ==0:
                #print j
            g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170,171, 173, 175, 182, 186]

            #
            # TRAITEMENT DES REQUETES ET EXTRATION DES RESSOURCES
            #

            search=re.search
            m=search("PREFIX(.)*",line)
            if m!=None:
                compteur=compteur+1
                #a.append(str(m.group(0)))
                if compteur not in g:

                    #
                    #  EXTRACTION ET ECRITURE DES RESSOURCES 
                    #
                    ressource=parse(str(m.group(0))).where
                    #gen.write('//'+str(ressource)+'\n')
                    #print "Tableau de la question "+ str(compteur)+" " + str(tableau)
                    resType.write(">>\n")
                    pms.write(">>\n")
                    for pos1,xValues in enumerate(ressource):
                        if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in str(xValues) or search('yago',str(xValues)) :
                            #gen.write("\nResourceType("+xValues[2][1]+"["+str(quest)+"],Class)\n")
                            #gen.write(xValues[2][1]+space+"Class")
                            #print xValues[2][1]+"  Class"

                            resType.write(xValues[2][1]+"  Class\n")
                            gen.write("\n>resourceType\n")
                            gen.write(xValues[2][1]+"  Class\n")
                            stock_ressources.append(xValues[2][1])

                            # On crée le fichier prior match score correspondant à cet exemple

                            for phrase in tableau:
                                res=simi(None,str(xValues[2][1]),str(phrase.title()),None).ratio()
                                if  res > MatchCriterium:
                                    # On écrit le hasPhrase
                                    gen.write(">hasPhrase\n")
                                    gen.write(str(phrase.title())+'\n')
                                    # On écrit le hasResource
                                    gen.write("\n>hasResource\n")
                                    gen.write(phrase+space+str(xValues[2][1])+"\n")
                                    # On écrit le priorMatchScore
                                    pms.write(">priorMatchScore\n")
                                    gen.write("\n>priorMatchScore\n")                                    
                                    pms.write(space+str(phrase.title())+str(xValues[2][1])+space+str(res)[0:3]+"\n")
                                    gen.write(str(phrase.title())+space+str(xValues[2][1])+space+str(res)[0:3]+"\n")
                        else:
                            for pos2,yValues in enumerate(xValues):
                                #On vérifie qu'il ne s'agisse pas d'une variable
                                if isinstance(yValues,tuple):
                                    # On recherche la catégorie dans laquelle la mettre
                                    if search('ontology',yValues[0]):
                                        if yValues[0][0]==yValues[0][0].lower():
                                            """#gen.write("\nResourceType(Dbo_"+str(yValues[1]).title()+"["+str(quest)+"]"+",Relation)\n")
                                            gen.write("\n>resourceType\n")
                                            gen.write(yValues[1].title()+"  Relation\n")
                                            resType.write(yValues[1].title()+"  Relation\n")"""
                                            resourceType('Relation',yValues[1],[gen,resType])                                            

                                            stock_ressources.append(yValues[1])
                                            priorMatchScore(tableau,yValues[1],[gen,resType)

                                    elif search('resource',yValues[0]):
                                        resourceType('Entity',yValues[1],[gen,resType])
                                        stock_ressources.append(yValues[1])
                                        priorMatchScore(tableau,yValues[1],[gen,pms])

                                    elif search('http://dbpedia.org/property/',str(xValues[1][0])):

                                        stock_ressources.append(xValues[1][1].title()+"["+str(quest)+"]")
                                        gen.write("\n>resourceType\n")
                                        gen.write(xValues[1][1]+"   Class\n")
                                        resType.write(xValues[1][1]+"   Class\n")
                                        for phrase in tableau:

                                            res=simi(None,str(xValues[1][1]),str(phrase.title()),None).ratio()
                                            if  res > MatchCriterium:
                                                #gen.write(str(res)[0:4]+" PriorMatchScore("+str(xValues[1][1].title())+"["+str(quest)+"]"+","+str(phrase.title())+"["+str(quest)+"]"+")\n\n")
                                                gen.write("\n>hasPhrase\n")
                                                gen.write(str(phrase.title())+'\n')
                                                gen.write(phrase.title()+space+xValues[1][1]+space+str(res)[0:2]+"\n")
                                    else:
                                        #print "\nTEST : "+str(xValues)
                                        pass
                    
                    #
                    #  ECRITURE DES REQUETES
                    # 
                    #gen.write('\n//'+m.group(0)+'\n'+'\n'+'\n')


            #
            #  EXTRACTION ET ECRITURE DES QUESTIONS
            #
            #print "CODE4 : " + str(stock_ressources)
            stopwords = ["?",",",".","!"]
            cpt1=0
            #Cas o`u la ligne de questions est isolée
            if i!=0:
                #gen.write("")
                var=tab[j+1]
                if compteur not in g:
                #if True:
                    elmt=proc.parse_doc(var)
                    # On stock l'ensemble des tokens dans un tableau
                    tableau=[]
		    gen.write(">phraseIndex\n")
                    for l,token in enumerate(elmt['sentences'][0]['tokens']):
                        if token not in stopwords:
                            tableau.append(token.title())
			    gen.write(str(l+1)+space+token.title()+"\n")	

                    #gen.write('\n//'+str(tableau)+'\n')
                    #tok.write(tableau)
                    #gen.write('\n//'+var+"\n//La ligne est isolée \n")
                    for token in tableau:
                        cpt2=0
                        #On crée la feature PosTag
                        for pos in elmt["sentences"][0]['pos']:
                            #On crée la feature DepTag
                            if cpt1==cpt2:
                                #gen.write("PhrasePosTag("+token+"["+str(quest)+"]"+','+pos+")\n")
                                pass
                            cpt2=cpt2+1
                        cpt1=cpt1+1

                    #
                    # On crée le prédicat deptag
                    #
                    deptag=elmt['sentences'][0]['deps_cc']
                    gen.write("\n>phraseDepTag\n")
                    for cpt in range(len(deptag)):
                        if cpt < len(tableau):
                            gen.write(tableau[deptag[cpt][1]]+space+tableau[deptag[cpt][2]]+space+deptag[cpt][0].title()+'\n')
                            #gen.write(a)
                            
                    #
                    # Fin de la création de deptag
                    #

                else:
                    #print "discarded question : "+ var
                    pass
                i=i-1
            # ON REPERE LES LIGNES DE QUESTIONS ICI
            elif "<string lang=\"en" in line:
                quest=quest+1
                gen.write(">> \n")
                #On recherche si la ligne suivante ne contient que le signe CDATA
                var=tab[j+1]
                m=search("<!\[CDATA\[$",var)
                #On s'apprete à extraire la ligne suivant qui est une question isolée.
                if m:
                    # SI IL NE S'AGIT PAS D'UNE REQUETE ALORS LA LIGNE SUIVANTE EST UNE QUESTION
                    if not search("PREFIX(.)*",var):
                        i=i+1
                #La ligne suivante n'est pas isolée, il s'agit d'une question entourée de marqueurs.
                else :
                    #print a[10:len(str(a))-4]
                    temp=var[10:len(str(var))-4]
                    elmt=proc.parse_doc(temp)
                    if compteur not in g:
                        #gen.write('\n//'+temp+'\n')
                        #tok.write(str(proc.parse_doc(temp)['sentences'][0]['tokens'])+'\n')
                        #gen.write('\n//'+str(elmt['sentences'][0]['tokens'])+'\n')
                        #
                        #  EXTRACTION DES DÉPENDANCES SYNTAXIQUES
                        #

                        tableau=[]
                        for l,token in enumerate(elmt['sentences'][0]['tokens']):
                            if token not in stopwords:
                                tableau.append(token.title())
                                #gen.write("PhraseIndex("+token.title()+"["+str(quest)+"]"+','+str(l+1)+','+str(l+1)+')\n')

                        gen.write("\n>phrasePosTag\n")
                        for token in tableau:
                            cpt2=0

                            #On crée la feature PosTag
                            for pos in elmt["sentences"][0]['pos']:
                                if cpt1==cpt2:
                                    #gen.write("PhrasePosTag("+token+"["+str(quest)+"]"+','+pos+")\n")
                                    gen.write(token+space+pos+'\n')
                                      
                                    pass
                                cpt2=cpt2+1
                            cpt1=cpt1+1    
                        #
                        gen.write("\n>phraseDepTag\n")
                        deptag=elmt['sentences'][0]['deps_cc']
                        for cpt in range(len(deptag)):
                            if cpt < len(tableau):
                                gen.write(tableau[deptag[cpt][1]]+space+tableau[deptag[cpt][2]]+space+deptag[cpt][0].title()+'\n')
                            
                        #
                        # Fin de la création de deptag
                        #


    
                    else:
                        print "discarded question "+ str(compteur) +" : "+ temp+'\n'



question()

