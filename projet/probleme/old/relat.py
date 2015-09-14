#-*- coding: utf-8 -*-

with open("./ressources.txt","r") as inp:
#    with open("./entree.txt","r") as inp:
    with open("./related.txt",'w') as out:
        for line1 in inp:
            for line2 in inp:
                print "hasRelatedness("+line1[:-1]+","+line2[:-1]+","+" XXX  "+')'
                out.write("hasRelatedness("+line1[:-1]+","+line2[:-1]+","+" XXX  "+')\n')
