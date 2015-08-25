#-*-coding: utf-8 -*-

import re
from fyzz import parse
from stanford_corenlp_pywrapper import CoreNLP
tempq='./temp/question.txt'

# g est la liste des questions posant problème au parseur SPARQL
java= "../stanford-corenlp-full-2015-04-20/*"
def question(loc="./input/donnee.xml"):
    i=0
    res=[] # // L'ensemble des ressources que l'on utilisera avec notre logiciel
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    with open(loc,'r') as inp, open(tempq,'w') as out,open("./temp/requetes.txt","r+") as req, open("./temp/general.txt","w") as gen, open("./temp/parsed-req.txt","w") as preq, open('./temp/tok.txt','w') as tok:
        tab=[]
        for line in inp:
            tab.append(line)
        compteur=0
        for j,line in enumerate(tab):
            flag=0
            #if j ==0:
                #print j
            g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170, 173, 175, 182, 186]

            #
            # TRAITEMENT DES REQUETES ET EXTRATION DES RESSOURCES
            #
            search=re.search
            m=search("PREFIX(.)*",line)
            if m!=None:
                #a.append(str(m.group(0)))
                compteur=compteur+1
                if compteur not in g:

                    #
                    #  EXTRACTION ET ECRITURE DES RESSOURCES 
                    #
                    ressource=parse(str(m.group(0))).where
                    preq.write(str(ressource)+'\n')
                    gen.write(str(ressource)+'\n')
                    
                    for pos1,xValues in enumerate(ressource):
                        if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in str(xValues) or search('yago',str(xValues)) :
                            gen.write("CODE0 : ResourceType("+xValues[2][1]+",Class)\n")
                        else:
                            for pos2,yValues in enumerate(xValues):
                                #On vérifie qu'il s'agisse pas d'une variable
                                if isinstance(yValues,tuple):
                                    # On recherche la catégorie dans laquelle la mettre
                                    if search('ontology',yValues[0]):
                                        if yValues[0][0]==yValues[0][0].lower():
                                            gen.write("CODE2 : ResourceType(dbo_"+str(yValues[1]).title()+",Relation)\n")

                                    elif search('resource',yValues[0]):
                                        gen.write("CODE4 : ResourceType(dbr_"+str(yValues[1]).title()+",Entity)\n")
                                    elif search('http://dbpedia.org/property/',str(xValues[1][0])):
                                        gen.write('CODE0 : ResourceType(' + str(xValues[1][1].title())+ ',Class)\n')
                                    else:
                                        print "\nTEST : "+str(xValues)
                    
                    #
                    #  ECRITURE DES REQUETES
                    #
                    
                    
                    req.write(m.group(0)+"\n")
                    gen.write(m.group(0)+'\n'+'\n'+'\n')


            #
            #  EXTRACTION ET ECRITURE DES QUESTIONS
            #

            stopwords = ["?",",",".","!"]
            cpt1=0
            #Cas o`u la ligne de questions est isolée
            if i!=0:
                #gen.write("")
                var=tab[j+1]
                if compteur not in g:
                    elmt=proc.parse_doc(var)
                    tableau=[]
                    # On stock l'ensemble des tokens dans un tableau
                    for l,token in enumerate(elmt['sentences'][0]['tokens']):
                         if token not in stopwords:
                             tableau.append(token)
                             gen.write("PhraseIndex("+token.title()+','+str(l+1)+','+str(l+1)+')\n')
                    gen.write('\n'+str(tableau)+'\n')
                    #tok.write(tableau)

                    out.write(var)
                    gen.write(var+"\t La ligne est isolée \n")
                    for token in tableau:
                        cpt2=0
                        #On crée la feature PosTag
                        for pos in elmt["sentences"][0]['pos']:
                            #On crée la feature DepTag
                            if cpt1==cpt2:
                                gen.write("PhrasePosTag("+token+','+pos+")\n")
                            cpt2=cpt2+1
                        cpt1=cpt1+1

                    #
                    # On crée le prédicat deptag
                    #
                    deptag=elmt['sentences'][0]['deps_cc']
                    for cpt in range(len(deptag)):
                        if cpt < len(tableau):
                            a= "phraseDepTag("+tableau[deptag[cpt][1]]+","+tableau[deptag[cpt][2]]+","+deptag[cpt][0]+")\n"
                            #print a
                            gen.write(a)
                            
                    #
                    # Fin de la création de deptag
                    #

                else:
                    print "discarded question : "+ var
                i=i-1
            #Cas général, on détecte les questions en anglais
            elif "<string lang=\"en" in line:
                #a = inp.next()  // Remplacement de l'itérateur pour prendre l'element suivant 
                #On recherche si la ligne suivante ne contient que le signe CDATA
                var=tab[j+1]
                m=search("<!\[CDATA\[$",var)
                #On s'apprete à extraire la ligne suivant qui est une question isolée.
                if m:
                    if not search("PREFIX(.)*",var):
                        i=i+1
                #La ligne suivante n'est pas isolée, il s'agit d'une question entourée de marqueurs.
                else :
                    #print a[10:len(str(a))-4]
                    temp=var[10:len(str(var))-4]
                    elmt=proc.parse_doc(temp)
                    if compteur not in g:
                        out.write(temp)
                        gen.write(temp+'\n')
                        #tok.write(str(proc.parse_doc(temp)['sentences'][0]['tokens'])+'\n')
                        gen.write(str(elmt['sentences'][0]['tokens'])+'\n')
                        #
                        #  EXTRACTION DES DÉPENDANCES SYNTAXIQUES
                        #

                        tableau=[]
                        for l,token in enumerate(elmt['sentences'][0]['tokens']):
                            if token not in stopwords:
                                tableau.append(token)
                                gen.write("PhraseIndex("+token.title()+','+str(l+1)+','+str(l+1)+')\n')
                        for token in tableau:
                            cpt2=0
                            #On crée la feature PosTag
                            for pos in elmt["sentences"][0]['pos']:
                                #On crée la feature DepTag
                                if cpt1==cpt2:
                                    gen.write("PhrasePosTag("+token+','+pos+")\n")
                                cpt2=cpt2+1
                            cpt1=cpt1+1    
                        #
                        deptag=elmt['sentences'][0]['deps_cc']
                        for cpt in range(len(deptag)):
                            if cpt < len(tableau):
                                a= "phraseDepTag("+tableau[deptag[cpt][1]]+","+tableau[deptag[cpt][2]]+","+deptag[cpt][0]+")\n"
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
