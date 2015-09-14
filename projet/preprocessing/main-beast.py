#-*-coding: utf-8 -*-
import sys
import pickle
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
search=re.search

def init():
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    pickle.dump(proc,  open( "save.p", "wb" ) )

def  hasRelation(inp):
    print inp
    t= search("SparqlVar",str(inp[0]))
    if t:
        print str(inp[0])
        print "Variable à gauche"
        if search('resource',str(inp[2])):
            print "\n>hasRelation"+'_1'+'\n'        
    t= search("SparqlVar",str(inp[2]))
    if t:
        print str(inp[2])
        print "Variable à droite"
        if search('resource',str(inp[0])):
            print "\n>hasRelation"+'1_'+'\n'        

def hasMeanWord(dico,reverse,files):
    for mot in dico:
        notMeanWord=["DT","IN","WDT","TO","CC","EX","POS","WP"]
        pos=[]
        #print mot,dico[mot]['index']
        for dep in dico[mot]['dep']:
            s= dico[mot]['index']
            e= dico[dep]['index']
            #print 's = '+str(s)
            #print 'e = '+str(e)
            if e>s:
                for values in range(s,e-1):
                    #print reverse[values]
                    if reverse[values].has_key('pos'):
                        pos.append(reverse[values]['pos'])
                        #print reverse[values]['pos']
                        #print '\n'
                
                for tag in pos:
                    if tag not in notMeanWord:
                        #print ">hasMeanWord\n"
                        s=''
                        structure_multifile("\n>hasMeanWord\n",files)
                        temp=[toQuote(mot),space,toQuote(dep),'\n']
                        structure_multifile(s.join(temp),files)
                        break
                phraseDepOne(mot,dep,pos,files)
                
            else :
                for values in range(e,s-1):
                    if reverse[values].has_key('pos'):
                        pos.append(reverse[values]['pos'])
                for tag in pos:
                    if tag not in notMeanWord:
                        #print ">hasMeanWord\n"
                        s=''
                        structure_multifile("\n>hasMeanWord\n",files)
                        temp=[toQuote(mot),space,toQuote(dep),'\n']
                        structure_multifile(s.join(temp),files)
                        #print str(mot)+"\t"+str(dep)+"\n"
                        break
                phraseDepOne(mot,dep,pos,files)
def phraseDepOne(mot,dep,tab,files):
    if len(tab)==1:
        s=""
        temp=[toQuote(mot),space,toQuote(dep),"\n"]
        structure_multifile("\n>phraseDepOne\n",files)
        structure_multifile(s.join(temp),files)

"""
            else:
                for values in range(e,s):
                    print reverse[values]['pos']
                    print '\n'
"""

def intoDico(key,value,Dict):
    if not key in Dict:
        Dict[key]={}
        Dict[key]['dep'] = [value]
    else:
        Dict[key]['dep'].append(value)


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
        'Entity' : "dbr_",
        'Class' : "" ,
        'Relation': "dbo_"
    }
    return case.get(Type, lambda : 'nothing')


def priorMatchScore(phrases,resource,files,MatchCriterium,Type):
    prefix = prefixGen(Type)
    #print phrases
    for phrase in phrases:
        res=simi(None,str(resource),str(phrase),None).ratio()
        if  res >MatchCriterium:
            s=""
            temp=["\n>hasPhrase\n",phrase,"\n"]
            structure_multifile(s.join(temp),files)            
            structure_multifile("\n>priorMatchScore\n",files)            
            temp=[phrase,space,toQuote(s.join([prefix,str(resource)])),space,str(res)[0:5],"\n"]
            structure_multifile(s.join(temp),files)            

def treatQuestion(proc,question):
    tokenizer=proc.parse_doc(question)['sentences'][0]
    tableau = re.sub("[^\w]"," ",question).split()
    tableau=map(toQuote,tableau)
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
    a=toQuote(s.join([prefixGen("Entity"),resource]))
    temp=[a,"   Entity\n"]
    structure_multifile(s.join(temp),files)            

def ClassType(resource,files):
    structure_multifile("\n>resourceType\n",files)        
    s=""
    a=toQuote(s.join([prefixGen("Class"),resource]))
    temp=[a,"   Class\n"]
    structure_multifile(s.join(temp),files)            

def RelationType(resource,files):
    structure_multifile("\n>resourceType\n",files)        
    s=""
    a=toQuote(s.join([prefixGen("Relation"),resource]))
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
    temp=[str(index),space,phrase,"\n"]
    structure_multifile(s.join(temp),files)            

