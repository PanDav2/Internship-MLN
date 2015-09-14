#-*-coding: utf-8 -*-
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
class compteur:
    def __init__(self,compteur,compteur_q):
        self.cpt=compteur
        self.cptq=compteur_q
    def incremente(self,q=False):
        if q:
            self.cptq += 1
            print "nouvelle valeur de compteur_q", str(self.cptq)
        else:
            self.cpt += 1
            print "nouvelle valeur de compteur", str(self.cpt)
            
a = compteur(0,0)

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
                        temp=["HasMeanWord(",numerise(mot),',',dep,')\n']
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
                        temp=["HasMeanWord(",numerise(mot),',',dep,')\n']
                        structure_multifile(s.join(temp),files)
                        #print str(mot)+"\t"+str(dep)+"\n"
                        break
                phraseDepOne(mot,dep,pos,files)

                
def phraseDepOne(mot,dep,tab,files):
    if len(tab)==1:
        s=""
        temp=["PhraseDepOne(",numerise(mot),',',dep,")\n"]
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


def numerise(message,ind=a):
    s=""
    temp=[message,'[',str(ind.cptq),']']
    return s.join(temp)

def createTab(entry,stopwords=stopwords):
    tab=[]
    for elmt in entry:
        if elmt not in stopwords:
            tab.append(numerise(elmt))
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
            temp=[str(res)[0:5],space,'PriorMatchScore(',phrase,',',prefix,numerise(str(resource)),")\n"]
            structure_multifile(s.join(temp),files)            

def treatQuestion(proc,question):
    tokenizer=proc.parse_doc(question)['sentences'][0]
    tableau = re.sub("[^\w]"," ",question).split()
    #tableau=map(title,tableau)
    res=[]
    #tableau= [for elmt in map(lambda : string))]
    res=map(numerise,res)
    return tokenizer,res


def extractQuestion(texte,case):
    mapping = {
        "cas1" : str(texte[10:len(str(texte))-4]),
        "cas2" : str(texte)
        }
    return mapping.get(case,lambda:'nothing')

def EntityType(resource,files):
    s=""
    a=s.join([prefixGen("Entity"),resource])
    temp=["ResourceType(",numerise(a),',',"Entity)\n"]
    structure_multifile(s.join(temp),files)            

def ClassType(resource,files):
    s=""
    a=s.join([prefixGen("Class"),resource])
    temp=["ResourceType(",numerise(a),',',"Class)\n"]
    structure_multifile(s.join(temp),files)            

def RelationType(resource,files):
    s=""
    a=s.join([prefixGen("Relation"),resource])
    temp=["ResourceType(",numerise(a),',',"Relation)\n"]
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
    temp=["PhraseIndex(",str(index),',',phrase,")\n"]
    structure_multifile(s.join(temp),files)            

def Dep_Pos_Extraction(tokenizer,files,debug=False):
    # On stock l'ensemble des tokens dans un tableau
    tableau=[]
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
            phraseIndex(index,numerise(token),files)
            tableau.append(token)
            if debug:
                print "Appended token\t"+str(token)+'\n'
    cpt1=0
    #On crée un dictionnaire de posTag pour la feature hasMeanWord
    for token in tableau:
        cpt2=0
        #On crée la feature PosTag
        for pos in tokenizer['pos']:
            if cpt1==cpt2:
                s=''
                temp=['PhrasePosTag(',numerise(str(token)),',',str(pos),")\n"]
                structure_multifile(s.join(temp),files)
                dico_Mots[str(token)]['pos']=pos
                reverse_Dico[dico_Mots[str(token)]['index']]['pos']=pos
            cpt2=cpt2+1
        cpt1=cpt1+1

    # On crée le prédicat deptag
    #
    deptag=tokenizer['deps_cc']
    for cpt in range(len(deptag)):
        if cpt < len(tableau):
            s=''
            intoDico(str(tableau[deptag[cpt][1]]),str(tableau[deptag[cpt][2]]),dico_Mots)
            temp=["PhraseDepTag(",numerise(tableau[deptag[cpt][1]]),',',numerise(tableau[deptag[cpt][2]]),',',deptag[cpt][0].title(),')\n']
            structure_multifile(s.join(temp),files)
                #
                # Fin de la création de deptag
                #
                #On crée la feature hasMeanWord
    hasMeanWord(dico_Mots,reverse_Dico,files)
    


def main(loc="./input/donnee.xml",MatchCriterium=0.5,debug=False,compteur=a):
    i=0
    quest=1
    #pickle.load( open( "save.p", "rb" ) )
    proc = CoreNLP('nerparse',corenlp_jars=[java])
    #pickle.dump(proc,  open( "save.p", "wb" ) )
    res=[] # // L'ensemble des ressources que l'on utilisera avec notre logiciel

    with open(loc,'r') as inp, open("./output-tuffy/output_beast.pml","w") as gen, open("./output-tuffy/priorMatchScore","w") as pms:
        # TAB CONTIENT L'ENSEMBLE DES LIGNES DU DOCUMENT DE DONNES (XML)
        tab=[]
        for line in inp:
            tab.append(line)
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
                    compteur.incremente(q=True)
                    if compteur.cpt not in g:
                        if m:
                            question=str(extractQuestion(tab[j+2],"cas2")) +'\n'
                        else:
                            question=str(extractQuestion(tab[j+1],"cas1")) + '\n'
                            print "question n° "+ str(compteur.cptq)+'\n'
                            #structure_multifile(">>\n",gen)
                            (tokenizer,tableau)=treatQuestion(proc,question)
                            Dep_Pos_Extraction(tokenizer,gen)
            #
            # TRAITEMENT DES REQUETES ET EXTRATION DES RESSOURCES
            #
            m=search("PREFIX(.)*",line)
            if m :
                compteur.incremente()
                if compteur.cpt not in g:
                    #
                    #  EXTRACTION ET ECRITURE DES RESSOURCES 
                    #
                    ressource=parse(str(m.group(0))).where
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

main()
