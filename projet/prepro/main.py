#-*-coding: utf-8 -*-

import re
from fyzz import parse
from stanford_corenlp_pywrapper import CoreNLP
tempq='./temp/question.txt'

# g est la liste des questions posant problème à
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
            if j ==0:
                print j
            g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170, 173, 175, 182, 186]

            #
            # TRAITEMENT DES REQUETES ET EXTRATION DES RESSOURCES
            #

            m=re.search("PREFIX(.)*",line)
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
            if i!=0:
                var=tab[j+1]
                if compteur not in g:
                    elmt=proc.parse_doc(var)
                    tableau=[]
                    for token in elmt['sentences'][0]['tokens']:
                         if token not in stopwords:
                             tableau.append(token)

                    #tok.write(tableau)
                    out.write(var)
                    gen.write(var)
                    for value in elmt['sentences'][0]['deps_cc']:
                        gen.write(str(value)+ '\n')

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
                            print a
                            gen.write(a)
                            
                    #
                    # Fin de la création de deptag
                    #

                else:
                    print "discarded question : "+ var
                i=i-1
            elif "<string lang=\"en" in line:
                #a = inp.next()  // Remplacement de l'itérateur pour prendre l'element suivant 
                var=tab[j+1]
                m=re.search("<!\[CDATA\[$",var)
                if m:
                    i=i+1
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
                        for token in elmt['sentences'][0]['tokens']:
                            if token not in stopwords:
                                tableau.append(token)

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
                                print a
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
