#-*-coding: utf-8 -*-

import re
from fyzz import parse
from stanford_corenlp_pywrapper import CoreNLP
import random
import numpy
import difflib
from numpy import floor
import shelve
tempq='./temp/question.txt'
simi=difflib.SequenceMatcher
r=random.random
# g est la liste des questions posant problème au parseur SPARQL
java= "../stanford-corenlp-full-2015-04-20/*"
space = "  "
stopwords = ["?",",",".","!"]

def toQuote(message):
    s=""
    temp=['"',message,'"']
    return s.join(temp)

def createTab(entry,stopwords=stopwords):
    tab=[]
    for elmt in entry:
        if elmt not in stopwords:
            tab.append(toQuote(elmt))
    return tab

def structure_multifile(message,files):
    if type(files) is file:
        files.write(message)
    else:
        for elmt in files:
            elmt.write(message)

def prefixGen(Type):
    case = {
        'Entity' : "dbr-",
        'Class' : "" ,
        'Relation': "dbo-"
    }
    return case.get(Type, lambda : 'nothing')

def priorMatchScore(phrases,resource,files,MatchCriterium,Type):
    prefix = prefixGen(Type)
    #print phrases
    for phrase in phrases:
        res=simi(None,str(resource),str(phrase),None).ratio()
        if  res >MatchCriterium:
            s=""
            temp=["\n>hasPhrase\n",phrase.title(),"\n"]
            structure_multifile(s.join(temp),files)            
            structure_multifile("\n>priorMatchScore\n",files)            
            temp=[phrase.title(),space,toQuote(s.join([prefix,str(resource.title())])),space,str(res)[0:5],"\n"]
            structure_multifile(s.join(temp),files)            

def treatQuestion(proc,question):
    #print question
    tokenizer=proc.parse_doc(question)['sentences'][0]
    #print "TOKEN\t"+str(tokenizer)+'\n'
    tableau=createTab(question.split())
    #print "TABLEAU\t"+str(tableau)+'\n'
    return tokenizer,tableau


def extractQuestion(texte,case):
    mapping = {
        "cas1" : str(texte[10:len(str(texte))-4]),
        "cas2" : str(texte)
        }
    return mapping.get(case,lambda:'nothing')



def EntityType(resource,files):
    structure_multifile("\n>resourceType\n",files)
    s=""
    a=toQuote(s.join([prefixGen("Entity"),resource.title()]))
    temp=[a,"   Entity\n"]
    structure_multifile(s.join(temp),files)            

def ClassType(resource,files):
    structure_multifile("\n>resourceType\n",files)        
    s=""
    a=toQuote(s.join([prefixGen("Class"),resource.title()]))
    temp=[a,"   Class\n"]
    structure_multifile(s.join(temp),files)            

def RelationType(resource,files):
    structure_multifile("\n>resourceType\n",files)        
    s=""
    a=toQuote(s.join([prefixGen("Relation"),resource.title()]))
    temp=[a,"   Relation\n"]
    structure_multifile(s.join(temp),files)            

def resourceType(typ,resource,fichiers):
    switcher = {
        'Entity' : EntityType,
        'Class' : ClassType,
        'Relation' : RelationType
    }
    func = switcher.get(typ,lambda :'nothing')

    return func(resource,fichiers)

def phraseIndex(index,phrase,files):
    s=""
    temp=[str(index),space,phrase.title(),"\n"]
    structure_multifile(s.join(temp),files)            

def Dep_Pos_Extraction(tokenizer,files,debug=False):
    # On stock l'ensemble des tokens dans un tableau
    tableau=[]
    structure_multifile(">phraseIndex\n",files)
    for l,token in enumerate(tokenizer['tokens']):
        index = l+1
        if token not in stopwords:
            phraseIndex(index,toQuote(token),files)
            tableau.append(token)
            if debug:
                print "Appended token\t"+str(token)+'\n'
    structure_multifile("\n>phrasePosTag\n",files)
    cpt1=0
    for token in tableau:
        cpt2=0
        #On crée la feature PosTag
        for pos in tokenizer['pos']:
            if cpt1==cpt2:
                s=''
                temp=[toQuote(str(token)),space,toQuote(str(pos)),"\n"]
                structure_multifile(s.join(temp),files)
                
            cpt2=cpt2+1
        cpt1=cpt1+1
    #
    # On crée le prédicat deptag
    #
    deptag=tokenizer['deps_cc']
    structure_multifile("\n>phraseDepTag\n",files)
    for cpt in range(len(deptag)):
        if cpt < len(tableau):
            s=''
            temp=[toQuote(tableau[deptag[cpt][1]]),space,toQuote(tableau[deptag[cpt][2]]),space,toQuote(deptag[cpt][0].title()),'\n']
            structure_multifile(s.join(temp),files)
                #
                # Fin de la création de deptag
                #



