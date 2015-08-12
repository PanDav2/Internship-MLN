#-*- coding: utf-8 -*-
## This script is meant to pre-process the data #TO COMPLETE
#from __future__ import unicode_literals
import sys
import random
import numpy
from stanford_corenlp_pywrapper import CoreNLP

java= "/people/panou/Stage/projet/stanford-corenlp-full-2015-04-20/*"
quest = "./output/quest-en.txt"
typeOfContent = ["Class","Entity","Relationship"]



#TODO gérer les problèmes d'encodage
#TODO extraire a partir d'un fichier donnée en argument 
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
                    out.write(inp.next())
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
    print "\n ####  Extraction des questions terminé  ####\n"

def phrases():
    #STOPWORDS is the list of words we'd like to discards in our 
    stopwords =[".","?","!",',']
    proc = CoreNLP("nerparse",corenlp_jars=[java])
    p=[]
    i=1
    print "####  Traitement et mise en forme des questions extraites  ####"
    with open(quest,'r') as inp:
        for line in inp:
            print "traitement de la ligne " + str(i)
            p.append(proc.parse_doc(line))
            i+=1
    with open('./output/phrases.txt','w') as outp:
        with open('./output/ressources1.txt','w') as outr:
            for elmt in p:
                for tok in elmt["sentences"][0]["lemmas"]:
                    if not tok in stopwords: 
                        a =tok
                        print a 
                        outr.write(a+'\n'.decode().encode('utf-8'))
                        outr.write('\n'.decode().encode('utf-8'))
                for tok in elmt["sentences"][0]["tokens"]:
                    if not tok in stopwords: 
                        outp.write(tok.decode().encode('utf-8')+'\n'.decode().encode('utf-8'))
                        outp.write('\n'.decode().encode('utf-8'))
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
                                file.write("resourceType("+temp.lower()+","+X[:1]+")\n")
    print "\t\t #### Création de la feature RessourceType à partir du fichier terminéé.  ####"


def Pclean():
    with open("./output/phrases.txt","r") as inp:
        with open("./output/phrases-p.txt",'w') as out:
            for line1 in inp:
                if line1 != "\n":
                    out.write(line1)


def Rclean():
    a = []
    
    with open("./output/ressources1.txt","r") as inp:
        with open("./output/clean-r.txt",'w') as out:
            for line1 in inp:
                if line1 != "\n":
                    if line1 not in a: 
                        a.append(line1)
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
                    #print elmt
                    #print "hasRelatedness("+line1[:-1]+","+line2[:-1]+","+str(random.random())+')'
                    out.write("hasRelatedness("+elmt[:-1]+","+elmt2[:-1]+","+str(random.random())+")\n")




loc = sys.argv[1]

question(loc)
phrases()
ressourcesType()
hasRelatedness()

