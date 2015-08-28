#-*-coding: utf-8 -*-

import re
from fyzz import parse
from stanford_corenlp_pywrapper import CoreNLP
import random
import numpy
import difflib
tempq='./temp/question.txt'

r=random.random
# g est la liste des questions posant problème au parseur SPARQL
java= "../stanford-corenlp-full-2015-04-20/*"
def question(loc="./input/donnee.xml",MatchCriterium=0.5):
    i=0
    quest=1
    res=[] # // L'ensemble des ressources que l'on utilisera avec notre logiciel
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    with open(loc,'r') as inp, open(tempq,'w') as out,open("./beast/requetes.txt","r+") as req, open("./beast/general.txt","w") as gen, open("./beast/parsed-req.txt","w") as preq, open('./beast/tok.txt','w') as tok:
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
                    preq.write(str(ressource)+'\n')
                    gen.write('//'+str(ressource)+'\n')
                    #print "Tableau de la question "+ str(compteur)+" " + str(tableau)
                    for pos1,xValues in enumerate(ressource):
                        if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in str(xValues) or search('yago',str(xValues)) :
                            gen.write("\nResourceType("+xValues[2][1]+"["+str(quest)+"],Class)\n")
                            stock_ressources.append(xValues[2][1])
                            for phrase in tableau:
                                res=simi(None,str(xValues[2][1]),str(phrase.title()),None).ratio()
                                if  res > MatchCriterium:
                                    gen.write(str(res)[0:4]+" PriorMatchScore("+str(xValues[2][1])+"["+str(quest)+"],"+str(phrase.title())+"["+str(quest)+"]"+")\n\n")
                        else:
                            for pos2,yValues in enumerate(xValues):
                                #On vérifie qu'il ne s'agisse pas d'une variable
                                if isinstance(yValues,tuple):
                                    # On recherche la catégorie dans laquelle la mettre
                                    if search('ontology',yValues[0]):
                                        if yValues[0][0]==yValues[0][0].lower():
                                            gen.write("\nResourceType(Dbo_"+str(yValues[1]).title()+"["+str(quest)+"]"+",Relation)\n")
                                            stock_ressources.append(yValues[1])
                                            for phrase in tableau:
                                                res=simi(None,str(yValues[1]),str(phrase.title()),None).ratio()
                                                if  res> MatchCriterium :
                                                    gen.write(str(res)[0:4]+" PriorMatchScore(Dbo_"+str(yValues[1]).title()+"["+str(quest)+"]"+","+str(phrase.title())+"["+str(quest)+"]"+")\n\n")

                                    elif search('resource',yValues[0]):
                                        gen.write("\nResourceType(Dbr_"+str(yValues[1]).title()+"["+str(quest)+"]"+",Entity)\n")
                                        stock_ressources.append(yValues[1])
                                        for phrase in tableau:
                                            res=simi(None,str(yValues[1]),str(phrase.title()),None).ratio()
                                            if  res >MatchCriterium:
                                                gen.write(str(res)[0:4]+" PriorMatchScore(Dbr_"+str(yValues[1].title())+"["+str(quest)+"]"+","+str(phrase.title())+"["+str(quest)+"]"+")\n\n")

                                    elif search('http://dbpedia.org/property/',str(xValues[1][0])):
                                        gen.write('\nResourceType(' + str(xValues[1][1].title())+"["+str(quest)+"]"+ ',Class)\n')
                                        stock_ressources.append(xValues[1][1].title()+"["+str(quest)+"]")
                                        for phrase in tableau:
                                            res=simi(None,str(xValues[1][1]),str(phrase.title()),None).ratio()
                                            if  res > MatchCriterium:
                                                gen.write(str(res)[0:4]+" PriorMatchScore("+str(xValues[1][1].title())+"["+str(quest)+"]"+","+str(phrase.title())+"["+str(quest)+"]"+")\n\n")
                                    else:
                                        #print "\nTEST : "+str(xValues)
                                        pass
                    
                    #
                    #  ECRITURE DES REQUETES
                    # 
                    req.write(m.group(0)+"\n")
                    gen.write('//'+m.group(0)+'\n'+'\n'+'\n')


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
                    for l,token in enumerate(elmt['sentences'][0]['tokens']):
                        if token not in stopwords:
                            tableau.append(token.title())
                            gen.write("PhraseIndex("+token.title()+"["+str(quest)+"]"+','+str(l+1)+','+str(l+1)+')\n')

                    gen.write('\n//'+str(tableau)+'\n')
                    #tok.write(tableau)

                    out.write(var)
                    gen.write('//'+var+"\n//La ligne est isolée \n")
                    for token in tableau:
                        cpt2=0
                        #On crée la feature PosTag
                        for pos in elmt["sentences"][0]['pos']:
                            #On crée la feature DepTag
                            if cpt1==cpt2:
                                gen.write("PhrasePosTag("+token+"["+str(quest)+"]"+','+pos+")\n")
                            cpt2=cpt2+1
                        cpt1=cpt1+1

                    #
                    # On crée le prédicat deptag
                    #
                    deptag=elmt['sentences'][0]['deps_cc']
                    for cpt in range(len(deptag)):
                        if cpt < len(tableau):
                            a= "PhraseDepTag("+tableau[deptag[cpt][1]]+"["+str(quest)+"]"+","+tableau[deptag[cpt][2]]+"["+str(quest)+"]"+","+deptag[cpt][0]+")\n"
                            #print a
                            gen.write(a)
                            
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
                #a = inp.next()  // Remplacement de l'itérateur pour prendre l'element suivant 
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
                        out.write(temp)
                        gen.write('//'+temp+'\n')
                        #tok.write(str(proc.parse_doc(temp)['sentences'][0]['tokens'])+'\n')
                        gen.write('//'+str(elmt['sentences'][0]['tokens'])+'\n')
                        #
                        #  EXTRACTION DES DÉPENDANCES SYNTAXIQUES
                        #

                        tableau=[]
                        for l,token in enumerate(elmt['sentences'][0]['tokens']):
                            if token not in stopwords:
                                tableau.append(token.title())
                                gen.write("PhraseIndex("+token.title()+"["+str(quest)+"]"+','+str(l+1)+','+str(l+1)+')\n')

                        for token in tableau:
                            cpt2=0
                            #On crée la feature PosTag
                            for pos in elmt["sentences"][0]['pos']:
                                #On crée la feature DepTag
                                if cpt1==cpt2:
                                    gen.write("PhrasePosTag("+token+"["+str(quest)+"]"+','+pos+")\n")
                                cpt2=cpt2+1
                            cpt1=cpt1+1    
                        #
                        deptag=elmt['sentences'][0]['deps_cc']
                        for cpt in range(len(deptag)):
                            if cpt < len(tableau):
                                a= "PhraseDepTag("+tableau[deptag[cpt][1]]+"["+str(quest)+"]"+","+tableau[deptag[cpt][2]]+"["+str(quest)+"]"+","+deptag[cpt][0]+")\n"
                                #print a
                                gen.write(a)
                            
                        #
                        # Fin de la création de deptag
                        #


    
                    else:
                        print "discarded question "+ str(compteur) +" : "+ temp+'\n'


"""                            for elmt in proc.parse_doc(temp)['sentences'][0]['deps_cc']:
                            gen.write(str(elmt))
                        for elmt in proc.parse_doc(temp)['sentences'][0]['pos']:
                            gen.write(str(elmt))
"""             

question()
