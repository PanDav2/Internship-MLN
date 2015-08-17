#-*- coding: utf-8 -*-
## This script is meant to pre-process the data #TO COMPLETE
#from __future__ import unicode_literals
import sys
import random
import numpy
from stanford_corenlp_pywrapper import CoreNLP
from difflib import SequenceMatcher

java= "../stanford-corenlp-full-2015-04-20/*"
quest = "./output/quest-en.txt"
typeOfContent = ["Class","Entity","Relationship"]


#TODO gérer les problèmes d'encodage
#TODO extraire a partir d'un fichier donnée en argument 

def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()

#TODO Définir une variable score
def depOne(inp,stopwords):
    with open('./output/depOne.txt','w') as depone:
        a = []
        for elmt in inp:
            for sent in elmt["sentences"][0]["lemmas"]:
                if sent not in stopwords:
                    a.append(sent)
        for elmt in a:
            for elmt2 in a:
                    if random.random()<0.01:
                        depone.write("PhraseDepOne("+elmt.title()+','+elmt2.title()+')\n')


    

def question(loc):
    print "\n ####  Extraction des questions à partir du fichier donnees en parametre  ####\n"
    data = "./output/data.txt"
    #TODO gérer l'extraction multi-lingue par un tableau
    #lan=["fr,en,es,it,fr,nl,ro"]
    with open(data,'w') as out:
        with open(loc,'r') as inp:
            for line in inp:
            #On détecte les lignes ou les phrases sont en anglais
                if "<string lang=\"en".decode().encode('utf-8') in line:
                    out.write(inp.next().title())
    with open(data,'r') as inp:
        with open(quest,'w') as out:
            for line in inp:
                if len(line.split())>1:
                    """
                    #Tentative de concatenner l'ensemble des mots en une phrase
                    for i in len(line.split()):
                    print line.split()[i]
                    """
                    out.write(line[10:len(line)-4]+'\n'.decode().encode('utf-8'))
    print "\n ####  Extraction des questions terminée  ####\n"

## Cette fonction gère la création des features phraseIndex, PosTag et crée les ressources.

## TODO Faire des fonctions afin que l'on s'y retouve mieux dans le traitement de données

def phrases(data):
    #STOPWORDS is the list of words we'd like to discards in our 
    stopwords =[".","?","!",',']
    proc = CoreNLP("nerparse",corenlp_jars=[java])
    p=[]
    i=1
    print "####  Traitement et mise en forme des questions extraites  ####"
    with open(data,'r') as inp:
        for line in inp:
            #print "traitement de la ligne " + str(i)
            p.append(proc.parse_doc(line))
            i+=1
    depOne(p,stopwords)
    with open('./output/phrases.txt','w') as outp:
        with open('./output/ressources1.txt','w') as outr:
            with open("./output/index.txt",'w') as outi:
                with open("./output/posTag.txt",'w') as outpos:
                    with open("./output/depTag.txt",'w') as outdep:
                        for elmt in p:
                            #### DEBUG
                            #print elmt["sentences"][0]["tokens"]
                            ####
                            for tok in elmt["sentences"][0]["lemmas"]:
                                if not tok in stopwords: 
                                    a = tok                                
                                    outr.write(a)
                                    outr.write('\n'.decode().encode('utf-8'))
                                    #Création de la feature phraseIndex
                            index=0
                            i=0
                            tableau=elmt["sentences"][0]["tokens"]
                            deptag=elmt['sentences'][0]['deps_cc']
                            for cpt in range(len(deptag)):
                                if not tableau[deptag[cpt][1]] in stopwords:
                                    outdep.write("PhraseDepTag("+tableau[deptag[cpt][1]]+","+tableau[deptag[cpt][2]]+","+deptag[cpt][0].title()+")\n")
                            for tok in tableau:
                                j=0
                                if not tok in stopwords: 
                                    #On crée la feature PosTag
                                    for pos in elmt["sentences"][0]['pos']:
                                        #On crée la feature DepTag
                                        if i==j:
                                            outpos.write("PhrasePosTag("+tok+','+pos+")\n")
                                        j=j+1
                                    i=i+1
                                        
                                    outp.write(tok.decode().encode('utf-8')+'\n'.decode().encode('utf-8'))
                                    outp.write('\n'.decode().encode('utf-8'))
                                    outi.write("PhraseIndex("+tok+","+str(index)+","+str(index+1)+")")
                                    index=index+1
                                    outi.write('\n'.decode().encode('utf-8'))
                        





def ressourcesType():
    print "\t #### Création de la feature RessourceType à partir du fichier en cours...  ####"
    #We create an array that will remember the resourceType created in case of redundance and will allow us to match ressource types to 
    res = []
    inp = "./output/ressources1.txt"
    out = "./output/ressourceType.txt"
    with open(out,"w") as file:
        with open("./ressources.txt","w") as ress:
            with open(inp,"r") as data:
                for line in data:
                    # We discard the empty lines created by the PhraseExtractor 
                    if line !=('\n'):
                        #Creation of the resourceType feature
                        #We consider that all phrases have all the possible types
                        for X in typeOfContent:
                            #We create random ressources type using a uniform distribution
                            temp = (line[:-1]+"["+X[:1]+"]")
                            #print temp
                            ress.write(temp+"\n")
                            if temp not in res :
                                res.append(temp)
                                file.write("ResourceType("+temp.title()+","+X[:1]+")\n")
    print "\t\t #### Création de la feature RessourceType à partir du fichier terminéé.  ####"


def Pclean():
    with open("./output/phrases.txt","r") as inp:
        with open("./output/clean-p.txt",'w') as out:
            for line1 in inp:
                if not len(line1.split())<1:
                    out.write(line1)


def Rclean():
    a = []    
    with open("./output/ressources1.txt","r") as inp:
        with open("./output/clean-r.txt",'w') as out:
            for line1 in inp:
                if line1 != "\n":
                    if line1 not in a: 
                        a.append(line1.title())
                        out.write(line1)

def hasRelatedness():
    a=[]
    with open("./output/clean-r.txt","r") as inp:
        for elmt in inp: 
            if elmt != '\n':
                if elmt not in a:
                    a.append(elmt)
        with open("./output/related.txt",'w') as out:
            for elmt in a:                     
                for elmt2 in a:
                    if elmt == elmt2 :
                        out.write("HasRelatedness("+elmt[:-1].title()+","+elmt2[:-1].title()+","+"1)\n")
                    else:
                        #print elmt
                        #print "hasRelatedness("+line1[:-1]+","+line2[:-1]+","+str(random.random())+')'
                        out.write("HasRelatedness("+elmt[:-1].title()+","+elmt2[:-1].title()+","+str(random.random())+")\n")


## Nous construisons la feature priorMatchScore en nous basant sur la similarité
## On suppose que tous les types sont compatibles entre eux
def priorMatchScore():
    with open("./output/clean-r.txt","r") as Rinp:
        with open("./ressources.txt","r") as Pinp:
            with open("./output/priorMatchScore.txt","w") as out:
                with open("./output/isTypeCompatible.txt","w") as outtype:
                    for line1 in Rinp:
                        for line2 in Pinp:
                            out.write("PriorMatchScore("+line1[:-1].title()+','+line2[:-1].title()+','+str(random.random())+')\n')
                            outtype.write("IsTypeCompatible("+line1[:-1].title()+','+line2[:-1].title()+','+"True"+')\n')

loc = sys.argv[1]

## Création de la base de connaissances

question(loc)
phrases(quest)
ressourcesType()
hasRelatedness()
Pclean()
priorMatchScore()