def main(loc="./input/donnee.xml",MatchCriterium=0.5,debug=False):
    search=re.search
    i=0
    quest=1
    res=[] # // L'ensemble des ressources que l'on utilisera avec notre logiciel
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    with open(loc,'r') as inp, open("./beast/requetes.txt","w") as req, open("./beast/general.pml","w") as gen, open("./beast/resourceType.txt","w") as resType, open("./beast/priorMatchScore","w") as pms, open('./test.test','w') as test:
        # TAB CONTIENT L'ENSEMBLE DES LIGNES DU DOCUMENT DE DONNES (XML)
        tab=[]
        for line in inp:
            tab.append(line)
        compteur=0
        compteur_q=0
        for j,line in enumerate(tab):
            stock_ressources=[]
            # g est l'ensemble des questions posant problème au parseur fyzz, probablement du à une version dépassée de SPARQL (la v1.0)
            g=[16, 30, 37, 65, 78, 84, 98, 99, 114, 121, 131, 135, 136, 139, 140, 143, 149, 150, 152, 162, 168, 169, 170,171, 173, 175, 182, 186]
            #
            #  EXTRACTION ET ECRITURE DES QUESTIONS
            #

            if j+1<len(tab):
                var = str(tab[j+1])
                m=search("<!\[CDATA\[$",var)
                if "<string lang=\"en" in line:
                    compteur_q=compteur_q+1
                    if m:
                        question=str(extractQuestion(tab[j+2],"cas2")) +'\n'
                    else:
                        question=str(extractQuestion(tab[j+1],"cas1")) + '\n'
                    print "question n° "+ str(compteur_q)+'\n'
                    structure_multifile(">>\n",gen)
                    (tokenizer,tableau)=treatQuestion(proc,question)
                    Dep_Pos_Extraction(tokenizer,gen)
            #
            # TRAITEMENT DES REQUETES ET EXTRATION DES RESSOURCES
            #
            m=search("PREFIX(.)*",line)
            if m :
                compteur=compteur+1
                if compteur not in g:
                    #
                    #  EXTRACTION ET ECRITURE DES RESSOURCES 
                    #
                    ressource=parse(str(m.group(0))).where
                    for pos1,xValues in enumerate(ressource):
                        if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in str(xValues) or search('yago',str(xValues)) :
                            stock_ressources.append(xValues[2][1])
                            resourceType('Class',xValues[2][1],[gen,resType])
                            priorMatchScore(tableau,xValues[2][1],[gen,resType],MatchCriterium,"Class")
                            print "On envoie le tableau \n "+str(tableau)
                        else:
                            for pos2,yValues in enumerate(xValues):
                                #On vérifie qu'il ne s'agisse pas d'une variable
                                if isinstance(yValues,tuple):
                                    # On recherche la catégorie dans laquelle la mettre
                                    if search('ontology',yValues[0]):
                                        if yValues[0][0]==yValues[0][0]:
                                            resourceType('Relation',yValues[1],[gen,pms])                                            
                                            stock_ressources.append(yValues[1])
                                            print "On envoie le tableau \n "+str(tableau)
                                            priorMatchScore(tableau,yValues[1],[gen,pms],MatchCriterium,"Relation")
                                    elif search('resource',yValues[0]):
                                        resourceType('Entity',yValues[1],[gen,resType])
                                        stock_ressources.append(yValues[1])
                                        priorMatchScore(tableau,yValues[1],[gen,pms],MatchCriterium,"Entity")
                                        print "On envoie le tableau \n "+str(tableau)   
                                    elif search('http://dbpedia.org/property/',str(xValues[1][0])):

                                        stock_ressources.append(xValues[1][1].title())
                                        resourceType('Class',xValues[1][1],[gen,resType])
                                        priorMatchScore(tableau,xValues[1][1].title(),[gen,pms],MatchCriterium,"Class")
                                        print "On envoie le tableau \n "+str(tableau)

                            
main(debug=True)