def Dep_Pos_Extraction(tokenizer,files,debug=False):
    # On stock l'ensemble des tokens dans un tableau
    tableau=[]
    structure_multifile(">phraseIndex\n",files)
    dico_Mots={}
    reverse_Dico={}
    for l,token in enumerate(tokenizer['tokens']):
        index = l+1
        if token not in stopwords: 
            if debug:
                print index
            dico_Mots[str(token)]={}
            reverse_Dico[index]={}
            dico_Mots[str(token)]['dep']=[]
            reverse_Dico[index]['dep']=[]
            dico_Mots[str(token)]['index']=index
            reverse_Dico[index]['mot']=str(token)
            phraseIndex(index,toQuote(token),files)
            tableau.append(token)
            if debug:
                print "Appended token\t"+str(token)+'\n'
    structure_multifile("\n>phrasePosTag\n",files)
    cpt1=0
    #On crée un dictionnaire de posTag pour la feature hasMeanWord
    for token in tableau:
        cpt2=0
        #On crée la feature PosTag
        for pos in tokenizer['pos']:
            if cpt1==cpt2:
                s=''
                temp=[toQuote(str(token)),space,toQuote(str(pos)),"\n"]
                structure_multifile(s.join(temp),files)
                dico_Mots[str(token)]['pos']=pos
                reverse_Dico[dico_Mots[str(token)]['index']]['pos']=pos
            cpt2=cpt2+1
        cpt1=cpt1+1

    # On crée le prédicat deptag
    #
    deptag=tokenizer['deps_cc']
    structure_multifile("\n>phraseDepTag\n",files)
    for cpt in range(len(deptag)):
        if deptag[cpt][1] < len(tableau) and deptag[cpt][2] < len(tableau):
            s=''
            intoDico(str(tableau[deptag[cpt][1]]),str(tableau[deptag[cpt][2]]),dico_Mots)
            temp=[toQuote(tableau[deptag[cpt][1]]),space,toQuote(tableau[deptag[cpt][2]]),space,toQuote(deptag[cpt][0].title()),'\n']
            structure_multifile(s.join(temp),files)
                #
                # Fin de la création de deptag
                #
                #On crée la feature hasMeanWord
    hasMeanWord(dico_Mots,reverse_Dico,files)
    


def main(loc="./input/donnee.xml",MatchCriterium=0.5,debug=False):

    i=0
    quest=1
    #pickle.load( open( "save.p", "rb" ) )
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    #pickle.dump(proc,  open( "save.p", "wb" ) )
    res=[] # // L'ensemble des ressources que l'on utilisera avec notre logiciel

    with open(loc,'r') as inp, open("./output-beast/trai.atoms","w") as gen, open("./output-beast/priorMatchScore","w") as pms:
        # TAB CONTIENT L'ENSEMBLE DES LIGNES DU DOCUMENT DE DONNES (XML)
        tab=[]
        for line in inp:
            tab.append(line)
        compteur=0
        compteur_q=0
        for j,line in enumerate(tab):
            stock_ressources=[]
            # g est l'ensemble des questions posant problème au parseur fyzz, probablement du à une version dépassée de SPARQL (la v1.0) pour le fichier donnee.xml
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
                #if compteur not in g:
                    #
                    #  EXTRACTION ET ECRITURE DES RESSOURCES 
                    #
                try:
                    ressource=parse(str(m.group(0))).where
                except Exception:
                    pass
                for pos1,xValues in enumerate(ressource):
                    if "http://www.w3.org/1999/02/22-rdf-syntax-ns#" in str(xValues) or search('yago',str(xValues)) :
                        stock_ressources.append(xValues[2][1])
                        resourceType('Class',xValues[2][1],[gen])
                        priorMatchScore(tableau,xValues[2][1],[gen],MatchCriterium,"Class")
                    else:
                        print line
                        # En cours d'implémentation hasRelation(xValues)                            
                        for pos2,yValues in enumerate(xValues):
                            #On vérifie qu'il ne s'agisse pas d'une variable
                            if isinstance(yValues,tuple):
                                # On recherche la catégorie dans laquelle la mettre
                                if search('ontology',yValues[0]):
                                    if yValues[0][0]==yValues[0][0]:
                                        resourceType('Relation',yValues[1],[gen,pms])                                            
                                        stock_ressources.append(yValues[1])
                                        
                                        priorMatchScore(tableau,yValues[1],[gen,pms],MatchCriterium,"Relation")
                                elif search('resource',yValues[0]):
                                    resourceType('Entity',yValues[1],[gen])
                                    stock_ressources.append(yValues[1])
                                    priorMatchScore(tableau,yValues[1],[gen,pms],MatchCriterium,"Entity")
                                elif search('http://dbpedia.org/property/',str(xValues[1][0])):
                                    stock_ressources.append(xValues[1][1])
                                    resourceType('Class',xValues[1][1],[gen])
                                    priorMatchScore(tableau,xValues[1][1],[gen,pms],MatchCriterium,"Class")



#init()
if len(sys.argv)!=1:
    main(loc=sys.argv[1])
else:
    main()
